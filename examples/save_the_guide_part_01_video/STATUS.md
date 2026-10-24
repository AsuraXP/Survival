# Save the Guide — Part 1 Status

## Current stage

**PROJECT ON HOLD — the user has confirmed that Part 1 is complete and they have received the finished result. Preserve all assets for a possible later Part 2, but do not rework Part 1 or continue the series unless the user explicitly resumes it. The new active launch story is `The Store Had Everything`.**

## Production counter

| Counter | Frames |
|---|---:|
| Planned final narrative frames | **146** |
| Total approved | **146** |
| Frames awaiting review | **0** |
| **Total retained on disk** | **146** |
| Pending production corrections | **0** |
| **Planned frames not yet produced** | **0** |

## Completed

- Research, series bible, full 14-paragraph/1,009-word Part 1 script, approved locked reference pack and validated 146-moment visual plan.
- Full fresh whole-image audit: **142 frames passed unchanged and 4 corrected frames passed reinspection**. All four corrections are now user-approved.
- All **146 retained frames** validate at native **1376×768**, with one unique frame for every planned moment.
- All **146 narration rows** join verbatim to the 14 approved script paragraphs.
- `FRAME_AUDIT.csv` records every frame's audit result, approval and SHA-256 hash.
- `PART02_HANDOFF.md` records the exact ending state for Part 2 continuity.
- `pipeline/cartoonstyle/` contains the one-take/WordBoundary/hard-cut production code in Survival.
- `run_save_the_guide_part01.sh` performs preflight, TTS, mandatory 146/146 timing verification, stitching, QA and ZIP packaging.
- `SAVE_THE_GUIDE_PART01_KAGGLE.ipynb` provides the requested single Kaggle cell with completed-video and deliverable download links.
- Runner syntax, Python imports, verbatim beat derivation and a 146-moment synthetic stitch/full-QA fixture all passed locally; synthetic media is not retained in the repository.

## Kaggle production

Import `SAVE_THE_GUIDE_PART01_KAGGLE.ipynb` into Kaggle, enable Internet and run the single cell. The runner:

1. Clones this exact branch and validates all 146 approved native frames and verbatim narration rows.
2. Produces one continuous `en-US-AndrewNeural` narration take at `-5%`.
3. Requires the exact **146/146 WordBoundary `[OK]`** result; it stops rather than using fallback timing.
4. Stitches native stills with hard cuts only, then runs full automated video QA.
5. Displays links to `SAVE_THE_GUIDE_PART01.mp4`, `SAVE_THE_GUIDE_PART01_DELIVERABLE.zip` and `QA_REPORT.md`.

## Runtime policy

There is **no fixed runtime cap**. The actual one-take narration will determine the final runtime on Kaggle.

No narration, measured timing file or stitched video has been produced in the repository yet.
