"""Prepare a reusable Part 1 continuation through a completed paragraph.

The opening manifest stays separate and locked.  Continuation rows add their
paragraph/moment numbers explicitly.  The output always contains all 14 script
beats (for the existing full master) but only the covered visual moments.
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


def resolve(path: str) -> Path:
    value = Path(path)
    return (value if value.is_absolute() else Path.cwd() / value).resolve()


def read_rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--through-paragraph", type=int, required=True)
    args = parser.parse_args()
    if not 2 <= args.through_paragraph <= 14:
        raise SystemExit("--through-paragraph must be in the range 2..14")

    project = Path(args.project).resolve()
    output = Path(args.output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    parts = paragraphs(project / "PART01_SCRIPT.md")
    if len(parts) != 14:
        raise SystemExit(f"Expected 14 Part 1 paragraphs, found {len(parts)}")

    opening = read_rows(project / "opening_pilot/visuals.csv")
    continuation = read_rows(project / "part01/visuals.csv")
    if len(opening) != 12 or [row["moment_id"] for row in opening] != [f"P{i:03d}" for i in range(1, 13)]:
        raise SystemExit("Opening must remain the sequential 12-frame P001–P012 manifest")

    covered: list[tuple[int, int, dict]] = [(1, index, row) for index, row in enumerate(opening, 1)]
    future_count = 0
    for row in continuation:
        paragraph = int(row["script_paragraph"])
        if paragraph > args.through_paragraph:
            future_count += 1
            continue
        covered.append((paragraph, int(row["paragraph_moment"]), row))
    covered.sort(key=lambda item: int(item[2]["moment_id"][1:]))

    expected_count = 12 + sum(
        1 for row in continuation if int(row["script_paragraph"]) <= args.through_paragraph
    )
    if len(covered) != expected_count:
        raise SystemExit("Continuation coverage is not contiguous")
    expected_ids = [f"P{i:03d}" for i in range(1, expected_count + 1)]
    if [row["moment_id"] for _, _, row in covered] != expected_ids:
        raise SystemExit(f"Covered frame IDs must be sequential through P{expected_count:03d}")

    by_paragraph: dict[int, list[tuple[int, dict]]] = {}
    for paragraph, moment, row in covered:
        by_paragraph.setdefault(paragraph, []).append((moment, row))
    if sorted(by_paragraph) != list(range(1, args.through_paragraph + 1)):
        raise SystemExit("Missing a covered paragraph")

    manifest: list[dict] = []
    for paragraph, entries in by_paragraph.items():
        entries.sort(key=lambda item: item[0])
        if [moment for moment, _ in entries] != list(range(1, len(entries) + 1)):
            raise SystemExit(f"Paragraph {paragraph} moment numbers are not sequential")
        assembled = " ".join(row["narration_text"] for _, row in entries)
        if assembled != parts[paragraph - 1]:
            raise SystemExit(f"Moment text does not reproduce paragraph {paragraph} verbatim")
        for moment, row in entries:
            if row["approval_status"] not in ACCEPTED:
                raise SystemExit(f"{row['moment_id']} is not accepted: {row['approval_status']}")
            frame = resolve(row["frame_file"])
            if not frame.is_file() or png_size(frame) != (1376, 768):
                raise SystemExit(f"Missing/non-native frame for {row['moment_id']}: {frame}")
            if "rejected" in row["reference_files"]:
                raise SystemExit(f"Rejected reference listed for {row['moment_id']}")
            for reference in row["reference_files"].split(";"):
                if not resolve(reference).is_file():
                    raise SystemExit(f"Missing reference for {row['moment_id']}: {reference}")
            manifest.append({
                "key": f"beat{paragraph:02d}m{moment:02d}",
                "paragraph": paragraph,
                "paragraph_moment": moment,
                "moment_id": row["moment_id"],
                "text": row["narration_text"],
                "frame_file": str(frame),
            })

    with (output / "beats.jsonl").open("w", encoding="utf-8", newline="\n") as handle:
        for index, text in enumerate(parts, 1):
            handle.write(json.dumps({"beat": index, "text": text}, ensure_ascii=False) + "\n")
    with (output / "timing_visuals.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["slide_id", "moment", "moment_text", "visual_prompt"], lineterminator="\n")
        writer.writeheader()
        for item in manifest:
            writer.writerow({
                "slide_id": item["paragraph"],
                "moment": item["paragraph_moment"],
                "moment_text": item["text"],
                "visual_prompt": item["moment_id"],
            })

    stitch_frames = output / "stitch_frames"
    stitch_frames.mkdir(parents=True, exist_ok=True)
    for old in stitch_frames.iterdir():
        if old.is_file() or old.is_symlink():
            old.unlink()
    for item in manifest:
        (stitch_frames / f"{item['key']}_v00_s00000000.png").symlink_to(item["frame_file"])

    coverage = {
        "script_paragraphs": 14,
        "through_paragraph": args.through_paragraph,
        "moment_count": len(manifest),
        "opening_moment_count": 12,
        "paragraph_moments": {str(p): len(by_paragraph[p]) for p in sorted(by_paragraph)},
        "moments": manifest,
        "future_manifest_rows_ignored": future_count,
    }
    (output / "coverage.json").write_text(json.dumps(coverage, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"Part 1 preflight PASS: paragraph 1–{args.through_paragraph}, "
        f"{len(manifest)} accepted native frames, verbatim text and valid references."
    )
    print(f"Derived full-master beats and covered word map: {output}")


if __name__ == "__main__":
    main()
