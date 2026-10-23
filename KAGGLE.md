# Save the Guide — Part 1: One-Cell Kaggle Notebook

Use **`SAVE_THE_GUIDE_PART01_KAGGLE.ipynb`**.

1. Import the notebook into Kaggle and enable **Internet** in the notebook settings.
2. Run its single code cell.

The cell clones `AsuraXP/Survival` on `arena/35064a39-survival`, runs `run_save_the_guide_part01.sh`, and then displays download links for:

- `SAVE_THE_GUIDE_PART01.mp4` — completed video.
- `SAVE_THE_GUIDE_PART01_DELIVERABLE.zip` — video, one-take narration, measured timings, script/plan, QA and Part 2 continuity handoff.
- `QA_REPORT.md` — automated production validation.

The runner stops on any error and will not stitch with missing frames, unmatched narration moments or fallback timing. It requires the exact **146/146 WordBoundary `[OK]`** result before producing the MP4. Narration is one continuous `en-US-AndrewNeural` take at `-5%`; assembly uses native 1376×768 stills and hard cuts only.
