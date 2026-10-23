# Save the Guide — Part 1 Status

## Current stage

**Research, series planning, full Part 1 narration, and the complete reference pack are approved and locked. The full 146-moment visual plan is validated. Batches 1–5 are approved. Batch 6 first-pass QA retained seven frames; three corrections and one section-completion frame remain.**

## Production counter

| Counter | Frames |
|---|---:|
| Planned final narrative frames | **146** |
| Approved opening | **10** |
| Approved training | **11** |
| Approved character/safety setup | **11** |
| Approved progress/initial crossing | **10** |
| Approved accident | **10** |
| **Total approved** | **52** |
| Batch 6 first-pass frames awaiting user review | **7** |
| **Total retained on disk** | **59** |
| Batch 6 corrections pending | **3** |
| Batch 6 completion frames not yet generated | **1** |
| **Final frames remaining** | **87** |

Batch numbering tracks planned production batches; correction and section-completion generations are additional rounds and do not increase the final 146-frame requirement.

## Completed

- `script.md` — complete Part 1 narration: 14 paragraphs and 1,009 words.
- `SERIES_BIBLE.md` — premise, characters, themes, equipment logic, three-part arc, setup/payoff ledger, and continuity rules.
- `RESEARCH.md` — sourced survival guidance and exact story applications.
- `references/save_the_guide/` — complete approved reference pack plus modular prompt and continuity rules.
- `visuals.csv` — **146 short narration moments** across 14 paragraphs; every paragraph is reproduced verbatim by its ordered `moment_text` values. Validation passes after the Batch 6 prompt corrections.
- `beats.jsonl` — 14 narration beats converted from the validated visual plan.
- `FRAME_REVIEW.md` — approvals, visual QA, corrections, counters, and standing continuity rules.
- **Batches 1–5:** 52 frames approved.
- **Batch 6:** seven first-pass frames retained; `m04`, `m06`, and `m10` require correction, and `m11` remains to be generated.

## Runtime policy

There is **no fixed runtime cap**. Actual narration timing will determine the final runtime after frame production.

## Next production steps

1. Obtain user review of the seven retained Batch 6 frames.
2. Run a four-frame Batch 6 completion round: regenerate `m04`, `m06`, and `m10`, then create `m11`.
3. If all four pass, Batch 6 will contain 11/11 frames and the overall count will be **63/146 retained**, leaving **83**.
4. Continue remaining frames in controlled batches of at most ten per generation round with visual inspection, user review, and checkpoint pushes.
5. Produce one-take `en-US-AndrewNeural` narration at `-5%`, require complete WordBoundary moment locking, and stitch native-resolution frames with hard cuts only.

No narration or stitched video has been produced yet.
