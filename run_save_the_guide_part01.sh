#!/usr/bin/env bash
# One-shot Kaggle production runner for Save the Guide — Part 1.
# Run from any directory; all paths resolve against this repository checkout.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VIDEO_DIR="$ROOT/examples/save_the_guide_part_01_video"
VIDEO_NAME="SAVE_THE_GUIDE_PART01.mp4"
DELIVERABLE="$ROOT/SAVE_THE_GUIDE_PART01_DELIVERABLE.zip"
export PYTHONPATH="$ROOT/pipeline${PYTHONPATH:+:$PYTHONPATH}"

printf '\n==> Install narration dependency\n'
python -m pip install --disable-pip-version-check -q -r "$ROOT/pipeline/requirements.txt"

if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
  printf '\n==> Install ffmpeg/ffprobe\n'
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ffmpeg
fi

cd "$VIDEO_DIR"

printf '\n==> Preflight: approved script, 146 moments and native frames\n'
python - <<'PY'
import csv, json, re, struct
from pathlib import Path
root = Path('.')
rows = list(csv.DictReader((root / 'visuals.csv').open(encoding='utf-8', newline='')))
assert len(rows) == 146, f'Expected 146 moments, found {len(rows)}'
expected = []
for row in rows:
    key = f"beat{int(row['slide_id']):02d}m{int(row['moment']):02d}"
    path = root / 'frames' / f'{key}_v00_s00000000.png'
    assert path.is_file(), f'Missing {path}'
    with path.open('rb') as handle:
        header = handle.read(24)
    assert header[:8] == b'\x89PNG\r\n\x1a\n' and header[12:16] == b'IHDR', path
    width, height = struct.unpack('>II', header[16:24])
    assert (width, height) == (1376, 768), f'{path}: {(width, height)}'
    expected.append(key)
actual = sorted(p.name for p in (root / 'frames').glob('*.png'))
assert len(actual) == 146, f'Expected exactly 146 frames, found {len(actual)}'
script = (root / 'script.md').read_text(encoding='utf-8')
paragraphs = [p.strip().replace('\n', ' ') for p in re.split(r'\n\s*\n', script) if p.strip() and not p.startswith('#')]
assert len(paragraphs) == 14
for beat, paragraph in enumerate(paragraphs, 1):
    assembled = ' '.join(r['moment_text'] for r in rows if int(r['slide_id']) == beat)
    assert assembled == paragraph, f'Narration mismatch in beat {beat}'
audit = list(csv.DictReader((root / 'FRAME_AUDIT.csv').open(encoding='utf-8', newline='')))
assert len(audit) == 146 and all(r['approval_status'] == 'approved' for r in audit)
print('Preflight PASS: 146 approved native frames and 146 verbatim narration rows.')
PY

printf '\n==> Derive the 14 narration beats\n'
python -m cartoonstyle.csv_to_beats --visuals visuals.csv --out beats.jsonl

printf '\n==> One continuous en-US-AndrewNeural take at -5%% + WordBoundary timing\n'
set -o pipefail
python -m cartoonstyle.tts \
  --beats beats.jsonl \
  --out-dir . \
  --voice en-US-AndrewNeural \
  --rate=-5% \
  --visuals visuals.csv 2>&1 | tee narration.log

# Never continue with proportional/fallback timing or a partially matched plan.
grep -E '\[tts\] 146 image moments locked to spoken words -> moments_timing\.json \[OK\]' narration.log >/dev/null || {
  printf 'ERROR: all 146 moments were not locked to WordBoundary events.\n' >&2
  exit 1
}

printf '\n==> Stitch 146 native stills with hard cuts and the one-take narration\n'
python -m cartoonstyle.stitch \
  --timing beats_with_timing.json \
  --images-dir frames/ \
  --out "$VIDEO_NAME" \
  --pick 0

printf '\n==> Full automated video QA\n'
python "$ROOT/pipeline/qa_save_guide.py" \
  --video "$VIDEO_NAME" \
  --visuals visuals.csv \
  --frames frames/ \
  --timing beats_with_timing.json \
  --moments moments_timing.json \
  --beats beats.jsonl \
  --script script.md \
  --out-json video_qa.json \
  --out-md QA_REPORT.md

printf '\n==> Package the completed deliverable\n'
python - <<PY
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(r'''$ROOT''')
video_dir = Path(r'''$VIDEO_DIR''')
deliverable = Path(r'''$DELIVERABLE''')
files = [
    'SAVE_THE_GUIDE_PART01.mp4',
    'narration.mp3',
    'narration.log',
    'beats.jsonl',
    'beats_with_timing.json',
    'moments_timing.json',
    'script.md',
    'visuals.csv',
    'FRAME_AUDIT.csv',
    'FULL_FRAME_AUDIT.md',
    'QA_REPORT.md',
    'video_qa.json',
    'PART02_HANDOFF.md',
]
with ZipFile(deliverable, 'w', compression=ZIP_DEFLATED, compresslevel=1) as archive:
    for name in files:
        path = video_dir / name
        if not path.is_file():
            raise FileNotFoundError(path)
        archive.write(path, arcname=f'SAVE_THE_GUIDE_PART01/{name}')
print(f'Packaged {len(files)} files: {deliverable}')
PY

printf '\n✅ DONE — completed video and deliverable ZIP:\n'
ls -lh "$VIDEO_DIR/$VIDEO_NAME" "$DELIVERABLE" "$VIDEO_DIR/QA_REPORT.md"
