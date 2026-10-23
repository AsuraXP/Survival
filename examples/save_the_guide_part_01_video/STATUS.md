# Save the Guide — Part 1 Status

## Current stage

**The shelter audit is complete. Rejected intermediate drafts did contain handmade wooden frames, but the retained Batch 9 sequence contains no tent or A-frame. The silver layer is the intentional emergency bivy. A real background-debris mismatch in `beat09m09` was corrected and that frame awaits re-review. Batch 10 has begun: four first-pass frames retained, five corrections and two completion frames pending.**

## Production counter

| Counter | Frames |
|---|---:|
| Planned final narrative frames | **146** |
| Approved Batches 1–8 | **85** |
| Approved Batch 9 subset (`m01`, `m03`, `m04`) | **3** |
| **Total approved** | **88** |
| Batch 9 awaiting review/re-review | **9** |
| Batch 10 first-pass awaiting review | **4** |
| **Total retained on disk** | **101** |
| Batch 10 corrections pending | **5** |
| Batch 10 completion frames not yet generated | **2** |
| **Final frames remaining** | **45** |

The approved count moved from 89 to 88 because the user's continuity audit reopened `beat09m09`; its cleaned replacement has not yet been user-reviewed.

## Completed

- Research, series bible, full 14-paragraph/1,009-word Part 1 script, approved locked reference pack and validated 146-moment visual plan.
- `beats.jsonl` — 14 narration beats derived from the plan.
- **Batches 1–8:** 85 frames approved.
- **Batch 9:** complete at **12/12 retained frames**; three approved and nine awaiting review/re-review. No retained tent or handmade sleeping-shelter frame.
- **Batch 10:** `m02`, `m04`, `m07`, and `m08` retained. Corrections pending for `m01`, `m03`, `m05`, `m06`, and `m09`; `m10` and `m11` not yet generated.
- `PROMPT_BIBLE.md` updated to prohibit shelter-frame drift, pre-fire debris popping, C04 bare-hand leakage and non-flat fire construction.
- All **101 retained frames** validated at native **1376×768**; narration text still validates verbatim across all 146 moments.

## Runtime policy

There is **no fixed runtime cap**. Actual narration timing will determine the final runtime after frame production.

## Next production steps

1. Review the cleaned Batch 9 sheet and four retained Batch 10 frames.
2. Run a seven-frame Batch 10 completion round: correct `m01`, `m03`, `m05`, `m06`, and `m09`; generate `m10` and `m11`.
3. If all seven pass, Batch 10 will be complete at 11/11 and the count will be **108/146 retained**, leaving **38**.
4. Continue in controlled batches of at most ten per generation round with inspection, user review and checkpoint pushes.
5. Produce one-take `en-US-AndrewNeural` narration at `-5%`, require complete WordBoundary moment locking, and stitch native-resolution frames with hard cuts only.

No narration or stitched video has been produced yet.
