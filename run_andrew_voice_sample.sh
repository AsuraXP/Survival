#!/usr/bin/env bash
# Generate a short en-US-AndrewNeural voice sample at normal 0% speed.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SAMPLE_DIR="$ROOT/voice_samples"
TEXT_FILE="$SAMPLE_DIR/andrew_0pct_sample.txt"
OUTPUT_FILE="$SAMPLE_DIR/andrew_0pct_sample.mp3"

python -m pip install --disable-pip-version-check -q edge-tts==7.3.1

ROOT="$ROOT" TEXT_FILE="$TEXT_FILE" OUTPUT_FILE="$OUTPUT_FILE" python - <<'PY'
import asyncio
import os
from pathlib import Path
import edge_tts

text = Path(os.environ['TEXT_FILE']).read_text(encoding='utf-8').strip()
output = Path(os.environ['OUTPUT_FILE'])

async def main() -> None:
    communicate = edge_tts.Communicate(text, 'en-US-AndrewNeural', rate='+0%')
    audio = bytearray()
    async for chunk in communicate.stream():
        if chunk['type'] == 'audio':
            audio.extend(chunk['data'])
    if not audio:
        raise RuntimeError('Andrew sample returned no audio.')
    output.write_bytes(audio)
    print(f'Andrew 0% sample written: {output} ({len(audio):,} bytes)')

asyncio.run(main())
PY
