# Save the Guide — Part 1 Status

## Current stage

**The fresh 146/146 whole-image audit is complete. 142 frames passed unchanged; four audit corrections passed production reinspection and now await user review. No image lacks an audit result and no production correction remains pending.**

## Production counter

| Counter | Frames |
|---|---:|
| Planned final narrative frames | **146** |
| Passed audit unchanged and approved | **142** |
| Corrected frames awaiting review | **4** |
| **Total retained on disk** | **146** |
| Pending production corrections | **0** |
| **Planned frames not yet produced** | **0** |

## Full-audit corrections

The review sheet is `review/part01_full_audit_corrections.jpg`.

- `beat04m01` — low flat natural-stick training-fire platform replaces the raised wooden table.
- `beat09m09` — bivy adjustment now preserves straight together legs, tucked hands, silver-over-green coverage and both characters' identities.
- `beat09m10` — wet trousers are just removed while Mara remains fully covered with straight legs; the orange shell is separate.
- `beat12m02` — the whisper close-up is reclining rather than upright, with integrated hood, silver rim and no pillow.

The complete audit method, batch coverage and validation results are in `FULL_FRAME_AUDIT.md`; every frame's outcome and SHA-256 hash are in `FRAME_AUDIT.csv`.

## Completed

- Research, series bible, full 14-paragraph/1,009-word Part 1 script, approved locked reference pack and validated 146-moment visual plan.
- `beats.jsonl` — 14 narration beats derived from the approved script.
- All **146 current frames** freshly audited against narration and continuity; **142 passed unchanged and 4 corrected frames passed reinspection**.
- All **146 retained frames** validate at native **1376×768**, with one unique frame for every planned moment.
- All **146 narration rows** join verbatim to the 14 approved script paragraphs; `beats.jsonl` also matches those paragraphs verbatim.
- Affected Batch 04, 09 and 12 review sheets rebuilt from current frames.

## Runtime policy

There is **no fixed runtime cap**. Actual narration timing will determine the final runtime.

## Next production steps

1. Obtain user review of the four full-audit replacement frames.
2. After approval, produce one continuous `en-US-AndrewNeural` narration take at `-5%`.
3. Require complete WordBoundary moment locking, stitch native-resolution frames with hard cuts only, and perform audio/visual/timing QA.
4. Record Part 1's ending state for Part 2 continuity.

No narration, measured timing file or stitched video has been produced yet.
