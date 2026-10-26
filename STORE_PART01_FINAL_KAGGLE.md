# Kaggle — The Store Had Everything: Final Part 1

## Run

Enable **Internet** and run the single cell below. No opening ZIP, prior Kaggle session or manual file restoration is required.

On a fresh session, the cell runs the opening builder once to create the complete 14-paragraph `en-US-AndrewNeural` master at normal `+0%`, then uses that same master for the full 114-frame video. If the master already exists, it is reused. The 12 opening frames remain locked; `FORCE_TTS=0` prevents a forced second take.

## One-cell run

```python
import os
import subprocess
from pathlib import Path
from IPython.display import Video, FileLink, display

BRANCH = "arena/35064a39-survival"
WORK = Path("/kaggle/working") if Path("/kaggle/working").exists() else Path.cwd()
REPO = WORK / "Survival"

if not REPO.exists():
    subprocess.run([
        "git", "clone", "--depth", "1", "--single-branch",
        "-b", BRANCH, "https://github.com/AsuraXP/Survival.git", str(REPO),
    ], check=True)
else:
    subprocess.run([
        "git", "-C", str(REPO), "pull", "--ff-only", "origin", BRANCH,
    ], check=True)

env = os.environ.copy()
env["FORCE_TTS"] = "0"
MASTER = REPO / "examples/the_store_had_everything/production/master"
REQUIRED = (
    "narration.mp3",
    "beats_with_timing.json",
    "moments_timing.json",
    "narration.log",
)

# Fresh session: build the master once. Existing session: reuse it.
if any(not (MASTER / name).is_file() for name in REQUIRED):
    subprocess.run(["bash", "run_store_opening_pilot.sh"], cwd=REPO, env=env, check=True)

if any(not (MASTER / name).is_file() for name in REQUIRED):
    raise RuntimeError("Master setup did not complete; full-video rendering was not started.")

env["THROUGH_PARAGRAPH"] = "14"
subprocess.run(["bash", "run_store_part01.sh"], cwd=REPO, env=env, check=True)

VIDEO = REPO / "examples/the_store_had_everything/PART01_THROUGH_P14.mp4"
PACKAGE = REPO / "STORE_PART01_P14_DELIVERABLE.zip"
QA = REPO / "examples/the_store_had_everything/production_part01/p14/QA_REPORT.md"

display(Video(str(VIDEO), embed=True))
display(FileLink(str(VIDEO), result_html_prefix="Download full Part 1 video: "))
display(FileLink(str(PACKAGE), result_html_prefix="Download full Part 1 package: "))
display(FileLink(str(QA), result_html_prefix="Open final media QA report: "))
```

## Outputs and safeguards

- `PART01_THROUGH_P14.mp4`: all 114 accepted native frames, hard-cut to one continuous Andrew `+0%` master.
- `STORE_PART01_P14_DELIVERABLE.zip`: video, all 114 frames, manifests/reviews, final SHA-256 frame audit, covered timings, media QA and reusable master assets.
- `production_part01/p14/QA_REPORT.md`: verifies all 114 WordBoundary-locked moments, unchanged first-12 timings within the same master, native H.264/AAC media, gapless timing and a full decode.

The runner stops on missing/non-native frames, unmatched narration, fallback timing, changed opening timings within the reused master or media-QA failure. A fresh session creates a fresh narration take; an existing master is reused rather than re-recorded.
