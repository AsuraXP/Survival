# Opening Pilot — Local Validation Record

Date: 2026-10-24

## Passed in the repository workspace

- Final C01 and all five active Nolan-containing frames (P001, P005, P007, P010 and P012) were regenerated and visually reviewed after the user's explicit three-hair-stroke correction.
- Every other identity detail remained in the review gate: round head, oval eyes, expressions, thin anatomy, wardrobe/badge, poses and props, plus Lena, unified lighting, backgrounds and spatial continuity.
- P010's small hair silhouette received an enlarged-crop review: exactly three strokes were confirmed separately from rear staircase lines.
- A full 12-frame sequence review passed for adjacent-shot identity, route direction, office-control layout, fixed landmarks, crowd/glass/shutter states and story-prop timing.
- All 12 active opening frames exist at native 1376×768 and have accepted review statuses.
- Superseded and failed identity candidates are isolated under `rejected/`; no active manifest row references them.
- The 12 narration segments reproduce approved Part 1 paragraph 1 exactly.
- `pipeline/prepare_store_pilot.py --project examples/the_store_had_everything` passed after the identity correction: 14 approved script paragraphs, 12 accepted native frames, verbatim opening text and valid reference paths. It derived 14 full-script beats and 12 opening-only word-map rows.
- A real-FFmpeg regression reproduced the Kaggle failure: `-shortest` plus the repeated final concat image extended a 32.500-second opening to 35.300 seconds. The corrected stitcher explicitly clone-pads, trims and timestamp-resets both streams at the measured opening boundary.
- The corrected real-media regression produced a 32.533-second video stream/container and 32.500-second audio for the 32.500-second opening. `pipeline/qa_store_pilot.py` passed all 26 checks, including full decode, using synthetic audio with the actual 12 native frames.
- `run_store_opening_pilot.sh` passed `bash -n`.
- `STORE_OPENING_PILOT_KAGGLE.ipynb` parsed as valid one-cell notebook JSON and has no stale commit pin.
- Python production/QA modules passed bytecode compilation.
- `git diff --check` passed.

## Not claimed locally

No real narration or completed story pilot has been produced in this sandbox. Edge TTS requires Kaggle Internet access. A temporary local FFmpeg binary validated the stitch correction with synthetic audio; that regression is not a substitute for the real Kaggle narration/video QA. The notebook must use a commit containing both the corrected identity/frame set and this explicit-duration stitch fix, not the earlier `a105863` state.

## Required Kaggle result

The one-cell runner must synthesize the complete 14-paragraph master with Andrew at normal `+0%`, lock all 12 opening moments to actual WordBoundary events without warnings, stitch the opening of that same take, pass the real 30–45 second/media/decode QA, and only then expose the completed pilot and reusable deliverable ZIP.
