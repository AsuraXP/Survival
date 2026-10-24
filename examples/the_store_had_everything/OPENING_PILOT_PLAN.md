# The Store Had Everything — Reusable Opening Pilot Plan

Status: active after the user's approval of the arc and Part 1 script on 2026-10-23. Style selection precedes recurring references and frame generation.

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

Simple Characters, Vivid World: characters follow the user-supplied round-head, minimal oval-eye, thin-limb construction, with expression carried by brows, eye shape, mouth, head tilt and posture. Environments and props use saturated teal/amber/blue accents, rich 2D detail, strong readable lighting, and non-graphic infected silhouettes. No realistic character faces, blank expressions, washed-out palette, captions, logos, borders, or watermarks.

## Production gates

1. User selects the opening style candidate. **Complete: simple-character/rich-world hybrid selected.**
2. Lock character, prop, palette, and location references. **In progress: opening pack presented for approval; the selected opening image is a style anchor, not an interchangeable background.**
3. Generate the full master narration in Kaggle and verify the actual opening duration and word timings.
4. Produce the opening frame batch and review it in sequence under `CONTINUITY_PROTOCOL.md`.
5. Assemble and present the 30–45 second pilot.
6. Only after pilot approval, continue the remaining Part 1 frames using the same master audio and approved references.
