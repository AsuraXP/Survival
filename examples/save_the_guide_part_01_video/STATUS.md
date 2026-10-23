# Save the Guide — Part 1 Status

## Current stage

**Research, series planning, full Part 1 narration, and the complete reference pack are approved and locked. The full 146-moment visual plan is validated. Batches 1–4 are approved. Batch 5 is now complete: all ten accident frames passed first-pass visual inspection and await user review.**

## Production counter

| Counter | Frames |
|---|---:|
| Planned final narrative frames | **146** |
| Approved opening | **10** |
| Approved training | **11** |
| Approved character/safety setup | **11** |
| Approved progress/initial crossing | **10** |
| **Total approved** | **42** |
| Complete Batch 5 awaiting user approval | **10** |
| **Total retained on disk** | **52** |
| Rejected candidates pending correction | **0** |
| **Final frames remaining** | **94** |

Batch numbering tracks planned production batches; correction and section-completion generations are additional rounds and do not increase the final 146-frame requirement.

## Completed

- `script.md` — complete Part 1 narration: 14 paragraphs and 1,009 words.
- `SERIES_BIBLE.md` — premise, characters, themes, equipment logic, three-part arc, setup/payoff ledger, and continuity rules.
- `RESEARCH.md` — sourced survival guidance and exact story applications.
- `references/save_the_guide/` — complete approved reference pack plus modular prompt and continuity rules.
- `visuals.csv` — **146 short narration moments** across 14 paragraphs; every paragraph is reproduced verbatim by its ordered `moment_text` values.
- `beats.jsonl` — 14 narration beats converted from the validated visual plan.
- `FRAME_REVIEW.md` — section approvals, batch-level visual QA, correction history, production counter, and standing continuity rules.
- **Batches 1–4:** 42 frames approved.
- **Batch 5:** 10/10 generated, visually inspected, and retained for review.

## Runtime policy

There is **no fixed runtime cap**. Actual narration timing will determine the final runtime after frame production.

## Next production steps

1. Obtain user approval for the complete Batch 5 accident section.
2. Generate **Batch 6**, first pass `beat06m01`–`beat06m10` followed by `beat06m11`: cold shock, failed self-rescue, Evan's unsafe step, Mara's rope command, and the first throw falling short.
3. Continue remaining frames in controlled batches of at most ten per generation round with visual inspection, user review, and checkpoint pushes.
4. Produce one-take `en-US-AndrewNeural` narration at `-5%`, require complete WordBoundary moment locking, and stitch native-resolution frames with hard cuts only.

No narration or stitched video has been produced yet.
