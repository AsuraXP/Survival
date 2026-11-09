#!/usr/bin/env bash
# run_cold_survival_kaggle.sh — STATE 6 runner for COLD SURVIVAL EP1.
# Audio (TTS/mix/encode) happens ONLY here on Kaggle. Never in the authoring workspace.
# Pipeline: deps -> clone/update -> preflight -> one-take Edge-TTS w/ word timestamps ->
#           robust monotonic word alignment -> PIL even-snap black-canvas pre-padding ->
#           frame-grid-exact per-beat segments, HARD CUTS only -> concat + loudnorm -14 LUFS
#           -> cold_survival_DELIVERABLE.zip
# v2 fix: cuts are aligned by monotonic token<->boundary matching (never by raw char
# offsets, which drift between punctuated script text and TTS boundary transcript),
# and each beat is encoded as its own segment with an exact frame count, so no player
# or demuxer can collapse slide durations.
set -euo pipefail

SLUG="cold_survival"
BRANCH="arena/23004249-survival"
REPO_URL="https://github.com/AsuraXP/Survival.git"
VOICE="en-US-AndrewNeural"
RATE="+10%"
FPS=30
WORK="$(pwd)/${SLUG}_kaggle_work"
PROJ="${SLUG}_video"
RUNNER_VERSION="v5-wordbound-guard"
SCRIPT="$(readlink -f "$0")"
rm -rf "${WORK}"          # never reuse manifests/segs from a previous run
mkdir -p "${WORK}"
echo "== runner ${RUNNER_VERSION}"

echo "== [1/7] deps @ $(date +%T)"
python3 -m pip install --quiet edge-tts pillow 2>&1 | tail -1 || true
if ! command -v ffmpeg >/dev/null 2>&1; then
  (apt-get update -y && apt-get install -y ffmpeg) >/dev/null 2>&1 || { sudo apt-get update -y && sudo apt-get install -y ffmpeg; }
fi
command -v ffmpeg >/dev/null 2>&1 || { echo "FATAL: ffmpeg unavailable"; exit 1; }

echo "== [2/7] clone/update repo @ ${BRANCH} @ $(date +%T)"
if [ -d Survival/.git ]; then
  BEFORE=$(git -C Survival rev-parse HEAD)
  git -C Survival fetch --depth 1 origin "${BRANCH}"
  git -C Survival reset --hard FETCH_HEAD
  AFTER=$(git -C Survival rev-parse HEAD)
  if [ "${BEFORE}" != "${AFTER}" ] && [ -z "${CS_SELFEXEC:-}" ]; then
    echo "== runner file changed during update -> re-exec from byte 0"
    CS_SELFEXEC=1 exec bash "${SCRIPT}"
  fi
else
  git clone --depth 1 --branch "${BRANCH}" "${REPO_URL}" Survival
fi
cd Survival
echo "== executing commit $(git rev-parse HEAD | cut -c1-10) with runner ${RUNNER_VERSION}"

echo "== [3/7] preflight (die on missing frames / voice / files) @ $(date +%T)"
python3 -u - "${PROJ}" <<'PYEOF'
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

echo "== [4/7] one continuous TTS take + word-level timestamps -> word-locked hard cuts @ $(date +%T)"
python3 -u - "${PROJ}" "${WORK}" "${VOICE}" "${RATE}" "${FPS}" <<'PYEOF'
import csv, os, re, sys, asyncio, json, subprocess, time
import edge_tts
proj, work, voice, rate, FPS = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5])
rows = list(csv.DictReader(open(f'{proj}/visuals.csv')))
texts = [r['moment_text'] for r in rows]
full = ' '.join(texts)
tokens = full.split()
starts = []           # token index where each beat begins
pos = 0
for t in texts:
    starts.append(pos)
    pos += len(t.split())

async def run():
    comm = edge_tts.Communicate(full, voice, rate=rate, boundary="WordBoundary")
    audio = bytearray(); bounds = []
    t0 = time.monotonic(); last = t0
    async for chunk in comm.stream():
        now = time.monotonic()
        if now - t0 > 900:
            raise TimeoutError('TTS stream exceeded 15 minutes')
        if now - last > 60:
            print(f'  tts streaming… {len(audio) * 8 // 48000}s of audio buffered', flush=True)
            last = now
        if chunk['type'] == 'audio':
            audio.extend(chunk['data'])
        elif chunk['type'] == 'WordBoundary':
            bounds.append((chunk['text'], chunk['offset'] / 1e7))   # 100ns ticks -> s
    return bytes(audio), bounds
