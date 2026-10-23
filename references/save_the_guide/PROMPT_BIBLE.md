# Save the Guide — Master Prompt Bible

This is the reusable prompt system for all reference assets and narrative frames. It is deliberately modular: one giant prompt containing every character, location, prop, and story event would create leakage and inconsistency.

## 1. Reference hierarchy

Every generation combines only the necessary layers:

1. **Global art style** — always used.
2. **Character identity** — only people in the scene.
3. **Wardrobe and physical state** — their condition at this exact story point.
4. **Location identity** — only the current place and lighting state.
5. **Prop identity** — only story-relevant objects present.
6. **Moment action and composition** — one clear event per frame.
7. **Negative constraints** — always applied.

Reference images and text blocks work together. A text prompt must never contradict an approved reference image.

## 2. Global art-style block

Use this meaning at the start of every visual prompt:

> Follow reference EXACT art style: loose imperfect black hand-drawn outlines, solid flat muted colour fills, pale icy-cyan offset shading, simple naive 2D anatomy, clear silhouettes, and an uncluttered composition. Keep the slightly awkward handmade drawing character. Do not make it polished vector art, realistic, painterly, three-dimensional, or childish in a different style. Use white or off-white negative space and restrained colours. 16:9.

The primary visual anchor is `references/art_style_v1.png`.

### Global negative block

> No photorealism, no 3D rendering, no gradients, no cinematic realism, no glossy shading, no polished corporate vector look, no detailed fabric simulation, no extra people, no unlisted objects, no text, no captions, no logos, no watermark, no border, no collage, no split screen, no multi-panel layout, and no change to approved character identity or geography.

## 3. Mara identity and wardrobe block

### Base identity — `C01_mara_base.png` APPROVED

> Mara Voss is a 36-year-old adult female wilderness instructor with an ordinary capable build, simple consistent facial features, dot eyes, a small natural mouth, and dark-auburn hair tied back in one practical braid. She wears a rust-orange hooded winter shell jacket, charcoal snow trousers, dark gloves, and dark-brown winter boots. She looks experienced, calm, and physically capable. Her dark gloves remain on whenever her hands appear; do not create bare-hand gestures. For tight portraits, crop her hands outside the frame unless they are required by the action. Preserve her exact face, hair colour, proportions, and outfit design from the approved base reference.

### Mara state rules

- **Training and crossing:** Dry base outfit; braid intact; orange shell worn normally.
- **After immersion:** Same face and outfit, but soaked; hair partly loosened by water; violent shivering; no blood or graphic injury.
- **Shelter:** Wet outer layers removed. She wears dry dark base layers and is wrapped in Evan's dark-green sleeping bag. The fixed post-setup layer order is **blue foam pad on snow → dark-green sleeping bag on the pad → silver emergency bivy outside, visibly draped over the bag's top and sides**. The silver bivy is never a groundsheet beneath or a loose sheet merely behind an exposed green bag; green may remain visible at the head opening and a narrow lower seam. Only the active setup shots may show Evan adjusting this coverage. Use `beat12m07` as the layer-order anchor; C04 is for upper-body identity only, not layer order or leg pose. Her right knee remains still and cannot bear weight. In every full-body shelter frame, both legs remain together and fully extended along the pad, with the right knee straight and one continuous sleeping-bag silhouette—never a raised knee, curled leg, or bent two-section pose. At rest and during every hand check or stillness shot, her head remains visible and all hands/gloves stay completely inside the bedding; Evan checks beneath the bivy without pulling out or displaying a hand. Only an explicit reaching or pointing action may show exactly one dark-gloved hand, with the other covered.
- **Part 2:** Same sheltered outfit and bedding. Her expression changes gradually with her condition; do not change her clothes to indicate improvement.
- **Part 3 and rescue:** She remains injured and sheltered. She does not stand or walk. Her orange jacket is no longer being worn because Evan uses it as a signal marker.

## 4. Evan identity and wardrobe block

### Base identity — `C05_evan_base.png` APPROVED

> Evan Reed is a 28-year-old adult male wilderness beginner with an ordinary build, short slightly messy dark-brown hair, simple consistent facial features, dot eyes, and a small natural mouth. He wears a muted teal winter jacket, grey winter trousers, brown boots, and a mustard-coloured personal backpack with a fixed pocket and strap layout. His muted teal jacket must never become rust-orange or red; rust-orange belongs to Mara alone. His winter trousers remain grey, never tan or khaki. His hands retain the pale, simple design shown in C05; do not introduce brown or dark gloves. He looks cautious and ordinary, not childish and not like a muscular action hero. Preserve his exact face, hair, proportions, and outfit design from the approved base reference.

### Evan state rules

- **Training and crossing:** Dry base outfit; mustard backpack present.
- **River rescue:** Same outfit; snow and water at his pale hands and knees; frightened but acting. Evan remains on the near bank. Frame his close-ups against unmistakable white snow, never blue water surrounding his body.
- **Shelter setup:** Backpack placed beside the shelter. Teal jacket and grey trousers remain on. Snow, moisture, and mild soot accumulate gradually.
- **Part 2 night:** Same clothing and hair; increasing exhaustion, no random wounds or new accessories.
- **Part 3 signal:** Same base outfit, using Mara's orange jacket only as a marker. His expression is afraid but focused, not triumphant or superhuman.

## 5. Location identity blocks

### Blackpine River — `L01_blackpine_river_day.png`

