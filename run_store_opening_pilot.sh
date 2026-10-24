#!/usr/bin/env bash
# One-cell Kaggle production runner for The Store Had Everything opening pilot.
# Synthesizes the FULL approved Part 1 once, then stitches only paragraph 1.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VIDEO_DIR="$ROOT/examples/the_store_had_everything"
PRODUCTION="$VIDEO_DIR/production"
MASTER="$PRODUCTION/master"
PILOT="$VIDEO_DIR/OPENING_PILOT.mp4"
DELIVERABLE="$ROOT/STORE_OPENING_PILOT_DELIVERABLE.zip"
export PYTHONPATH="$ROOT/pipeline${PYTHONPATH:+:$PYTHONPATH}"

printf '\n==> Install narration dependency\n'
python -m pip install --disable-pip-version-check -q -r "$ROOT/pipeline/requirements.txt"

if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
  printf '\n==> Install ffmpeg/ffprobe\n'
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ffmpeg
fi

printf '\n==> Preflight: 14 script beats, 12 accepted native frames and verbatim opening map\n'
cd "$ROOT"
python "$ROOT/pipeline/prepare_store_pilot.py" \
  --project "$VIDEO_DIR" \
  --output-dir "$PRODUCTION"

printf '\n==> One continuous FULL Part 1 take: en-US-AndrewNeural at normal +0%%\n'
mkdir -p "$MASTER"
set -o pipefail
FORCE=()
if [[ "${FORCE_TTS:-0}" == "1" ]]; then
  FORCE=(--force)
fi
python -m cartoonstyle.tts \
  --beats "$PRODUCTION/beats.jsonl" \
  --out-dir "$MASTER" \
  --voice en-US-AndrewNeural \
  --rate=+0% \
  --visuals "$PRODUCTION/timing_visuals.csv" \
  "${FORCE[@]}" 2>&1 | tee "$MASTER/narration.log"

# Never accept proportional/fallback timing or a partially matched opening.
if grep -E 'WARNING|proportional span|lead-in slot' "$MASTER/narration.log"; then
  printf 'ERROR: narration/timing warnings require correction; refusing to stitch.\n' >&2
  exit 1
fi
grep -E '\[tts\] 12 image moments locked to spoken words -> moments_timing\.json \[OK\]' \
  "$MASTER/narration.log" >/dev/null || {
  printf 'ERROR: all 12 opening moments were not locked to WordBoundary events.\n' >&2
  exit 1
}

printf '\n==> Stitch the measured opening of the same full master take\n'
python -m cartoonstyle.stitch \
  --timing "$MASTER/beats_with_timing.json" \
  --images-dir "$PRODUCTION/stitch_frames" \
  --out "$PILOT" \
  --pick 0

printf '\n==> Automated master/pilot/video QA\n'
python "$ROOT/pipeline/qa_store_pilot.py" \
  --video "$PILOT" \
  --script "$VIDEO_DIR/PART01_SCRIPT.md" \
  --visuals "$VIDEO_DIR/opening_pilot/visuals.csv" \
  --frames "$VIDEO_DIR/opening_pilot/frames" \
  --beats "$PRODUCTION/beats.jsonl" \
  --timing "$MASTER/beats_with_timing.json" \
  --moments "$MASTER/moments_timing.json" \
  --out-json "$VIDEO_DIR/opening_pilot/video_qa.json" \
  --out-md "$VIDEO_DIR/opening_pilot/QA_REPORT.md"

printf '\n==> Package pilot and reusable Part 1 master assets\n'
python - <<PY
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(r'''$ROOT''')
video_dir = Path(r'''$VIDEO_DIR''')
deliverable = Path(r'''$DELIVERABLE''')
files = [
    'OPENING_PILOT.mp4',
    'PART01_SCRIPT.md',
    'OPENING_PILOT_PLAN.md',
    'opening_pilot/visuals.csv',
    'opening_pilot/FRAME_REVIEW.md',
    'opening_pilot/BATCH01_REVIEW.md',
    'opening_pilot/BATCH02_REVIEW.md',
    'opening_pilot/VALIDATION.md',
    'opening_pilot/QA_REPORT.md',
    'opening_pilot/video_qa.json',
    'production/beats.jsonl',
    'production/timing_visuals.csv',
    'production/master/narration.mp3',
    'production/master/beats_with_timing.json',
    'production/master/moments_timing.json',
    'production/master/narration.log',
]
files += [f'opening_pilot/frames/P{index:03d}.png' for index in range(1, 13)]
with ZipFile(deliverable, 'w', compression=ZIP_DEFLATED, compresslevel=1) as archive:
    for name in files:
        path = video_dir / name
        if not path.is_file():
            raise FileNotFoundError(path)
        archive.write(path, arcname=f'STORE_OPENING_PILOT/{name}')
print(f'Packaged {len(files)} files: {deliverable}')
PY

printf '\n✅ DONE — reusable opening pilot, full Part 1 master narration and QA:\n'
ls -lh "$PILOT" "$DELIVERABLE" "$VIDEO_DIR/opening_pilot/QA_REPORT.md" "$MASTER/narration.mp3"