bounds = None
for attempt in (1, 2):
    try:
        audio, bounds = asyncio.run(run())
        break
    except TimeoutError as e:
        print(f'  TTS attempt {attempt} timed out: {e}', flush=True)
        if attempt == 2:
            raise SystemExit('FATAL: TTS stream timed out twice — voice service unreachable')
open(f'{work}/voice.mp3', 'wb').write(audio)
print(f'  word boundaries received: {len(bounds)} events / {len(tokens)} script tokens', flush=True)
if len(bounds) < 0.8 * len(tokens):
    raise SystemExit('FATAL: WordBoundary channel dead (sentence-level events?) — '
                     'refusing to guess timing; aborting')

# ---ALIGN---
# robust monotonic token<->boundary alignment (no char offsets anywhere)
ONES = ['zero','one','two','three','four','five','six','seven','eight','nine','ten',
        'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen',
        'eighteen','nineteen']
TENS = ['','', 'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def num_words(n):
    if n < 20: return [ONES[n]]
    if n < 100:
        w = [TENS[n // 10]]
        if n % 10: w.append(ONES[n % 10])
        return w
    if n < 1000:
        w = [ONES[n // 100], 'hundred']
        if n % 100: w += num_words(n % 100)
        return w
    w = num_words(n // 1000) + ['thousand']
    if n % 1000: w += num_words(n % 1000)
    return w
def norm(w): return re.sub(r'[^a-z0-9]+', '', w.lower())
def forms(tok):
    f = [norm(tok)]
    if re.fullmatch(r'\d{1,4}', tok):
        f.append(''.join(norm(w) for w in num_words(int(tok))))
    return f
def align(bounds, tokens, starts, window=16):
    cuts = []
    bi = 0; last_t = 0.0; last_tok = 0; spw = 0.32   # seconds-per-word EMA seed
    for s in starts:                                  # beat 0 included: consume its boundary
        target = forms(tokens[s]); hit = None
        for j in range(bi, min(bi + window, len(bounds))):
            acc = ''
            for m in range(3):                       # merges splits: forty+seven, don't+care
                if j + m >= len(bounds): break
                acc += norm(bounds[j + m][0])
                if acc and acc in target:
                    hit = (j, bounds[j][1]); break
            if hit: break
        if hit:
            j, t = hit
            gap_tok = max(1, s - last_tok)
            spw = 0.5 * spw + 0.5 * max(0.05, (t - last_t) / gap_tok)
            cuts.append(t); bi = j + 1; last_t = t; last_tok = s
        else:                                        # rare: spoken form unmatched -> EMA estimate
            cuts.append(last_t + spw * (s - last_tok)); last_tok = s
    cuts[0] = 0.0                                     # reel starts with the audio
    for k in range(1, len(cuts)):                    # monotonic, min beat 0.30 s
        cuts[k] = max(cuts[k], cuts[k - 1] + 0.30)
    return cuts
# ---END ALIGN---
cuts = align(bounds, tokens, starts)

dur = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration',
                            '-of','csv=p=0', f'{work}/voice.mp3'],
                           capture_output=True, text=True).stdout.strip())
cuts.append(dur)
frame_edges = [round(c * FPS) for c in cuts]
for k in range(1, len(frame_edges)):                 # exact frame grid, strictly increasing
    frame_edges[k] = max(frame_edges[k], frame_edges[k - 1] + 9)
manifest = []
for i, r in enumerate(rows):
    f = f"{proj}/frames/beat{int(r['slide_id']):02d}m{int(r['moment']):02d}.png"
    manifest.append({'frame': f, 'start': cuts[i], 'end': cuts[i + 1],
                     'frames': frame_edges[i + 1] - frame_edges[i]})
json.dump(manifest, open(f'{work}/manifest.json', 'w'), indent=1)
open(f'{work}/video_dur.txt', 'w').write(f'{frame_edges[-1] / FPS:.6f}')
ds = [m['end'] - m['start'] for m in manifest]
ds.sort()
print(f'TTS done: {dur:.1f}s audio | {len(manifest)} word-locked hard cuts | '
      f'beat len min/med/max = {ds[0]:.2f}/{ds[len(ds)//2]:.2f}/{ds[-1]:.2f}s | '
      f'total video frames = {frame_edges[-1]}')
if ds[0] < 0.25 or frame_edges[-1] < int(dur * FPS) - FPS:
    print('FATAL: alignment collapsed (flash-frame risk)'); sys.exit(1)
PYEOF

echo "== [5/7] PIL even-snap black-canvas pre-padding (no -vf pad/scale later!) @ $(date +%T)"
python3 -u - "${PROJ}" "${WORK}" <<'PYEOF'
import json, os, sys
from PIL import Image
proj, work = sys.argv[1], sys.argv[2]
man = json.load(open(f'{work}/manifest.json'))
ims = [Image.open(m['frame']) for m in man]
W = max(im.width for im in ims); H = max(im.height for im in ims)
W += W % 2; H += H % 2
os.makedirs(f'{work}/padded', exist_ok=True)
for m, im in zip(man, ims):
    canvas = Image.new('RGB', (W, H), (0, 0, 0))
    canvas.paste(im.convert('RGB'), (0, 0))
    canvas.save(f"{work}/padded/" + os.path.basename(m['frame']), optimize=False, compress_level=6)
print(f'padded {len(man)} frames to {W}x{H} (even) on black RGB canvas')
PYEOF

echo "== [6/7] frame-grid-exact segments + HARD-CUT concat + aac192k + loudnorm -14 LUFS + 30fps libx264 yuv420p @ $(date +%T)"
python3 -u - "${WORK}" "${FPS}" <<'PYEOF'
import json, os, subprocess, sys
work, FPS = sys.argv[1], sys.argv[2]
man = json.load(open(f'{work}/manifest.json'))
if sorted(m['frames'] for m in man)[0] < 8:
    raise SystemExit('FATAL: segment frame counts collapsed (strobe risk) — refusing to encode')
segdir = f'{work}/segs'; os.makedirs(segdir, exist_ok=True)
for i, m in enumerate(man):
    src = f"{work}/padded/" + os.path.basename(m['frame'])
    out = f'{segdir}/seg{i:04d}.mp4'
    subprocess.run(['ffmpeg','-y','-v','error','-loop','1','-framerate',FPS,'-i',src,
                    '-frames:v',str(m['frames']),'-c:v','libx264','-preset','veryfast',
                    '-crf','18','-pix_fmt','yuv420p',out], check=True)
    if i % 20 == 0 or i == len(man) - 1:
        print(f'  seg {i + 1}/{len(man)} encoded', flush=True)
with open(f'{work}/segs.txt','w') as fh:
    for i in range(len(man)):
        fh.write(f"file '{segdir}/seg{i:04d}.mp4'\n")
tot = sum(m['frames'] for m in man) / int(FPS)
fs = sorted(m['frames'] for m in man)
print(f'{len(man)} segments encoded, exact frame counts, total {tot:.1f}s, zero transitions')
print(f'seg frames min/med/max = {fs[0]}/{fs[len(fs)//2]}/{fs[-1]} '
      f'({fs[0]/int(FPS):.2f}s / {fs[len(fs)//2]/int(FPS):.2f}s / {fs[-1]/int(FPS):.2f}s per beat)')
if fs[0] < 8:
    raise SystemExit('FATAL: segment frame counts collapsed (strobe risk) — aborting before encode finish')
PYEOF
VID_DUR=$(cat "${WORK}/video_dur.txt")
echo "== loudnorm -14 LUFS pre-pass on narration @ $(date +%T)"
ffmpeg -y -v error -i "${WORK}/voice.mp3" -af "loudnorm=I=-14:TP=-1.5:LRA=11,apad" \
  -t "${VID_DUR}" -c:a aac -b:a 192k "${WORK}/voice_norm.m4a"
echo "== final mux (video stream-copy + pre-normalized audio, zero filters at mux) @ $(date +%T)"
ffmpeg -y -v error -f concat -safe 0 -i "${WORK}/segs.txt" -i "${WORK}/voice_norm.m4a" \
  -c:v copy -c:a copy -movflags +faststart "${WORK}/VIDEO.mp4"
echo "== mux done @ $(date +%T)"
ffprobe -v error -show_entries format=duration -of csv=p=0 "${WORK}/VIDEO.mp4"

echo "== [7/7] package deliverable @ $(date +%T)"
cp "${WORK}/VIDEO.mp4" ./VIDEO.mp4
zip -j -q "${SLUG}_DELIVERABLE.zip" VIDEO.mp4 "${PROJ}/thumbnail.jpg" "${PROJ}/metadata.json" "${PROJ}/script.md" "${PROJ}/youtube.txt"
ls -la "${SLUG}_DELIVERABLE.zip" VIDEO.mp4
echo "== DONE: ${SLUG}_DELIVERABLE.zip (VIDEO.mp4 + thumbnail.jpg + metadata.json + script.md + youtube.txt)"