> A narrow, slow side channel of the Blackpine River in midwinter. Snow-covered ice, a near bank with a recognisable spruce root, a far bank with a current-weakened patch concealed beneath ordinary-looking snow, and muted spruce trees. Cold off-white daylight. No people unless the frame explicitly includes them.

### Broken-ice site — `L02_broken_ice_site.png`

> The exact same river composition and banks as L01, now with one broken opening and fractured shelf in the established weak-ice position. Do not move the banks, trees, opening, or spruce root.

### Spruce shelter — `L03_spruce_shelter_day.png`

> A sheltered spruce stand a short assisted walk from the river's near bank. Fixed tree trunks and open space for the sleeping pad, bivy, and an outdoor fire platform. Dead branches are available beneath the trees. The ground remains covered in white snow with pale-cyan shadows; no exposed dirt, mud, grass, or seasonal change. The site feels protected but not warm or comfortable. Never turn this location into a tent, lean-to, wooden A-frame, or constructed sleeping shelter. Before the script deliberately gathers firewood, keep loose logs and branch piles out of the immediate continuity background. The later fire base is only a small, low, flat platform of parallel natural sticks directly above continuous snow, never a shelter frame, stone slab, exposed-dirt patch, sawn-log raft, or upright wooden structure. For fire-base corrections, use the approved `beat10m07` narrative frame as the relevant visual continuity anchor.

### Night shelter — `L04_spruce_shelter_night.png`

> Exactly the same shelter geography as L03, changed only to dark-blue night conditions with wind and snow. Firelight may add restrained amber illumination outside the sleeping shelter. No new trees or layout changes.

### Rescue meadow — `L05_rescue_meadow_dawn.png`

> A nearby open snowy meadow within a short walk of the shelter, with a treeline connecting it visually to the same spruce stand. Pale dawn after the storm. Enough open snow for a large dark-branch X and an orange signal marker. No cliff or mountain climb.

## 6. Prop identity blocks

- **Mara's group pack:** Large navy expedition pack with fixed outer-pocket layout. It contains the group shelter, stove, her sleeping bag, and satellite messenger. It disappears beneath the ice and does not return.
- **Evan's backpack:** Mustard personal pack matching C05. Its pockets and straps do not change.
- **Throw rope:** Red rope with a simple loop and small red storage bag. Before the first throw, the bag remains visibly attached in every medium or wide shot and is small enough to hang from one hand; a close-up may exclude it only through cropping. Never turn it into a tall canister or make it appear and disappear between shots. Used from the bank, then stored on Evan's pack.
- **Sleep shelter kit:** Dark-green sleeping bag, blue foam pad, silver emergency bivy, and spare dry sweater. These remain at the shelter unless the story explicitly moves them.
- **Fire and first-aid kit:** Small fire kit, dry tinder container, metal cup, and waterproof first-aid booklet.
- **Navigation and signal kit:** Compass with sighting mirror and simple emergency whistle.
- **Orange shell jacket:** Mara's exact rust-orange jacket. Wet after immersion but retained. Used in Part 3 as the signal's orange centrepiece.

No prop may appear merely because it would make a frame more exciting. It must already exist in the story inventory.

## 7. Frame assembly template

For each narrative frame, assemble only the relevant information in this order:

> **STYLE:** Global art-style block.  
> **CHARACTERS:** Approved identity image(s) and current wardrobe/state.  
> **LOCATION:** Approved location image and current weather/light state.  
> **ACTION:** One clear action or reaction from the current narration moment.  
> **PROPS:** Only the relevant approved prop(s), with their current condition.  
> **COMPOSITION:** Specify who is where, the single focal point, and what the viewer must understand immediately.  
> **NEGATIVE:** Global negative block plus any scene-specific exclusions.  
> **FORMAT:** 16:9.

Example of the level of specificity required for a river frame:

> Mara is chest-deep in the established broken opening near the far bank, wearing the soaked version of her base outfit. Evan is on the near bank in his dry teal outfit, lying low on solid ground and throwing the red rope toward her. The viewer must understand that Evan is rescuing from the bank rather than entering the broken ice. Keep the river, trees, opening, and characters consistent with their approved references. One coherent scene only. 16:9.

## 8. Continuity checks before accepting any image

1. Do the faces and hairstyles match the approved character bases?
2. Is each character wearing the correct outfit for this exact story point?
3. Is Mara's right-knee limitation respected?
4. Are the river opening, shelter trees, and meadow consistent with their approved geography?
5. Are only currently available props visible?
6. Is the action physically consistent with the research, such as Evan rescuing from the bank?
7. Is there exactly one clear idea rather than multiple scenes in one image?
8. Does the drawing technique match the approved loose style rather than a polished vector style?
9. Are all frames in the production batch identical in pixel dimensions?
10. Has the image been reviewed rather than accepted only because generation succeeded?

## 9. Reference selection by story area

| Story area | Images to combine |
|---|---|
| Training | Style + Mara base + Evan base + relevant location + fire kit |
| River crossing | Style + both base characters + L01 |
| River rescue | Style + Mara post-immersion + Evan base/panic + L02 + throw rope |
| Shelter setup | Style + Mara shelter wrap + Evan base + L03 + sleep kit |
| Part 2 night | Style + Mara shelter wrap + Evan base + L04 + relevant existing kit |
| Dawn signalling | Style + Evan determined + L05 + orange jacket + navigation/signal kit |
| Rescue | Style + both correct character states + established meadow/shelter geography |

Do not include a scene-bearing reference when only a character identity is needed; use the scene-free base character anchor instead.
