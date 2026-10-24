# The Store Had Everything — Character and Rendering References

## Final identity authority

The user's final identity instruction on 2026-10-24 is binding: **Nolan has exactly three simple curved black hair strokes**, matching `character_style_user.jpg`. This choice is intended to reduce generation drift. It supersedes the earlier spiky-fringe direction.

The simplification applies only to that hair shape. Nolan's round head, black oval eyes, expressions, thin neck and limbs, approximate 3.5-head proportions, teal vest, charcoal clothing, dark trousers, light-soled shoes, blank lanyard, poses and prop state remain mandatory. Lena, lighting, backgrounds, camera geography and spatial continuity are equally binding.

## S00 — User-supplied construction and Nolan-hair source

`character_style_user.jpg` was supplied by the user on 2026-10-23. Its original upload filename was `From Klickpin.com- 1096978421763600576-pin-id-1096978421763600576.jpg`.

It guides the round head, clean dark outline, minimal black oval eyes, thin neck and limbs, simplified hands and shoes, expression through brows/mouth/posture, and Nolan's final three-stroke hair silhouette. It does not dictate wardrobe, colour palette, store, props, lighting or composition.

## S01 — Original hybrid: historical only

`examples/the_store_had_everything/style_tests/hybrid_opening_establishing.png` was selected in the first hybrid test. Its realistic background was subsequently rejected for visual cohesion, and its spiky Nolan hair was superseded by the user's final three-stroke instruction.

**Do not use S01 as an active identity or environment reference.** It remains only as a record of the direction's history.

## S02 — Unified cartoon rendering anchor

After the background-cohesion concern, the user selected option 2 in the unified-cartoon test:

`examples/the_store_had_everything/style_tests/unified_cartoon_opening.png`

This 769×1363 portrait image is a rendering-style reference only, not a final frame. It guides shared outlines, cel shading and vivid colour relationships. Final story frames remain horizontal 16:9.

## Current correction state

- Active `nolan_identity.png` is the new round-head, oval-eye, thin-limb C01 with exactly three curved black hair strokes.
- The former spiky C01 is isolated at `references/the_store_had_everything/rejected/nolan_spiky_identity.png`.
- Active Nolan-containing frames P001, P005, P007, P010 and P012 have been regenerated and reviewed against the final identity.
- Their superseded versions and failed correction attempts are isolated under `opening_pilot/rejected/`; none may guide production.
- The old unified cohesion proofs are historical style tests, not active combined masters. The active opening master is `opening_pilot/frames/P001.png`.

## Unified target

- **Characters:** simple round-head/oval-eye construction, final C01/C02 hair silhouettes and wardrobe, thin limbs, expressive brows/mouth/posture and anatomically readable poses.
- **Environment and props:** vivid hand-drawn 2D cel-cartoon rendering with related dark outlines, simplified geometric props, large clean colour shapes and broad stylized light/shadow bands.
- **Integration:** characters and environment share line, shading and lighting logic. Neither realistic backgrounds nor flat sticker-like characters are acceptable.
- **Continuity:** no style anchor overrides the current identity, scene state, last accepted frame or `CONTINUITY_PROTOCOL.md`.

Only accepted frames may become continuation references. Every later frame requires individual and adjacent-sequence review before use.
