#!/usr/bin/env bash
# run_cold_survival_kaggle.sh — STATE 6 runner for COLD SURVIVAL EP1.
# Audio (TTS/mix/encode) happens ONLY here on Kaggle. Never in the authoring workspace.
# Pipeline: deps -> clone/update -> preflight -> one-take Edge-TTS w/ word timestamps ->
#           PIL even-snap black-canvas pre-padding -> hard-cut concat (word-locked) ->
#           loudnorm -14 LUFS -> cold_survival_DELIVERABLE.zip
set -euo pipefail

SLUG="cold_survival"
BRANCH="arena/23004249-survival"
REPO_URL="https://github.com/AsuraXP/Survival.git"
VOICE="en-US-AndrewNeural"
RATE="+10%"
WORK="$(pwd)/${SLUG}_kaggle_work"
PROJ="${SLUG}_video"

echo "== [1/7] deps"
python3 -m pip install --quiet edge-tts pillow 2>&1 | tail -1 || true
if ! command -v ffmpeg >/dev/null 2>&1; then
  (apt-get update -y && apt-get install -y ffmpeg) >/dev/null 2>&1 || sudo apt-get update -y && sudo apt-get install -y ffmpeg
fi
command -v ffmpeg >/dev/null 2>&1 || { echo "FATAL: ffmpeg unavailable"; exit 1; }

echo "== [2/7] clone/update repo @ ${BRANCH}"
if [ -d Survival/.git ]; then
  git -C Survival fetch --depth 1 origin "${BRANCH}"
  git -C Survival reset --hard FETCH_HEAD
  REPO=Survival
else
  git clone --depth 1 --branch "${BRANCH}" "${REPO_URL}" Survival
  REPO=Survival
fi
cd "${REPO}"
mkdir -p "${WORK}"

echo "== [3/7] preflight (die on missing frames / voice / files)"
python3 - "${PROJ}" <<'PYEOF'
import csv, os, sys, asyncio
proj = sys.argv[1]
rows = list(csv.DictReader(open(f'{proj}/visuals.csv')))
missing = [f"{proj}/frames/beat{int(r['slide_id']):02d}m{int(r['moment']):02d}.png"
           for r in rows if not os.path.exists(f"{proj}/frames/beat{int(r['slide_id']):02d}m{int(r['moment']):02d}.png")]
if missing:
    print('FATAL missing frames:', missing[:10], '...'); sys.exit(1)
for f in [f'{proj}/thumbnail.jpg', f'{proj}/metadata.json', f'{proj}/script.md', f'{proj}/youtube.txt']:
    if not os.path.exists(f): print('FATAL missing file:', f); sys.exit(1)
import edge_tts
async def chk():
    voices = await edge_tts.list_voices()
    return any(v['ShortName'] == 'en-US-AndrewNeural' for v in voices)
if not asyncio.run(chk()):
    print('FATAL: voice en-US-AndrewNeural unresolvable'); sys.exit(1)
print(f'preflight OK: {len(rows)} beats, all frames + assets present, voice resolvable')
PYEOF

echo "== [4/7] one continuous TTS take + word-level timestamps -> cuts"
python3 - "${PROJ}" "${WORK}" "${VOICE}" "${RATE}" <<'PYEOF'
import csv, os, re, sys, asyncio, json
import edge_tts
proj, work, voice, rate = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
rows = list(csv.DictReader(open(f'{proj}/visuals.csv')))
texts = [r['moment_text'] for r in rows]
full = ' '.join(texts)
tokens = full.split()
# char start of each token in `full`
cuts_tokens = []  # token index where each beat starts
pos = 0; starts = []
for t in texts:
    starts.append(pos)
    pos += len(t.split()) 
async def run():
    comm = edge_tts.Communicate(full, voice, rate=rate)
    audio = bytearray(); bounds = []
    async for chunk in comm.stream():
        if chunk['type'] == 'audio':
            audio.extend(chunk['data'])
        elif chunk['type'] == 'WordBoundary':
            bounds.append((chunk['text'], chunk['offset'] / 1e7))
    open(f'{work}/voice.mp3', 'wb').write(bytes(audio))
    return bounds
