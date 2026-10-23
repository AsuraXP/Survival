# Save the Guide — Part 1 Status

## Current stage

**Research, series planning, full Part 1 narration, and the complete reference pack are approved and locked. The full 146-moment visual plan is validated. Batches 1–8 and four Batch 9 frames are approved. Batch 9 now has ten retained frames; six new frames await review and only `m07` and `m11` still require correction.**

## Production counter

| Counter | Frames |
|---|---:|
| Planned final narrative frames | **146** |
| Approved Batches 1–8 | **85** |
| Approved Batch 9 first-pass subset | **4** |
| **Total approved** | **89** |
| New Batch 9 frames awaiting user review | **6** |
| **Total retained on disk** | **95** |
| Batch 9 corrections pending | **2** |
| **Final frames remaining** | **51** |

Batch numbering tracks planned production batches; correction and section-completion generations are additional rounds and do not increase the final 146-frame requirement.

## Completed

- `script.md` — complete Part 1 narration: 14 paragraphs and 1,009 words.
- `SERIES_BIBLE.md` — premise, characters, themes, equipment logic, three-part arc, setup/payoff ledger and continuity rules.
- `RESEARCH.md` — sourced survival guidance and exact story applications.
- `references/save_the_guide/` — complete approved reference pack plus modular prompt and continuity rules.
- `visuals.csv` — **146 short narration moments** across 14 paragraphs; every paragraph is reproduced verbatim by its ordered `moment_text` values. Validation passes after the latest prompt corrections.
- `beats.jsonl` — 14 narration beats converted from the validated visual plan.
- `FRAME_REVIEW.md` — approvals, reopened frames, visual QA, corrections, counters and standing continuity/anatomy rules.
- **Batches 1–8:** 85 frames approved.
- **Batch 9:** `m01`, `m03`, `m04`, and `m09` approved; corrected `m02`, `m05`, `m06`, `m08`, `m10`, and new `m12` retained for review. Only `m07` and `m11` remain.
- All **95 retained frames** validated at native **1376×768**.

## Runtime policy

There is **no fixed runtime cap**. Actual narration timing will determine the final runtime after frame production.

## Next production steps

1. Obtain user review of the six new Batch 9 frames in the refreshed review sheet.
2. Regenerate only `beat09m07` and `beat09m11`, enforcing two-boot anatomy, the established spruce shelter, and no unapproved structures or firewood.
3. If both pass, Batch 9 will contain 12/12 frames and the overall count will be **97/146 retained**, leaving **49**.
4. Continue remaining frames in controlled batches of at most ten per generation round with visual inspection, user review and checkpoint pushes.
5. Produce one-take `en-US-AndrewNeural` narration at `-5%`, require complete WordBoundary moment locking, and stitch native-resolution frames with hard cuts only.

No narration or stitched video has been produced yet.
