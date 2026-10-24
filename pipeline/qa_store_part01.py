"""QA a Part 1 continuation without changing its approved opening."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from qa_store_pilot import command, media_duration, png_size, script_paragraphs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--coverage", required=True)
    parser.add_argument("--timing", required=True)
    parser.add_argument("--moments", required=True)
    parser.add_argument("--opening-moments", required=True)
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    project = Path(args.project)
    video = Path(args.video)
    timing_path = Path(args.timing)
    narration = timing_path.parent / "narration.mp3"
    coverage = json.loads(Path(args.coverage).read_text(encoding="utf-8"))
    moments = json.loads(Path(args.moments).read_text(encoding="utf-8"))
    opening_original = json.loads(Path(args.opening_moments).read_text(encoding="utf-8"))
    timed_beats = json.loads(timing_path.read_text(encoding="utf-8"))
    manifest = coverage["moments"]
    through = int(coverage["through_paragraph"])
    checks: list[dict] = []

    def check(name: str, passed: bool, detail: str) -> None:
        checks.append({"name": name, "pass": bool(passed), "detail": detail})

    parts = script_paragraphs(project / "PART01_SCRIPT.md")
    check("14 approved Part 1 paragraphs", len(parts) == 14, f"actual={len(parts)}")
    check("Continuous completed-paragraph coverage", 2 <= through <= 14, f"through={through}")
    check("14 measured full-master beats", len(timed_beats) == 14, f"actual={len(timed_beats)}")
    check("Full-master text remains verbatim", [beat["text"] for beat in timed_beats] == parts,
          "all 14 beat texts match the approved script")

    missing: list[str] = []
    bad_sizes: list[str] = []
    for item in manifest:
        frame = Path(item["frame_file"])
        if not frame.is_file():
            missing.append(item["moment_id"])
        elif png_size(frame) != (1376, 768):
            bad_sizes.append(item["moment_id"])
    check("All covered native frames exist", not missing and not bad_sizes,
          f"frames={len(manifest)} missing={missing} bad={bad_sizes}")

    narration_duration = media_duration(narration)
    master_end = float(timed_beats[-1]["start"]) + float(timed_beats[-1]["sec"])
    check("Timing covers the complete master take", abs(master_end - narration_duration) <= 0.05,
          f"master={narration_duration:.3f}s final_beat_end={master_end:.3f}s")

    ordered = sorted(moments, key=lambda item: float(item["start"]))
    expected_keys = [item["key"] for item in manifest]
    check("Covered moment count", len(ordered) == int(coverage["moment_count"]) == len(manifest),
          f"actual={len(ordered)} expected={len(manifest)}")
    check("Every covered moment locked once in order", [m["key"] for m in ordered] == expected_keys,
          f"keys through paragraph {through}")
    expected_text = {item["key"]: item["text"] for item in manifest}
    check("Covered moment text preserved",
          all(m["text"] == expected_text.get(m["key"]) for m in ordered),
          "timing text matches the covered manifests")
    check("Timing starts at zero", bool(ordered) and abs(float(ordered[0]["start"])) <= 0.001,
          f"start={ordered[0]['start'] if ordered else 'n/a'}")
    check("Positive moment durations", all(float(m["sec"]) > 0 for m in ordered),
          f"minimum={min((float(m['sec']) for m in ordered), default=0):.3f}s")
    gaps = []
    for current, following in zip(ordered, ordered[1:]):
        end = float(current["start"]) + float(current["sec"])
        if abs(end - float(following["start"])) > 0.002:
            gaps.append((current["key"], following["key"]))
    check("Gapless non-overlapping continuation timing", not gaps, f"exceptions={gaps}")

    original = sorted(opening_original, key=lambda item: float(item["start"]))
    current_opening = ordered[:12]
    opening_same = len(original) == len(current_opening) == 12
    for before, after in zip(original, current_opening):
        opening_same = opening_same and before["key"] == after["key"] and before["text"] == after["text"]
        opening_same = opening_same and abs(float(before["start"]) - float(after["start"])) <= 0.001
        opening_same = opening_same and abs(float(before["sec"]) - float(after["sec"])) <= 0.001
    check("Approved opening timings remain unchanged", opening_same,
          "all first 12 keys, text, starts and durations match the opening master")
    opening_end = float(original[-1]["start"]) + float(original[-1]["sec"])
    covered_end = float(ordered[-1]["start"]) + float(ordered[-1]["sec"])
    paragraph_end = float(timed_beats[through - 1]["start"]) + float(timed_beats[through - 1]["sec"])
    check("Continuation ends at measured paragraph boundary", abs(covered_end - paragraph_end) <= 0.05,
          f"moments_end={covered_end:.3f}s paragraph_end={paragraph_end:.3f}s")
    check("New story follows the locked opening", covered_end > opening_end + 1.0,
          f"opening={opening_end:.3f}s continuation={covered_end:.3f}s")
    remaining = narration_duration - covered_end
    check("Master availability matches coverage", remaining > 1.0 if through < 14 else abs(remaining) <= 0.05,
          f"remaining={remaining:.3f}s")

    probe = json.loads(command([
        "ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(video),
    ]).stdout)
    streams = probe["streams"]
    video_streams = [s for s in streams if s.get("codec_type") == "video"]
    audio_streams = [s for s in streams if s.get("codec_type") == "audio"]
    subtitle_streams = [s for s in streams if s.get("codec_type") == "subtitle"]
    check("One video and one audio stream", len(video_streams) == 1 and len(audio_streams) == 1,
          f"video={len(video_streams)} audio={len(audio_streams)}")
    check("No caption/subtitle stream", not subtitle_streams, f"subtitle_streams={len(subtitle_streams)}")
    v = video_streams[0] if video_streams else {}
    a = audio_streams[0] if audio_streams else {}
    check("Native video dimensions", (v.get("width"), v.get("height")) == (1376, 768),
          f"actual={v.get('width')}x{v.get('height')}")
    check("H.264 yuv420p at 30 fps",
          v.get("codec_name") == "h264" and v.get("pix_fmt") == "yuv420p" and v.get("r_frame_rate") == "30/1",
          f"codec={v.get('codec_name')} pix_fmt={v.get('pix_fmt')} fps={v.get('r_frame_rate')}")
    check("AAC narration stream", a.get("codec_name") == "aac", f"codec={a.get('codec_name')}")

    video_duration = float(probe["format"]["duration"])
    v_duration = float(v.get("duration", video_duration))
    a_duration = float(a.get("duration", video_duration))
    check("Container matches covered narration", abs(video_duration - covered_end) <= 0.35,
          f"container={video_duration:.3f}s covered={covered_end:.3f}s")
    check("Video stream covers the measured ending", abs(v_duration - covered_end) <= 0.12,
          f"video_stream={v_duration:.3f}s covered={covered_end:.3f}s")
    check("Audio stream covers the measured ending", abs(a_duration - covered_end) <= 0.12,
          f"audio_stream={a_duration:.3f}s covered={covered_end:.3f}s")
    decoded = subprocess.run(
        ["ffmpeg", "-v", "error", "-xerror", "-i", str(video), "-f", "null", "-"],
        capture_output=True, text=True,
    )
    check("Full video decode without errors", decoded.returncode == 0,
          "decoded start-to-finish" if decoded.returncode == 0 else decoded.stderr.strip()[:1000])

    passed = all(item["pass"] for item in checks)
    report = {
        "status": "PASS" if passed else "FAIL",
        "video": str(video),
        "through_paragraph": through,
        "covered_moments": len(ordered),
        "opening_moments_unchanged": opening_same,
        "opening_duration_seconds": round(opening_end, 3),
        "covered_duration_seconds": round(covered_end, 3),
        "full_master_duration_seconds": round(narration_duration, 3),
        "video_duration_seconds": round(video_duration, 3),
        "checks": checks,
    }
    Path(args.out_json).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# The Store Had Everything — Part 1 Continuation QA",
        "",
        f"**Status: {'PASS' if passed else 'FAIL'}**",
        "",
        f"Coverage: **paragraph 1–{through}**, {len(ordered)} moments",
        f"Locked opening: **{opening_end:.3f} seconds**, first 12 timings unchanged",
        f"Continuation runtime: **{covered_end:.3f} seconds**",
        f"Full master retained: **{narration_duration:.3f} seconds**",
        "",
        "| Check | Result | Detail |",
        "|---|---|---|",
    ]
    for item in checks:
        detail = item["detail"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {item['name']} | {'PASS' if item['pass'] else 'FAIL'} | {detail} |")
    lines.append("")
    Path(args.out_md).write_text("\n".join(lines), encoding="utf-8")
    print(f"[qa] {report['status']}: paragraph 1–{through}, {len(ordered)} moments, {covered_end:.3f}s")
    if not passed:
        raise SystemExit("QA failed: " + ", ".join(item["name"] for item in checks if not item["pass"]))


if __name__ == "__main__":
    main()
