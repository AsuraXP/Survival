#!/usr/bin/env bash
# Extend the approved opening through completed Part 1 paragraphs without
# re-recording or modifying the original master/opening assets.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VIDEO_DIR="$ROOT/examples/the_store_had_everything"
SOURCE_MASTER="$VIDEO_DIR/production/master"
THROUGH="${THROUGH_PARAGRAPH:-2}"
if [[ ! "$THROUGH" =~ ^([2-9]|1[0-4])$ ]]; then
  printf 'THROUGH_PARAGRAPH must be an integer from 2 through 14.\n' >&2
  exit 1
fi
LEVEL="$(printf '%02d' "$THROUGH")"
PRODUCTION="$VIDEO_DIR/production_part01/p$LEVEL"
MASTER="$PRODUCTION/master"
PILOT="$VIDEO_DIR/PART01_THROUGH_P$LEVEL.mp4"
DELIVERABLE="$ROOT/STORE_PART01_P${LEVEL}_DELIVERABLE.zip"
export PYTHONPATH="$ROOT/pipeline${PYTHONPATH:+:$PYTHONPATH}"

if [[ "${FORCE_TTS:-0}" == "1" ]]; then
  printf 'ERROR: FORCE_TTS is forbidden for continuation; the approved opening must not be re-recorded.\n' >&2
  exit 1
fi
for required in narration.mp3 beats_with_timing.json moments_timing.json narration.log; do
  if [[ ! -f "$SOURCE_MASTER/$required" ]]; then
    printf 'ERROR: approved opening master is missing: %s\n' "$SOURCE_MASTER/$required" >&2
    printf 'Restore STORE_OPENING_PILOT_DELIVERABLE.zip under the project; do not record a replacement.\n' >&2
    exit 1
  fi
done

printf '\n==> Install narration dependency\n'
python -m pip install --disable-pip-version-check -q -r "$ROOT/pipeline/requirements.txt"
if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
  printf '\n==> Install ffmpeg/ffprobe\n'
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ffmpeg
fi

printf '\n==> Prepare accepted Part 1 coverage through paragraph %s\n' "$THROUGH"
cd "$ROOT"
rm -rf "$PRODUCTION"
python "$ROOT/pipeline/prepare_store_part01.py" \
  --project "$VIDEO_DIR" \
  --output-dir "$PRODUCTION" \
  --through-paragraph "$THROUGH"

# Copy the approved cache so all continuation timing/log outputs are separate
# from the original opening master.  The copied narration is reused, not TTS'd.
mkdir -p "$MASTER"
cp "$SOURCE_MASTER/narration.mp3" "$MASTER/narration.mp3"
cp "$SOURCE_MASTER/beats_with_timing.json" "$MASTER/beats_with_timing.json"
if [[ -d "$SOURCE_MASTER/audio" ]]; then
  cp -a "$SOURCE_MASTER/audio" "$MASTER/audio"
fi

printf '\n==> Reuse approved Andrew +0%% master; map covered WordBoundary moments\n'
set -o pipefail
python -m cartoonstyle.tts \
  --beats "$PRODUCTION/beats.jsonl" \
  --out-dir "$MASTER" \
  --voice en-US-AndrewNeural \
  --rate=+0% \
  --visuals "$PRODUCTION/timing_visuals.csv" 2>&1 | tee "$MASTER/narration.log"
if grep -E 'WARNING|proportional span|lead-in slot|narration\.mp3 written' "$MASTER/narration.log"; then
  printf 'ERROR: continuation requires clean reuse of the approved master and exact word matches.\n' >&2
  exit 1
fi
grep -E '\[tts\] [0-9]+ image moments locked to spoken words -> moments_timing\.json \[OK\]' \
  "$MASTER/narration.log" >/dev/null || {
  printf 'ERROR: covered moments were not locked to WordBoundary events.\n' >&2
  exit 1
}

printf '\n==> Stitch the approved opening plus continuation from the same master\n'
python -m cartoonstyle.stitch \
  --timing "$MASTER/beats_with_timing.json" \
  --images-dir "$PRODUCTION/stitch_frames" \
  --out "$PILOT" \
  --pick 0

printf '\n==> Continuation QA, including unchanged first-12 opening timings\n'
python "$ROOT/pipeline/qa_store_part01.py" \
  --video "$PILOT" \
  --project "$VIDEO_DIR" \
  --coverage "$PRODUCTION/coverage.json" \
  --timing "$MASTER/beats_with_timing.json" \
  --moments "$MASTER/moments_timing.json" \
  --opening-moments "$SOURCE_MASTER/moments_timing.json" \
  --out-json "$PRODUCTION/QA.json" \
  --out-md "$PRODUCTION/QA_REPORT.md"

printf '\n==> Package continuation and reusable approved master\n'
python - <<PY
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json
root = Path(r'''$ROOT''')
video_dir = Path(r'''$VIDEO_DIR''')
production = Path(r'''$PRODUCTION''')
deliverable = Path(r'''$DELIVERABLE''')
coverage = json.loads((production / 'coverage.json').read_text())
files = [
    'PART01_THROUGH_P$LEVEL.mp4',
    'PART01_SCRIPT.md',
    'OPENING_PILOT_PLAN.md',
    'opening_pilot/APPROVAL.md',
    'opening_pilot/visuals.csv',
    'part01/visuals.csv',
    'part01/CONTINUATION_PLAN.md',
    'production/master/narration.mp3',
    'production/master/beats_with_timing.json',
    'production/master/moments_timing.json',
    'production/master/narration.log',
    'production_part01/p$LEVEL/coverage.json',
    'production_part01/p$LEVEL/beats.jsonl',
    'production_part01/p$LEVEL/timing_visuals.csv',
    'production_part01/p$LEVEL/master/beats_with_timing.json',
    'production_part01/p$LEVEL/master/moments_timing.json',
    'production_part01/p$LEVEL/master/narration.log',
    'production_part01/p$LEVEL/QA_REPORT.md',
    'production_part01/p$LEVEL/QA.json',
]
files += [str(Path(item['frame_file']).relative_to(video_dir)) for item in coverage['moments']]
files += [str(path.relative_to(video_dir)) for path in sorted((video_dir / 'part01').glob('BATCH*_REVIEW.md'))]
with ZipFile(deliverable, 'w', compression=ZIP_DEFLATED, compresslevel=1) as archive:
    for name in files:
        path = video_dir / name
        if not path.is_file():
            raise FileNotFoundError(path)
        archive.write(path, arcname=f'STORE_PART01/{name}')
print(f'Packaged {len(files)} files: {deliverable}')
PY

printf '\n✅ DONE — Part 1 through paragraph %s, with the approved opening preserved:\n' "$THROUGH"
ls -lh "$PILOT" "$DELIVERABLE" "$PRODUCTION/QA_REPORT.md"
