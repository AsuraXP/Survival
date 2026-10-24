# The Store Had Everything — Prompt Bible

Status: active opening-production prompt rules, aligned to the user's final three-hair-stroke Nolan identity on 2026-10-24.

## Reference hierarchy

Use references together, not as substitutes for one another:

1. **Scene/location master:** controls camera, architecture, landmark placement, lighting and existing crowd state.
2. **Current Nolan and/or Lena identity reference:** controls character construction, exact hair silhouette, wardrobe and hand/prop state.
3. **Previous accepted frame:** controls the immediate physical action when the shot is a direct continuation.
4. **User construction source:** controls the round-head/oval-eye/thin-limb construction and Nolan's exact three-stroke hair; it does not control wardrobe, composition or background.
5. **S02 unified cartoon:** anchors shared outlines, cel shading and vivid colour relationships; its portrait crop is not a video frame.

The original S01 hybrid and old cohesion proofs are historical only: their spiky Nolan hair is superseded and their backgrounds are not active. Never prompt a same-scene continuation from text alone. Never use a rejected frame or an incompatible scene state as a reference.

## Canonical character prompts

### Nolan — C01

Nolan Brooks, 26, lean, approximately 3.5 heads tall in the selected simple cartoon construction. Oversized, nearly perfectly circular pale head with a clean dark hand-drawn outline; solid-black vertical oval eyes; simple curved brows and mouth; no realistic nose detail; thin neck and limbs; simplified hands and shoes. **Exactly three and only three separate curved black hair strokes rise from the otherwise bald top of his head, matching `nolan_identity.png` and `character_style_user.jpg`.** Keep all three visible and readable in front, three-quarter, profile and wider views; a completely bald head with zero strokes is an identity failure. No brown hair mass, fringe, spikes, side hair, fourth stroke or extra decorative marks.

Vivid teal fleece vest over a charcoal dark long-sleeve shirt, dark work trousers, dark sneakers with pale/light soles, plain black lanyard with blank light-grey badge. Worried determination expressed through brow angle, mouth, head tilt, posture and hands. No backpack or radio in the opening.

The three-stroke simplification never permits a changed head shape, realistic facial detail, altered eyes, thicker anatomy, wardrobe changes, missing badge, changed pose or ignored scene continuity.

### Lena — C02

Lena Ortiz, 34, ordinary capable build, approximately 3.5 heads tall in the same simple cartoon construction. Oversized round pale head, clean dark outline, solid-black vertical oval eyes, simple curved brows and mouth, no realistic nose detail, thin neck and limbs. Smooth black hair tied back with one narrow braid over her anatomical right shoulder when visible. Warm amber delivery jacket over dark burgundy shirt, navy cargo trousers, dark work shoes. Van keys canonically held in her anatomical right hand during the opening; right hand means the viewer-left hand in a straight-on front view. Worried focus through brow angle, mouth and body posture. No backpack or radio in the opening paragraph.

## Canonical world prompt

Unified vivid hand-drawn 2D cel-cartoon environment, related dark outlines around architecture and props, simplified geometric outdoor equipment, large clean colour shapes, two-or-three-tone cel shading, restrained stylized shadows, saturated teal, amber, orange and electric-blue accents, deep-blue night beyond the storefront, warm amber practical lights, cyan security-office monitor glow, broad graphic floor-light bands, recognizable props and atmospheric depth without realistic micro-texture. Characters remain simple while receiving the same cel shading, contact shadows and lighting logic so they occupy the same world naturally.

### Opening palette anchors

- Nolan teal: approximately `#147D85`; charcoal clothing `#292C30`.
- Lena amber: approximately `#C88924`; burgundy `#5C1F2A`; navy `#202B43`.
- Storefront night: deep cobalt blue; office monitors: cyan.
- Tent: vivid orange; coolers: saturated medium blue; kayaks: clear green.

These are visual targets, not permission to recolour the accepted identity references arbitrarily.

## Required story-frame prompt order

1. Narration moment and emotional purpose.
2. `scene_id`, `setup_id`, exact master and previous accepted frame.
3. Fixed character positions, route direction, head/body attention, props and hand state.
4. Fixed landmark, infected, shutter, equipment and lighting state.
5. The one intended camera/expression/action change.
6. Relevant canonical character and world descriptions, including Nolan's round head and exactly three visible hair strokes.
7. Preservation constraints and negative constraints.

## Global negative constraints

No realistic protagonist faces, detailed irises, detailed noses, complex facial anatomy, comic-book muscles or changed head/body proportions. No missing, extra or replaced Nolan hair strokes; no brown/spiky/fringed hair; no oval/pointed head; no changed oval eyes, wardrobe, badge or proportions. No extra fingers or props, swapped key hand, missing/switched braid, backpacks or radio before their story acquisition. No moved shelves, tents, coolers, kayaks, stairs or office; no extra interior people or exits; no uncovered glass after the shutter closes; no gore, captions, readable brand text, logos, borders or watermarks.

Do not compensate for a weak result by redesigning the location or changing a character's physical position. Reject and correct the failed variable. If a small hair silhouette is ambiguous, inspect an enlarged review crop before acceptance.

## Opening master rule

`opening_store_background.png` is the approved unified background for setup A01. Its native dimensions are 1376×768. Opening story frames must retain that composition and native-output workflow. The 1672×941 original hybrid, 769×1363 unified portrait test and portrait identity references are references, not frames to insert indiscriminately into the video.

`examples/the_store_had_everything/opening_pilot/frames/P001.png` is the active combined opening master. The old cohesion proofs contain superseded identity states and must not be used. Active Nolan-containing opening frames are P001, P005, P007, P010 and P012; each has been regenerated and reviewed for the final identity.
