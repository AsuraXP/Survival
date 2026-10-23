# Save the Guide — Part 1 Status

## Current stage

**Research, series planning, full Part 1 narration, and the complete reference pack are approved and locked. The full 146-moment visual plan is validated. Batches 1–3 are approved. Batch 4's first pass is complete: nine frames are retained, and one missing-glove error is queued for correction.**

## Production counter

| Counter | Frames |
|---|---:|
| Planned final narrative frames | **146** |
| Approved opening | **10** |
| Approved training | **11** |
| Approved character/safety setup | **11** |
| **Total approved** | **32** |
| Batch 4 retained, awaiting user review | **9** |
| **Total retained on disk** | **41** |
| Rejected Batch 4 candidates pending correction | **1** |
| **Final frames still needed** | **105** |

Batch numbering tracks planned production batches; correction and section-completion generations are additional rounds and do not increase the final 146-frame requirement.

## Completed

- `script.md` — complete Part 1 narration: 14 paragraphs and 1,009 words.
- `SERIES_BIBLE.md` — premise, characters, themes, equipment logic, three-part arc, setup/payoff ledger, and continuity rules.
- `RESEARCH.md` — sourced survival guidance and exact story applications.
- `references/save_the_guide/` — complete approved reference pack plus modular prompt and continuity rules.
- `visuals.csv` — **146 short narration moments** across 14 paragraphs; every paragraph is reproduced verbatim by its ordered `moment_text` values.
- `beats.jsonl` — 14 narration beats converted from the validated visual plan.
- `FRAME_REVIEW.md` — section approvals, batch-level visual QA, correction history, production counter, and standing continuity rules.
- **Batches 1–3:** 32 frames approved.

## Runtime policy

There is **no fixed runtime cap**. Actual narration timing will determine the final runtime after frame production.

## Next production steps

1. Regenerate `beat04m06` with Mara's dark gloves intact to complete Batch 4.
2. Review the completed batch at **42/146 retained**, leaving **104 final frames**.
3. Generate **Batch 5**, the concealed weak ice, accident, and lost-pack sequence.
4. Continue remaining frames in controlled batches of at most ten with visual inspection, user review, and checkpoint pushes.
5. Produce one-take `en-US-AndrewNeural` narration at `-5%`, require complete WordBoundary moment locking, and stitch native-resolution frames with hard cuts only.

No narration or stitched video has been produced yet.
