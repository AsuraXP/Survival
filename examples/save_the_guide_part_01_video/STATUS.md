# Save the Guide — Part 1 Status

## Current stage

**Batches 1–10 are approved. Batch 11's ten-frame first pass retained three frames and rejected seven for stone/dirt bases, sawn logs, A-frames, orange wardrobe leakage or Mara's bare hand. The rejected structure and continuity errors are not in the retained sequence.**

## Production counter

| Counter | Frames |
|---|---:|
| Planned final narrative frames | **146** |
| **Total approved (Batches 1–10)** | **108** |
| Batch 11 first-pass awaiting review | **3** |
| **Total retained on disk** | **111** |
| Batch 11 corrections pending | **7** |
| **Final frames remaining** | **35** |

## Completed

- Research, series bible, full 14-paragraph/1,009-word Part 1 script, approved locked reference pack and validated 146-moment visual plan.
- `beats.jsonl` — 14 narration beats derived from the plan.
- **Batches 1–10:** 108 frames approved.
- **Batch 11:** `m01`, `m03`, and `m08` retained. Corrections pending for `m02`, `m04`, `m05`, `m06`, `m07`, `m09`, and `m10`.
- `PROMPT_BIBLE.md` — now explicitly prohibits stone slabs, exposed dirt, sawn-log bases and upright frames; approved `beat10m07` is the fire-base continuity anchor.
- All **111 retained frames** validated at native **1376×768**; narration text validates verbatim across all 146 moments.

## Runtime policy

There is **no fixed runtime cap**. Actual narration timing will determine the final runtime after frame production.

## Next production steps

1. Review the three retained Batch 11 frames.
2. Regenerate the seven rejected Batch 11 moments using the approved flat fire base and strict wardrobe/hand constraints.
3. If all seven pass, Batch 11 will be complete at 10/10 and the count will be **118/146 retained**, leaving **28**.
4. Continue in controlled batches of at most ten per generation round with inspection, user review and checkpoint pushes.
5. Produce one-take `en-US-AndrewNeural` narration at `-5%`, require complete WordBoundary moment locking, and stitch native-resolution frames with hard cuts only.

No narration or stitched video has been produced yet.
