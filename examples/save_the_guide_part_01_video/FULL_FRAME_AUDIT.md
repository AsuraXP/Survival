# Save the Guide — Part 1 Full Frame Audit

Audit date: **2026-10-23**

Scope: **all 146 current narrative frames**, not historical candidates or rejected files.

## Result

- **142 frames passed the fresh whole-image audit unchanged.**
- **4 frames were reopened, corrected and passed native whole-image reinspection.**
- **146/146 current frames now have a production-audit result.**
- The four replacements await user review; no production correction remains pending.

The per-frame outcome, approval state, native dimensions and SHA-256 hash for every image are recorded in `FRAME_AUDIT.csv`. The four corrected frames are collected in `review/part01_full_audit_corrections.jpg`.

## Method and coverage

Fresh review sheets were built from the current files on disk for all 14 batches. Every frame was checked against its actual narration moment and the locked prompt bible. Uncertain details were opened at native resolution rather than accepted from thumbnails. Each replacement was then inspected as a complete image for new defects.

A before/after SHA-256 comparison confirmed that only the four intended image files changed during correction; the other 142 files remained byte-for-byte unchanged.

| Batch | Frames | Passed unchanged | Corrected and passed |
|---|---:|---:|---:|
| 01 | 10 | 10 | 0 |
| 02 | 11 | 11 | 0 |
| 03 | 11 | 11 | 0 |
| 04 | 10 | 9 | 1 |
| 05 | 11 | 11 | 0 |
| 06 | 11 | 11 | 0 |
| 07 | 11 | 11 | 0 |
| 08 | 11 | 11 | 0 |
| 09 | 12 | 10 | 2 |
| 10 | 11 | 11 | 0 |
| 11 | 10 | 10 | 0 |
| 12 | 9 | 8 | 1 |
| 13 | 9 | 9 | 0 |
| 14 | 10 | 10 | 0 |
| **Total** | **146** | **142** | **4** |

## Corrected frames

- **`beat04m01` — training fire.** Removed the raised braced wooden table. The small controlled flame now sits on a low flat natural-stick platform above continuous snow with visible gaps. Evan, Mara and the dry training setting remain intact.
- **`beat09m09` — bivy wind barrier.** Removed ambiguous raised-knee coverage. Evan now adjusts the silver bivy while Mara remains fully covered on the blue pad, with green bag beneath the silver exterior, hands inside, both legs together and fully extended, right knee straight, and no pillow.
- **`beat09m10` — wet trousers removed.** Rebuilt the action so Evan holds the just-removed wet charcoal trousers with his full connected body visible. Mara remains fully covered with straight together legs; no base-layer exposure, duplicate trousers or nudity. The wet orange shell lies separately.
- **`beat12m02` — “You did it.”** Replaced the upright close-up with a reclining whisper that matches the adjacent shelter shots. Mara has a faint proud expression, one auburn braid, an integrated green hood, a thin silver rim and no pillow.

Two rejected setup retries were not installed: one changed Evan's hair/identity and the other exposed base-layer legs and cropped Evan to arms. Only the final inspected replacements are retained.

## Checks applied

- Moment-specific action and emotional read against the verbatim narration row.
- Mara/Evan identity, hairstyle, wardrobe, gloves and current wet/dry state.
- Evan on the snowy bank during the rescue; red rope bag visibly attached in pre-throw medium/wide views.
- Mara's navy pack lost beneath the ice and never returned; Evan's mustard pack and rope ownership preserved.
- Right-knee limitation, straight together legs in full-body shelter views, tucked hands at rest, and no unintended exposed hands.
- Blue pad → green sleeping bag → silver bivy outside and over the bag; integrated hood and no pillow or silver head-bunch.
- Low controlled fires on the established natural-stick platform; no raised table, stone, dirt, sawn-log base or fire against bedding.
- Intentional training shelter distinguished from unintended shelter structures at the accident/survival site.
- Phone, lodge rotary telephone, weather/lighting, geography and final roadless/vehicle-free isolation.
- Native **1376×768**, full-bleed image, no captions, readable text or border.

## Final validation

- **146/146** planned frame filenames present and unique.
- **146/146** current images validate at native **1376×768**.
- **146/146** narration rows still join verbatim to the 14 approved script paragraphs.
- `beats.jsonl` remains unchanged and matches the approved paragraphs.
- **146/146** frames have a row and hash in `FRAME_AUDIT.csv`.

## Approval gate

The user's continuation approved the preceding 146-frame set before this audit. The four audited replacements are new visual material, so the current approval state is **142 approved + 4 awaiting review**. After those four are approved, one-take narration, WordBoundary timing, hard-cut stitching and QA can begin.

No narration, measured timing file or stitched video has been produced yet.
