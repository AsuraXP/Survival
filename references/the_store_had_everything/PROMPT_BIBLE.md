# The Store Had Everything — Prompt Bible

Status: proposed for reference-pack approval. This governs prompting after the user selected the simple-character/rich-world hybrid.

## Reference hierarchy

Use references together, not as substitutes for one another:

1. **Scene/location master:** controls camera, architecture, landmark placement, lighting and existing crowd state.
2. **Nolan and/or Lena identity reference:** controls character construction, hair and wardrobe.
3. **Previous approved frame:** controls the immediate physical action when the shot is a direct continuation.
4. **User style source:** controls simple character construction only; it does not control wardrobe, composition or background.
5. **Selected hybrid test:** controls the relationship between simple characters and the richer world; it is not the canonical opening background.

Never prompt a same-scene continuation from text alone. Never mix the selected test's background with the clean opening background plate as though they were identical.

## Canonical character prompts

### Nolan — C01

Nolan Brooks, 26, lean, approximately 3.5 heads tall in the supplied simple cartoon construction. Oversized round pale head, clean dark hand-drawn outline, sparse dark-brown loose-fringe hair, solid-black vertical oval eyes, simple curved brows and mouth, no nose detail, thin neck and limbs, simplified hands and shoes. Vivid teal fleece vest over a charcoal dark long-sleeve shirt, dark work trousers, dark sneakers with pale soles, plain black lanyard with blank light-grey badge. Worried determination expressed through brow angle, mouth, head tilt and posture. No backpack or radio in the opening.

### Lena — C02

Lena Ortiz, 34, ordinary capable build, approximately 3.5 heads tall in the same simple cartoon construction. Oversized round pale head, clean dark outline, solid-black vertical oval eyes, simple curved brows and mouth, no nose detail, thin neck and limbs. Smooth black hair tied back with one narrow braid over her anatomical right shoulder when visible. Warm amber delivery jacket over dark burgundy shirt, navy cargo trousers, dark work shoes. Van keys canonically held in her anatomical right hand during the opening; right hand means the viewer-left hand in a straight-on front view. Worried focus through brow angle, mouth and body posture. No backpack or radio in the opening paragraph.

## Canonical world prompt

Rich vivid detailed 2D cinematic environment, graphic-novel depth, confident environmental line work, controlled shading, saturated teal, amber, orange and electric-blue accents, deep-blue night beyond the storefront, warm amber practical lights, cyan security-office monitor glow, reflective but readable floor, atmospheric depth, recognizable outdoor equipment. Characters remain simple while receiving restrained cel shading, contact shadows and rim light so they occupy the same world naturally.

### Opening palette anchors

- Nolan teal: approximately `#147D85`; charcoal clothing `#292C30`.
- Lena amber: approximately `#C88924`; burgundy `#5C1F2A`; navy `#202B43`.
- Storefront night: deep cobalt blue; office monitors: cyan.
- Tent: vivid orange; coolers: saturated medium blue; kayaks: clear green.

These are visual targets, not permission to recolour the approved identity references arbitrarily.

## Required story-frame prompt order

1. Narration moment and emotional purpose.
2. `scene_id`, `setup_id`, exact master and previous approved frame.
3. Fixed character positions, route direction, head/body attention, props and hand state.
4. Fixed landmark, infected, shutter, equipment and lighting state.
5. The one intended camera/expression/action change.
6. Relevant canonical character and world descriptions.
7. Preservation constraints and negative constraints.

## Global negative constraints

No realistic protagonist faces, detailed irises, detailed noses, complex facial anatomy, comic-book muscles or changed head/body proportions. No extra fingers or props, swapped key hand, missing braid, changed hair or wardrobe, backpacks or radio before their story acquisition. No moved shelves, tents, coolers, kayaks, stairs or office; no extra interior people or exits; no uncovered glass after the shutter closes; no gore, captions, readable brand text, logos, borders or watermarks.

Do not compensate for a weak result by redesigning the location or changing a character's physical position. Reject and correct the failed variable.

## Opening master rule

`opening_store_background.png` is the only canonical background for setup A01 once approved. Its native dimensions are 1376×768. Opening story frames must retain that composition and native-output workflow; the 1672×941 selected style test and the portrait identity references are references, not frames to insert indiscriminately into the video.
