# Opening Pilot — Local Validation Record

Date: 2026-10-24

## Passed in the repository workspace

- All 12 active opening frames exist at native 1376×768 and have accepted review statuses.
- The 12 narration segments reproduce approved Part 1 paragraph 1 exactly.
- `pipeline/prepare_store_pilot.py` derived 14 full-script beats, 12 opening-only word-map rows and 12 valid native-frame links.
- Every active frame's listed reference files exist; no rejected reference is listed.
- `pipeline/qa_store_pilot.py` passed a synthetic timing/media fixture with 26 checks, including a 35-second opening within a 300-second full master.
- `run_store_opening_pilot.sh` passed `bash -n`.
- `STORE_OPENING_PILOT_KAGGLE.ipynb` parsed as valid one-cell notebook JSON.
- Python production/QA modules passed bytecode compilation.

## Not claimed locally

No real narration or completed pilot video has been produced in this sandbox. Edge TTS requires Kaggle Internet access, and local FFmpeg is unavailable. The synthetic QA fixture validates program logic; it is not a substitute for the real Kaggle audio/video QA.

## Required Kaggle result

The one-cell runner must synthesize the complete 14-paragraph master with Andrew at normal `+0%`, lock all 12 opening moments to actual WordBoundary events without warnings, stitch the opening of that same take, pass the real 30–45 second/media/decode QA, and only then expose the completed pilot and reusable deliverable ZIP.
