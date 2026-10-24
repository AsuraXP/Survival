# Kaggle — The Store Had Everything Opening Pilot

## Run

1. Open a Kaggle notebook with **Internet enabled**.
2. Upload/open `STORE_OPENING_PILOT_KAGGLE.ipynb`, or paste the cell below.
3. Run the one cell. It clones `arena/35064a39-survival`, installs the pinned narration dependency, synthesizes the full Part 1 master, stitches the measured opening, runs QA and packages the deliverables.

```python
import subprocess
from IPython.display import FileLink, display

subprocess.run(
    "rm -rf Survival && "
    "git clone --depth 1 --single-branch -b arena/35064a39-survival "
    "https://github.com/AsuraXP/Survival.git && "
    "cd Survival && bash run_store_opening_pilot.sh",
    shell=True,
    check=True,
)

display(FileLink("Survival/examples/the_store_had_everything/OPENING_PILOT.mp4"))
display(FileLink("Survival/STORE_OPENING_PILOT_DELIVERABLE.zip"))
display(FileLink("Survival/examples/the_store_had_everything/opening_pilot/QA_REPORT.md"))
display(FileLink("Survival/examples/the_store_had_everything/production/master/narration.mp3"))
```

## What it produces

- `OPENING_PILOT.mp4`: the 12 accepted native frames, hard-cut to the actual opening WordBoundary timings.
- `STORE_OPENING_PILOT_DELIVERABLE.zip`: pilot, full master narration, timing data, QA, script, frame plan and accepted frames.
- `production/master/narration.mp3`: the **complete 14-paragraph Part 1 narration**, generated once with `en-US-AndrewNeural` at normal `+0%`.
- `production/master/beats_with_timing.json`: all 14 measured paragraph spans for later continuation.
- `production/master/moments_timing.json`: the 12 opening image spans.
- `opening_pilot/QA_REPORT.md`: automated checks, including the 30–45 second opening requirement and a full video decode.

## Why the pilot is reusable

The runner does not record a short standalone demo. It synthesizes all 986 approved Part 1 words in one take and uses only the measured first-paragraph segment for the pilot. If the pilot is accepted, the same master audio, opening frames and timings remain the beginning of the finished episode.

The runner refuses to stitch if any beat/moment needs proportional fallback timing, if a frame is missing/non-native, or if QA fails. Do not enable `FORCE_TTS` during normal continuation; it exists only for an intentional re-synthesis after a script or voice change.