bounds = asyncio.run(run())
# reconstruct char spans of boundary texts inside `full` (space-joined)
recon = ' '.join(b[0] for b in bounds)
spans = []
p = 0
for b in bounds:
    i = recon.find(b[0], p)
    spans.append((i, i + len(b[0]), b[1]))
    p = i + len(b[0])
# char start of each of our tokens in `full`
tok_char = []
c = 0
for t in tokens:
    tok_char.append(c); c += len(t) + 1
def time_at_token(idx):
    target = tok_char[idx]
    for (s, e, tsec) in spans:
        if s <= target < e:
            return tsec
    return spans[-1][2] if spans else 0.0
cuts = [0.0]
for k in range(1, len(rows)):
    cuts.append(time_at_token(starts[k]))
import subprocess
dur = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{work}/voice.mp3'],capture_output=True,text=True).stdout.strip())
cuts.append(dur)
manifest = []
for i, r in enumerate(rows):
    f = f"{proj}/frames/beat{int(r['slide_id']):02d}m{int(r['moment']):02d}.png"
    manifest.append({'frame': f, 'start': cuts[i], 'end': cuts[i+1]})
json.dump(manifest, open(f'{work}/manifest.json','w'), indent=1)
print(f'TTS done: {dur:.1f}s audio, {len(manifest)} word-locked hard cuts')
PYEOF

echo "== [5/7] PIL even-snap black-canvas pre-padding (no -vf pad/scale later!)"
python3 - "${PROJ}" "${WORK}" <<'PYEOF'
import json, os, sys
from PIL import Image
proj, work = sys.argv[1], sys.argv[2]
man = json.load(open(f'{work}/manifest.json'))
paths = [m['frame'] for m in man]
ims = [Image.open(p) for p in paths]
W = max(im.width for im in ims); H = max(im.height for im in ims)
W = W + (W % 2); H = H + (H % 2)
os.makedirs(f'{work}/padded', exist_ok=True)
for m, im in zip(man, ims):
    canvas = Image.new('RGB', (W, H), (0, 0, 0))
    canvas.paste(im.convert('RGB'), (0, 0))
    out = f"{work}/padded/" + os.path.basename(m['frame'])
    canvas.save(out, optimize=False, compress_level=6)
print(f'padded {len(man)} frames to {W}x{H} (even) on black RGB canvas')
PYEOF

echo "== [6/7] hard-cut concat (word-locked) + aac192k + loudnorm -14 LUFS + 30fps libx264 yuv420p"
python3 - "${WORK}" <<'PYEOF'
import json, os, sys
work = sys.argv[1]
man = json.load(open(f'{work}/manifest.json'))
lines = []
for i, m in enumerate(man):
    d = max(0.04, m['end'] - m['start'])
    lines.append(f"file '{work}/padded/{os.path.basename(m['frame'])}'")
    lines.append(f"duration {d:.3f}")
lines.append(f"file '{work}/padded/{os.path.basename(man[-1]['frame'])}'")  # hold last frame
open(f'{work}/list.txt','w').write('\n'.join(lines) + '\n')
print('concat list written:', len(man), 'hard cuts, zero transitions')
PYEOF
ffmpeg -y -v error -f concat -safe 0 -i "${WORK}/list.txt" -i "${WORK}/voice.mp3" \
  -r 30 -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -af loudnorm=I=-14:TP=-1.5:LRA=11 \
  -movflags +faststart -shortest "${WORK}/VIDEO.mp4"
ffprobe -v error -show_entries format=duration,size -of default=nw=1 "${WORK}/VIDEO.mp4"

echo "== [7/7] package deliverable"
cp "${WORK}/VIDEO.mp4" ./VIDEO.mp4
zip -j -q "${SLUG}_DELIVERABLE.zip" VIDEO.mp4 "${PROJ}/thumbnail.jpg" "${PROJ}/metadata.json" "${PROJ}/script.md" "${PROJ}/youtube.txt"
ls -la "${SLUG}_DELIVERABLE.zip" VIDEO.mp4
echo "== DONE: ${SLUG}_DELIVERABLE.zip (VIDEO.mp4 + thumbnail.jpg + metadata.json + script.md + youtube.txt)"
