# Kaggle — Part 1 Continuation Through Paragraph 2

## Prerequisite

Run this in the **same Kaggle session** as the approved opening so `Survival/examples/the_store_had_everything/production/master/` still contains the approved narration, beat timing, opening moments and narration log. The continuation runner copies that cache and never re-records it. `FORCE_TTS` is forbidden.

For a fresh session, first restore the opening deliverable's `production/master/` directory under the cloned project. Do not generate a replacement master.

## One-cell run

```python
import subprocess
from IPython.display import Video, FileLink, display

subprocess.run(
    "cd Survival && "
    "git pull --ff-only origin arena/35064a39-survival && "
    "THROUGH_PARAGRAPH=2 bash run_store_part01.sh",
    shell=True,
    check=True,
)

video_path = "Survival/examples/the_store_had_everything/PART01_THROUGH_P02.mp4"
display(Video(video_path, embed=True))
display(FileLink(video_path, result_html_prefix="Download continued video: "))
display(FileLink(
    "Survival/STORE_PART01_P02_DELIVERABLE.zip",
    result_html_prefix="Download continuation package: "
))
display(FileLink(
    "Survival/examples/the_store_had_everything/production_part01/p02/QA_REPORT.md",
    result_html_prefix="Open QA report: "
))
```

## Result and safeguards

- `PART01_THROUGH_P02.mp4`: approved 12-frame opening plus six new paragraph-2 frames, all hard-cut to the same master take.
- `STORE_PART01_P02_DELIVERABLE.zip`: continued video, all 18 covered frames, manifests/reviews, covered timings, QA and the approved master assets.
- QA checks the first 12 keys, text, starts and durations against the original opening master, then validates the longer video and a full decode.
- The original `OPENING_PILOT.mp4` and `production/master/` files are not modified.
