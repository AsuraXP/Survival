"""Validate the finished Save the Guide Part 1 video using ffprobe/ffmpeg.

No third-party Python packages are required. The checks cover all 146 source
frames, verbatim narration rows, gapless WordBoundary moment timing, native
video geometry, streams, duration and a full decode of the completed MP4.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import struct
import subprocess
from pathlib import Path


def command(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, capture_output=True, text=True, check=True)


def media_duration(path: Path) -> float:
    result = command([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "csv=p=0", str(path),
    ])
    return float(result.stdout.strip())


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError(f"Not a valid PNG: {path}")
    return struct.unpack(">II", header[16:24])


def script_paragraphs(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [
        part.strip().replace("\n", " ")
        for part in re.split(r"\n\s*\n", text)
        if part.strip() and not part.startswith("#")
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", required=True)
    parser.add_argument("--visuals", required=True)
    parser.add_argument("--frames", required=True)
    parser.add_argument("--timing", required=True, help="beats_with_timing.json")
    parser.add_argument("--moments", required=True, help="moments_timing.json")
    parser.add_argument("--beats", required=True, help="beats.jsonl")
    parser.add_argument("--script", required=True)
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    video = Path(args.video)
    visuals_path = Path(args.visuals)
    frames_dir = Path(args.frames)
    timing_path = Path(args.timing)
    moments_path = Path(args.moments)
    beats_path = Path(args.beats)
    narration = timing_path.parent / "narration.mp3"
    out_json = Path(args.out_json)
    out_md = Path(args.out_md)

    checks: list[dict] = []

    def check(name: str, passed: bool, detail: str) -> None:
        checks.append({"name": name, "pass": bool(passed), "detail": detail})

    rows = list(csv.DictReader(visuals_path.open(encoding="utf-8", newline="")))
    expected_keys = [f"beat{int(r['slide_id']):02d}m{int(r['moment']):02d}" for r in rows]
    expected_text = {f"beat{int(r['slide_id']):02d}m{int(r['moment']):02d}": r["moment_text"] for r in rows}
    check("146 narration moments", len(rows) == 146, f"actual={len(rows)}")

    frame_files = sorted(frames_dir.glob("*.png"))
    bad_sizes = []
    missing = []
    for key in expected_keys:
        path = frames_dir / f"{key}_v00_s00000000.png"
        if not path.is_file():
            missing.append(key)
            continue
        if png_size(path) != (1376, 768):
            bad_sizes.append(key)
    check("146 planned frames present", not missing and len(frame_files) == 146,
          f"files={len(frame_files)} missing={missing}")
    check("Native source dimensions", not bad_sizes, f"expected=1376x768 bad={bad_sizes}")

    paragraphs = script_paragraphs(Path(args.script))
    check("14 script paragraphs", len(paragraphs) == 14, f"actual={len(paragraphs)}")
    for beat, paragraph in enumerate(paragraphs, 1):
        assembled = " ".join(r["moment_text"] for r in rows if int(r["slide_id"]) == beat)
        check(f"Verbatim narration beat {beat:02d}", assembled == paragraph,
              "moment rows join exactly to the approved paragraph" if assembled == paragraph else "MISMATCH")

    beats_jsonl = [json.loads(line) for line in beats_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    check("14 derived beats", len(beats_jsonl) == 14, f"actual={len(beats_jsonl)}")
    check("Beat text remains verbatim", [b["text"] for b in beats_jsonl] == paragraphs,
          "beats.jsonl matches the approved script")

    moments = json.loads(moments_path.read_text(encoding="utf-8"))
    ordered = sorted(moments, key=lambda item: float(item["start"]))
    check("146 timed moments", len(moments) == 146, f"actual={len(moments)}")
    check("Every moment locked once in narrative order", [m["key"] for m in ordered] == expected_keys,
          "timing keys match visuals.csv sequentially")
    check("Moment text preserved", all(m["text"] == expected_text.get(m["key"]) for m in ordered),
          "timing text matches visuals.csv")
    check("Timing starts at zero", bool(ordered) and abs(float(ordered[0]["start"])) <= 0.001,
          f"start={ordered[0]['start'] if ordered else 'n/a'}")
    check("Positive moment durations", all(float(m["sec"]) > 0 for m in ordered),
          f"minimum={min((float(m['sec']) for m in ordered), default=0):.3f}s")
    gaps = []
    for current, following in zip(ordered, ordered[1:]):
        end = float(current["start"]) + float(current["sec"])
        if abs(end - float(following["start"])) > 0.002:
            gaps.append((current["key"], following["key"], end, following["start"]))
    check("Gapless non-overlapping moment timing", not gaps, f"exceptions={gaps[:5]}")

    narration_duration = media_duration(narration)
    final_end = float(ordered[-1]["start"]) + float(ordered[-1]["sec"]) if ordered else 0.0
    check("Timing covers the one-take narration", abs(final_end - narration_duration) <= 0.05,
          f"narration={narration_duration:.3f}s final_frame_end={final_end:.3f}s")

    timed_beats = json.loads(timing_path.read_text(encoding="utf-8"))
    check("14 measured beat spans", len(timed_beats) == 14, f"actual={len(timed_beats)}")

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

    v = video_streams[0]
    a = audio_streams[0]
    check("Native video dimensions", (v.get("width"), v.get("height")) == (1376, 768),
          f"actual={v.get('width')}x{v.get('height')}")
    check("H.264 yuv420p at 30 fps",
          v.get("codec_name") == "h264" and v.get("pix_fmt") == "yuv420p" and v.get("r_frame_rate") == "30/1",
          f"codec={v.get('codec_name')} pix_fmt={v.get('pix_fmt')} fps={v.get('r_frame_rate')}")
    check("AAC narration stream", a.get("codec_name") == "aac", f"codec={a.get('codec_name')}")

    video_duration = float(probe["format"]["duration"])
    check("Video/audio duration agreement", abs(video_duration - narration_duration) <= 0.35,
          f"video={video_duration:.3f}s narration={narration_duration:.3f}s delta={abs(video_duration-narration_duration):.3f}s")

    decoded = subprocess.run(["ffmpeg", "-v", "error", "-xerror", "-i", str(video), "-f", "null", "-"],
                             capture_output=True, text=True)
    check("Full video decode without errors", decoded.returncode == 0,
          "decoded start-to-finish" if decoded.returncode == 0 else decoded.stderr.strip()[:1000])

    passed = all(item["pass"] for item in checks)
    report = {
        "status": "PASS" if passed else "FAIL",
        "video": str(video),
        "narration": str(narration),
        "frames": len(frame_files),
        "timed_moments": len(moments),
        "narration_duration_seconds": round(narration_duration, 3),
        "video_duration_seconds": round(video_duration, 3),
        "video_stream": v,
        "audio_stream": a,
        "checks": checks,
    }
    out_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    minutes = int(video_duration // 60)
    seconds = video_duration - minutes * 60
    lines = [
        "# Save the Guide — Part 1 Video QA",
        "",
        f"**Status: {'PASS' if passed else 'FAIL'}**",
        "",
        f"Completed video: `{video.name}`",
        f"Runtime: **{minutes}:{seconds:04.1f}** ({video_duration:.3f} seconds)",
        f"Frames/moments: **{len(frame_files)}/{len(moments)}**",
        f"Video: **{v.get('width')}×{v.get('height')}**, {v.get('codec_name')}, {v.get('pix_fmt')}, {v.get('r_frame_rate')} fps",
        f"Audio: **{a.get('codec_name')}**, one continuous narration take",
        "Visual assembly: **hard cuts between native still frames; no captions or Ken Burns motion**",
        "",
        "| Check | Result | Detail |",
        "|---|---|---|",
    ]
    for item in checks:
        detail = item["detail"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {item['name']} | {'PASS' if item['pass'] else 'FAIL'} | {detail} |")
    lines += [
        "",
        "The QA runner validates all 146 frame files, every narration row, gapless moment timing, native video geometry, stream formats, duration agreement and a complete decode of the finished MP4.",
        "",
    ]
    out_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"[qa] {report['status']}: {len(moments)} moments, {len(frame_files)} frames, {video_duration:.3f}s -> {out_md}")
    if not passed:
        failed = [item["name"] for item in checks if not item["pass"]]
        raise SystemExit("QA failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
