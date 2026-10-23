# Save the Guide — Part 1 Frame Review

Frames were retained only after visual inspection. User approval was explicit through review/continue approval. Rejected candidates never counted toward the 146 final frames, and user-flagged or audit-flagged frames were reopened even after prior approval.

## Visual production: APPROVED AND LOCKED 146/146

Every current image was freshly checked against its narration moment and the locked continuity rules. **142 frames passed the full audit unchanged; 4 were corrected and passed whole-image reinspection. The user has now approved those final four corrections as well.**

- Approved frames: **146/146**
- Frames awaiting review: **0**
- Pending production corrections: **0**
- Planned frames not yet produced: **0**

Full coverage and per-frame hashes are in `FULL_FRAME_AUDIT.md` and `FRAME_AUDIT.csv`; every audit row is marked approved.

The four final audit corrections were:

- `beat04m01` — low flat natural-stick training-fire platform.
- `beat09m09` — bivy adjustment with locked identity, straight legs and silver-over-green coverage.
- `beat09m10` — wet trousers removed while Mara remains fully covered.
- `beat12m02` — reclining whisper consistent with adjacent shelter shots.

The blond-Evan/twin-tail-looking setup retry was discarded and never installed. The retained `beat09m09` is the later dark-brown-haired, single-auburn-braid version.

## Standing continuity and QA rules

- Evan's hands are pale and ungloved; his jacket, sleeves and cuffs remain muted teal, trousers grey.
- Mara has one auburn braid and her face remains visible in shelter shots unless the script deliberately changes coverage.
- At rest and during every hand check or stillness shot, all Mara's hands and gloves remain tucked inside. Only explicit reaching/pointing actions may show exactly one dark-gloved hand.
- Full-body Mara: both legs together and fully extended along the blue pad, right knee straight, one continuous silhouette; no raised knee, curled leg or separate leg sections.
- Silver bivy remains outside and over the green sleeping bag. No pillow or pillow-shaped bunch beneath/behind the head.
- Open spruce cover only: no tent, lean-to, wooden A-frame, poles, log surround or handmade sleeping shelter. The earlier crooked training shelter is intentional only where the script names it.
- Fire remains outside on the established low natural-stick platform over snow, never on a raised table or against bedding. No stone slab, dirt base, sawn-log raft or roaring campfire.
- The lodge telephone remains the same black rotary design across exterior, on-hook and off-hook shots; no people or readable route-sheet text.
- Every final frame is native 1376×768, full-bleed, with no captions, border or polished-panel treatment.

## Next stage

Use the one-cell `SAVE_THE_GUIDE_PART01_KAGGLE.ipynb` notebook to generate one-take `en-US-AndrewNeural` narration at `-5%`, require all 146 WordBoundary locks, stitch with hard cuts and run video QA. No narration, measured timing file or stitched video exists in the repository yet.
