"""Preflight and derive Kaggle inputs for The Store Had Everything opening pilot.

No third-party packages or network access are required. The approved Part 1
script becomes 14 narration beats. The 12 accepted opening moments become
word-matching rows for beat 1 only, so one full master take can produce both
the reusable pilot and timing for later Part 1 continuation.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import struct
from pathlib import Path

ACCEPTED = {"approved_user_2026-10-24", "accepted_internal_qa_2026-10-24"}


def paragraphs(script: Path) -> list[str]:
    text = script.read_text(encoding="utf-8")
    return [
        part.strip().replace("\n", " ")
        for part in re.split(r"\n\s*\n", text)
        if part.strip() and not part.startswith("#")
    ]


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError(f"Not a valid PNG: {path}")
    return struct.unpack(">II", header[16:24])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, help="examples/the_store_had_everything")
    parser.add_argument("--output-dir", default="", help="default: PROJECT/production")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    opening = project / "opening_pilot"
    output = Path(args.output_dir).resolve() if args.output_dir else project / "production"
    output.mkdir(parents=True, exist_ok=True)

    parts = paragraphs(project / "PART01_SCRIPT.md")
    if len(parts) != 14:
        raise SystemExit(f"Expected 14 Part 1 paragraphs, found {len(parts)}")

    with (opening / "visuals.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 12:
        raise SystemExit(f"Expected 12 opening moments, found {len(rows)}")

    expected_ids = [f"P{index:03d}" for index in range(1, 13)]
    if [row["moment_id"] for row in rows] != expected_ids:
        raise SystemExit("Opening moment IDs are not sequential P001–P012")
    for row in rows:
        if row["approval_status"] not in ACCEPTED:
            raise SystemExit(f"{row['moment_id']} is not accepted: {row['approval_status']}")
        frame = Path(row["frame_file"])
        if not frame.is_absolute():
            frame = Path.cwd() / frame
        frame = frame.resolve()
        if not frame.is_file():
            raise SystemExit(f"Missing frame: {frame}")
        if png_size(frame) != (1376, 768):
            raise SystemExit(f"Non-native frame dimensions: {frame} -> {png_size(frame)}")
        for reference in row["reference_files"].split(";"):
            reference_path = Path(reference)
            if not reference_path.is_absolute():
                reference_path = Path.cwd() / reference_path
            if not reference_path.resolve().is_file():
                raise SystemExit(f"Missing reference for {row['moment_id']}: {reference_path}")
        if "rejected" in row["reference_files"]:
            raise SystemExit(f"Rejected reference listed for {row['moment_id']}")

    assembled = " ".join(row["narration_text"] for row in rows)
    if assembled != parts[0]:
        raise SystemExit("Opening moment text does not reproduce Part 1 paragraph 1 verbatim")

    with (output / "beats.jsonl").open("w", encoding="utf-8", newline="\n") as handle:
        for index, text in enumerate(parts, 1):
            handle.write(json.dumps({"beat": index, "text": text}, ensure_ascii=False) + "\n")

    with (output / "timing_visuals.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["slide_id", "moment", "moment_text", "visual_prompt"],
            lineterminator="\n",
        )
        writer.writeheader()
        for index, row in enumerate(rows, 1):
            writer.writerow({
                "slide_id": 1,
                "moment": index,
                "moment_text": row["narration_text"],
                "visual_prompt": row["moment_id"],
            })

    stitch_frames = output / "stitch_frames"
    stitch_frames.mkdir(parents=True, exist_ok=True)
    for old in stitch_frames.iterdir():
        if old.is_file() or old.is_symlink():
            old.unlink()
    for index, row in enumerate(rows, 1):
        source = Path(row["frame_file"]).resolve()
        key = f"beat01m{index:02d}"
        destination = stitch_frames / f"{key}_v00_s00000000.png"
        destination.symlink_to(source)

    print(
        "Preflight PASS: 14 approved script paragraphs, 12 accepted native opening frames, "
        "verbatim opening text and valid reference paths."
    )
    print(f"Derived full-script beats and opening-only word map: {output}")


if __name__ == "__main__":
    main()
