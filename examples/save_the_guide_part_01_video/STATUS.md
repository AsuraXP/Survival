# Save the Guide — Part 1 Status

## Current stage

**Research, series planning, full Part 1 narration, and the complete reference pack are approved and locked. The full 146-moment visual plan is validated. Batches 1–8 are approved, including all user-requested corrections. Batch 9 first-pass QA retained four frames; six corrections and two section-completion frames remain.**

## Production counter

| Counter | Frames |
|---|---:|
| Planned final narrative frames | **146** |
| Approved opening | **10** |
| Approved training | **11** |
| Approved character/safety setup | **11** |
| Approved progress/initial crossing | **10** |
| Approved accident | **10** |
| Approved first rescue attempt | **11** |
| Approved coordinated extraction | **11** |
| Approved injury discovery | **11** |
| **Total approved** | **85** |
| Batch 9 first-pass frames awaiting user review | **4** |
| **Total retained on disk** | **89** |
| Batch 9 corrections pending | **6** |
| Batch 9 completion frames not yet generated | **2** |
| **Final frames remaining** | **57** |

Batch numbering tracks planned production batches; correction and section-completion generations are additional rounds and do not increase the final 146-frame requirement.

## Completed

- `script.md` — complete Part 1 narration: 14 paragraphs and 1,009 words.
- `SERIES_BIBLE.md` — premise, characters, themes, equipment logic, three-part arc, setup/payoff ledger, and continuity rules.
- `RESEARCH.md` — sourced survival guidance and exact story applications.
- `references/save_the_guide/` — complete approved reference pack plus modular prompt and continuity rules.
- `visuals.csv` — **146 short narration moments** across 14 paragraphs; every paragraph is reproduced verbatim by its ordered `moment_text` values. Validation passes after the Batch 9 prompt corrections.
- `beats.jsonl` — 14 narration beats converted from the validated visual plan.
- `FRAME_REVIEW.md` — approvals, reopened frames, visual QA, corrections, counters, and standing continuity/anatomy rules.
- **Batches 1–8:** 85 frames approved.
- **Batch 9:** `m01`, `m03`, `m04`, and `m09` retained; six first-pass candidates rejected; `m11` and `m12` remain to be generated.

## Runtime policy

There is **no fixed runtime cap**. Actual narration timing will determine the final runtime after frame production.

## Next production steps

1. Obtain user review of the four retained Batch 9 frames.
2. Run an eight-frame Batch 9 completion round: regenerate `m02`, `m05`, `m06`, `m07`, `m08`, and `m10`; generate `m11` and `m12`.
3. If all eight pass, Batch 9 will contain 12/12 frames and the overall count will be **97/146 retained**, leaving **49**.
4. Continue remaining frames in controlled batches of at most ten per generation round with visual inspection, user review, and checkpoint pushes.
5. Produce one-take `en-US-AndrewNeural` narration at `-5%`, require complete WordBoundary moment locking, and stitch native-resolution frames with hard cuts only.

No narration or stitched video has been produced yet.
