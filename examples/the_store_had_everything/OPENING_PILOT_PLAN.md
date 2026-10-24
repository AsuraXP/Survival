# The Store Had Everything — Reusable Opening Pilot Plan

Status: **approved by the user and locked on 2026-10-24.** The corrected Kaggle opening is the reusable beginning of Part 1. Continuation has begun from paragraph 2 with P013 onward; see `opening_pilot/APPROVAL.md` and `part01/CONTINUATION_PLAN.md`.

## Reuse guarantee

The opening pilot is being produced as the actual beginning of Part 1, not as a disposable proof with different assets.

- Generate the **complete approved Part 1 master narration once** using `en-US-AndrewNeural` at normal `0%` speed.
- Retain its actual word-level WordBoundary timings as the master timing source.
- Build the pilot from the beginning of that same master audio, ending after the approved 94-word opening paragraph.
- Generate pilot frames at final native resolution with the selected recurring references and the same hard-cut pipeline intended for the full episode.
- If the pilot is approved, retain its audio, frames, timing, and edit unchanged as the opening segment of the finished Part 1. Continue the remaining story from the next word boundary.
- If the pilot needs changes, preserve usable assets and revise only the affected style references, shots, timing, or edit. A rejected style candidate is not silently reused in the final.

This avoids the mismatch that could result from narrating a short demo separately and then recording a different full take later.

## Opening narration

The store had enough food for months. Enough water. Enough batteries to light every aisle. Unfortunately, it also had a public-address system that would not shut up. Every thirty seconds, a cheerful voice announced another sale. Every thirty seconds, more infected pressed against the front glass. From behind checkout three, Nolan could see the security office above the rear wall. The announcement controls were in there. So was the switch for the metal shutter. All he and Lena had to do was cross the store before the next announcement brought the whole crowd through.

## Opening continuity setup

### Fixed geography

- Front glass and blue night are on the storefront side; the infected remain outside the glass in this opening.
- Checkout three is the characters' starting cover.
- Camping landmarks are deeper inside: orange tent display, blue cooler stack, and green kayak wall.
- The security office is elevated above the rear wall, with a readable observation window and monitor glow.
- The public-address speaker is overhead; the metal shutter has not yet descended.

### Initial character state

- Nolan begins behind checkout three with his left shoulder toward the storefront, facing toward the rear office. He has his store key/lanyard and box cutter. He does not have a backpack.
- Lena begins one step behind and to Nolan's right. She has her van keys in her anatomical right hand, with her simple braid over her right shoulder when visible. She does **not** have the hand-crank radio yet; it is acquired at the camping display in the next paragraph.
- Their movement toward the office occurs only when the narration describes the objective and crossing. A camera change alone cannot move them.

### Lighting and art

Unified Vivid Cel Cartoon: retain the final C01/C02 identities, including Nolan's round head, black oval eyes, thin anatomy, fixed wardrobe and exactly three simple curved black hair strokes, plus Lena's right-side braid and key hand. Characters and environments share dark outlines, simplified geometric props, two/three-tone cel shading and broad amber/blue light bands. No realistic character faces or backgrounds, missing/extra/replaced Nolan hair strokes, blank expressions, washed-out palette, captions, logos, borders or watermarks.

## Production gates

1. Select the character and rendering direction. **Complete: final C01/C02 identities locked, including the user's three-hair-stroke Nolan correction; unified cel-cartoon rendering selected.**
2. Lock character, prop, palette, and location references. **Complete on 2026-10-24: final three-stroke C01/C02/L01 pack locked; corrected P001 is the active opening master. Earlier realistic, flat-haired and spiky-haired proofs are not active references.**
3. Generate the full master narration in Kaggle and verify the actual opening duration and word timings. **Runner/notebook ready; Kaggle execution pending.**
4. Produce the opening frame batches and review them in sequence under `CONTINUITY_PROTOCOL.md`. **Complete: all 12 frames accepted through assistant per-image/sequence QA.**
5. Assemble and present the 30–45 second pilot. **Complete: corrected Kaggle pilot assembled and approved by the user; P001–P012 and its measured opening edit are locked.**
6. Continue the remaining Part 1 frames using the same master audio and approved references. **Active: Batch 3, P013–P018, starts at paragraph 2. Do not enable `FORCE_TTS`.**
