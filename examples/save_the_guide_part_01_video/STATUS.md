# Save the Guide — Part 1 Status

## Current stage

**Research, series planning, full Part 1 narration, and the complete reference pack are approved and locked. The full moment-by-moment visual plan is complete and validated. The first ten hook candidates have been visually reviewed: seven frames are retained for user batch review, and three continuity failures were rejected and queued for regeneration.**

## Completed

- `script.md` — complete Part 1 narration: 14 paragraphs and 1,009 words, with in-medias-res hook, river rescue, character setup, survival decisions, and hypothermia cliffhanger.
- `SERIES_BIBLE.md` — premise, characters, themes, equipment logic, complete three-part arc, setup/payoff ledger, and continuity rules.
- `RESEARCH.md` — ice safety, ice rescue, hypothermia, shelter, trip planning, stay/go decisions, and signalling sources with their story applications.
- `references/save_the_guide/REFERENCE_PLAN.md` — approved character, location, prop, colour, and state anchors required before narrative frame production.
- `references/save_the_guide/PROMPT_BIBLE.md` — modular style, identity, wardrobe, state, geography, prop, composition, and continuity rules for every generation.
- `references/save_the_guide/REFERENCE_MANIFEST.md` — explicit approval and lock status for every reference asset.
- `visuals.csv` — **146 short narration moments** across the 14 paragraphs. Joining each paragraph's `moment_text` values reproduces the script verbatim; average length is 6.91 whitespace-delimited words per moment.
- `beats.jsonl` — 14 narration beats converted from the validated visual plan; placeholder durations will be replaced by actual WordBoundary timings.
- `FRAME_REVIEW.md` — batch-level visual QA, retained frames, rejected candidates, and correction reasons.

## Frame production

- Planned narrative frames: **146**
- Retained after internal review and awaiting user batch review: **7**
- Rejected candidates removed and queued for regeneration: **3**
- Approved narrative frame batches: **0**
- Narration or stitched video produced: **none**

## Runtime policy

There is **no fixed runtime cap**. The story should use the length required for strong pacing and emotional payoff. Word count alone will not be used to cut good material; actual narration timing will be checked after frame production.

## Next production steps

1. Regenerate `beat01m01`, `beat01m06`, and `beat01m10` with the documented geography and state corrections.
2. Continue with `beat02m01`–`beat02m07`, inspect all ten new candidates, and checkpoint the retained set.
3. Generate remaining frames in controlled batches of at most ten with user batch review and checkpoint pushes.
4. Produce one-take `en-US-AndrewNeural` narration at `-5%`, require complete WordBoundary moment locking, and stitch native-resolution frames with hard cuts only.

Research sources and their exact story applications are documented in `RESEARCH.md`.
