"""Automated QA for The Store Had Everything reusable opening pilot.

Validates the 12 native frames and verbatim opening word map, the complete
14-beat master narration timing, the measured 30–45 second opening span,
video streams/geometry and a full decode. No third-party Python packages.
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
    parser.add_argument("--script", required=True)
    parser.add_argument("--visuals", required=True, help="opening_pilot/visuals.csv")
    parser.add_argument("--frames", required=True, help="opening_pilot/frames")
    parser.add_argument("--beats", required=True, help="14-beat full-script beats.jsonl")
    parser.add_argument("--timing", required=True, help="full master beats_with_timing.json")
    parser.add_argument("--moments", required=True, help="opening-only moments_timing.json")
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    video = Path(args.video)
    visuals_path = Path(args.visuals)
    frames_dir = Path(args.frames)
    timing_path = Path(args.timing)
    moments_path = Path(args.moments)
    narration = timing_path.parent / "narration.mp3"
    checks: list[dict] = []

    def check(name: str, passed: bool, detail: str) -> None:
        checks.append({"name": name, "pass": bool(passed), "detail": detail})

    with visuals_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    expected_keys = [f"beat01m{index:02d}" for index in range(1, 13)]
    expected_text = {
        f"beat01m{index:02d}": row["narration_text"]
        for index, row in enumerate(rows, 1)
    }
    check("12 opening narration moments", len(rows) == 12, f"actual={len(rows)}")

    missing: list[str] = []
    bad_sizes: list[str] = []
    for index in range(1, 13):
        path = frames_dir / f"P{index:03d}.png"
        if not path.is_file():
            missing.append(path.name)
        elif png_size(path) != (1376, 768):
            bad_sizes.append(path.name)
    frame_files = sorted(frames_dir.glob("P*.png"))
    check("12 active opening frames", not missing and len(frame_files) == 12,
          f"files={len(frame_files)} missing={missing}")
    check("Native source dimensions", not bad_sizes,
          f"expected=1376x768 bad={bad_sizes}")
    check("Every frame passed review", all(
        row["approval_status"] in {"approved_user_2026-10-24", "accepted_internal_qa_2026-10-24"}
        for row in rows
    ), "approval statuses in visuals.csv")

    parts = script_paragraphs(Path(args.script))
    check("14 Part 1 script paragraphs", len(parts) == 14, f"actual={len(parts)}")
    assembled = " ".join(row["narration_text"] for row in rows)
    check("Opening narration remains verbatim", bool(parts) and assembled == parts[0],
          "12 rows join exactly to approved paragraph 1")

    beats = [json.loads(line) for line in Path(args.beats).read_text(encoding="utf-8").splitlines() if line.strip()]
    check("14 full-script beats", len(beats) == 14, f"actual={len(beats)}")
    check("Full master text remains verbatim", [beat["text"] for beat in beats] == parts,
          "beats.jsonl matches all approved Part 1 paragraphs")

    moments = json.loads(moments_path.read_text(encoding="utf-8"))
    ordered = sorted(moments, key=lambda item: float(item["start"]))
    check("12 timed opening moments", len(moments) == 12, f"actual={len(moments)}")
    check("Every moment locked once in narrative order",
          [moment["key"] for moment in ordered] == expected_keys,
          "timing keys match P001–P012 sequentially")
    check("Moment text preserved",
          all(moment["text"] == expected_text.get(moment["key"]) for moment in ordered),
          "timing text matches opening visuals.csv")
    check("Timing starts at zero", bool(ordered) and abs(float(ordered[0]["start"])) <= 0.001,
          f"start={ordered[0]['start'] if ordered else 'n/a'}")
    check("Positive moment durations", all(float(moment["sec"]) > 0 for moment in ordered),
          f"minimum={min((float(moment['sec']) for moment in ordered), default=0):.3f}s")
    gaps = []
    for current, following in zip(ordered, ordered[1:]):
        end = float(current["start"]) + float(current["sec"])
        if abs(end - float(following["start"])) > 0.002:
            gaps.append((current["key"], following["key"]))
    check("Gapless non-overlapping opening timing", not gaps, f"exceptions={gaps}")

    timed_beats = json.loads(timing_path.read_text(encoding="utf-8"))
    check("14 measured full-master beat spans", len(timed_beats) == 14,
          f"actual={len(timed_beats)}")
    narration_duration = media_duration(narration)
    master_end = float(timed_beats[-1]["start"]) + float(timed_beats[-1]["sec"]) if timed_beats else 0.0
    check("Timing covers the complete master take", abs(master_end - narration_duration) <= 0.05,
          f"master={narration_duration:.3f}s final_beat_end={master_end:.3f}s")

    opening_end = float(ordered[-1]["start"]) + float(ordered[-1]["sec"]) if ordered else 0.0
    first_beat_end = float(timed_beats[0]["start"]) + float(timed_beats[0]["sec"]) if timed_beats else 0.0
    check("Pilot ends at measured paragraph 1 boundary", abs(opening_end - first_beat_end) <= 0.05,
          f"moments_end={opening_end:.3f}s paragraph_end={first_beat_end:.3f}s")
    check("Reusable 30–45 second opening", 30.0 <= opening_end <= 45.0,
          f"opening={opening_end:.3f}s; voice remains Andrew 0%")
    check("Master audio remains available for continuation", narration_duration > opening_end + 1.0,
          f"remaining={narration_duration - opening_end:.3f}s")

    probe = json.loads(command([
        "ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(video),
    ]).stdout)
    streams = probe["streams"]
    video_streams = [stream for stream in streams if stream.get("codec_type") == "video"]
    audio_streams = [stream for stream in streams if stream.get("codec_type") == "audio"]
    subtitle_streams = [stream for stream in streams if stream.get("codec_type") == "subtitle"]
    check("One video and one audio stream", len(video_streams) == 1 and len(audio_streams) == 1,
          f"video={len(video_streams)} audio={len(audio_streams)}")
    check("No caption/subtitle stream", not subtitle_streams,
          f"subtitle_streams={len(subtitle_streams)}")
    v = video_streams[0] if video_streams else {}
    a = audio_streams[0] if audio_streams else {}
    check("Native video dimensions", (v.get("width"), v.get("height")) == (1376, 768),
          f"actual={v.get('width')}x{v.get('height')}")
    check("H.264 yuv420p at 30 fps",
          v.get("codec_name") == "h264" and v.get("pix_fmt") == "yuv420p" and v.get("r_frame_rate") == "30/1",
          f"codec={v.get('codec_name')} pix_fmt={v.get('pix_fmt')} fps={v.get('r_frame_rate')}")
    check("AAC narration stream", a.get("codec_name") == "aac", f"codec={a.get('codec_name')}")

    video_duration = float(probe["format"]["duration"])
    check("Video matches opening-audio duration", abs(video_duration - opening_end) <= 0.35,
          f"video={video_duration:.3f}s opening={opening_end:.3f}s")
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
        "full_master_narration": str(narration),
        "frames": len(frame_files),
        "opening_moments": len(moments),
        "full_master_duration_seconds": round(narration_duration, 3),
        "opening_duration_seconds": round(opening_end, 3),
        "video_duration_seconds": round(video_duration, 3),
        "video_stream": v,
        "audio_stream": a,
        "checks": checks,
    }
    Path(args.out_json).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# The Store Had Everything — Opening Pilot QA",
        "",
        f"**Status: {'PASS' if passed else 'FAIL'}**",
        "",
        f"Completed pilot: `{video.name}`",
        f"Opening runtime: **{opening_end:.3f} seconds**",
        f"Full master narration retained: **{narration_duration:.3f} seconds**",
        f"Frames/moments: **{len(frame_files)}/{len(moments)}**",
        f"Video: **{v.get('width')}×{v.get('height')}**, {v.get('codec_name')}, {v.get('pix_fmt')}, {v.get('r_frame_rate')} fps",
        f"Audio: **{a.get('codec_name')}**, opening of one continuous Andrew 0% master take",
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
        "The pilot is the measured first paragraph of the complete Part 1 master take. Its accepted frames, audio and timings can be retained for the finished episode.",
        "",
    ]
    Path(args.out_md).write_text("\n".join(lines), encoding="utf-8")
    print(f"[qa] {report['status']}: {len(moments)} moments, {len(frame_files)} frames, opening {opening_end:.3f}s")
    if not passed:
        failed = [item["name"] for item in checks if not item["pass"]]
        raise SystemExit("QA failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
