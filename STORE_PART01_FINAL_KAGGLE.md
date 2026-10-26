# Kaggle — The Store Had Everything: Final Part 1

## Prerequisite

Use the **same Kaggle session as the approved opening**, or attach the approved `STORE_OPENING_PILOT_DELIVERABLE.zip` as a Kaggle input. The cell reuses that master and never records a replacement opening. Enable Internet for GitHub, package installation and any required system packages.

## One-cell run

```python
import os
import subprocess
import zipfile
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

MASTER = REPO / "examples/the_store_had_everything/production/master"
REQUIRED = (
    "narration.mp3",
    "beats_with_timing.json",
    "moments_timing.json",
    "narration.log",
)

# Restore only the approved cache if this is a fresh session. Never rerun TTS.
if any(not (MASTER / name).is_file() for name in REQUIRED):
    candidates = []
    input_root = Path("/kaggle/input")
    if input_root.exists():
        candidates.extend(sorted(input_root.rglob("STORE_OPENING_PILOT_DELIVERABLE.zip")))
    local_zip = WORK / "STORE_OPENING_PILOT_DELIVERABLE.zip"
    if local_zip.is_file():
        candidates.append(local_zip)
    if not candidates:
        raise FileNotFoundError(
            "Approved opening master missing. Use the approved opening session "
            "or attach STORE_OPENING_PILOT_DELIVERABLE.zip as a Kaggle input. "
            "No replacement narration will be recorded."
        )
    MASTER.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(candidates[0]) as archive:
        for name in REQUIRED:
            member = f"STORE_OPENING_PILOT/production/master/{name}"
            (MASTER / name).write_bytes(archive.read(member))
    print(f"Restored approved opening master from: {candidates[0]}")

env = os.environ.copy()
env["THROUGH_PARAGRAPH"] = "14"
env["FORCE_TTS"] = "0"
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

- `PART01_THROUGH_P14.mp4`: all 114 accepted native frames, hard-cut to the approved one-take Andrew `+0%` master.
- `STORE_PART01_P14_DELIVERABLE.zip`: video, all 114 frames, manifests/reviews, final SHA-256 frame audit, covered timings, media QA and reusable approved master assets.
- `production_part01/p14/QA_REPORT.md`: verifies all 114 WordBoundary-locked moments, unchanged first-12 opening timings, native H.264/AAC media, gapless timing and a full decode.

The runner stops on missing/non-native frames, unmatched narration, fallback timing, changed opening timings or media-QA failure. `FORCE_TTS=0` is explicit.
