# CONTINUITY — long_cold_video

> **v3 LOCK (current).** Style = the user's original reference: `refs/ref_style_02_caveman_phone_cave.jpg`.
> v1 (dark anime-watercolour) and v2 (gouache / ink-wash / matte) are **REJECTED** — do not reuse anything from them.

## Art direction reference
`refs/ref_style_02_caveman_phone_cave.jpg` — **the canonical look.** Clean black ink line, flat warm watercolour, cream parchment, round white head, dot eyes, shaggy ink-stroke hair.
`refs/ref_style_01_modern_caveman_3panel.jpg` — same look, secondary.
**Use:** drawing technique, line quality, paper texture, palette, character design.
**Never use:** their composition, cave layout, props (fire pit, carved panel, potted plant, starry sky), or framing as a template. Environment changes per row.

## STYLE & MEDIUM (verbatim block — paste unchanged into every prompt)
> Hand-drawn comic watercolour illustration on warm cream parchment paper: confident black ink outlines of clearly varying weight, loose hatching and cross-hatch strokes for shadow, flat transparent watercolour washes laid inside the ink lines that occasionally bleed a little past them, visible cold-press paper grain, a slightly uneven hand-torn paper border framing the whole image, warm cream paper tone, palette of ochre, burnt sienna, warm brown and cream with cool slate blue and deep indigo reserved for night, snow and distance, no smooth gradients, no airbrush, no 3D render, no photorealism, no anime or manga rendering, no glossy shading, no text, no lettering, no signage, no logos.

## PROTAGONIST ("You") (verbatim block — paste unchanged into every prompt)
> A single cartoon survivor drawn in exactly the reference character's design: perfectly round cream-white head with no nose, exactly two small solid black dot eyes set wide apart and symmetrical (always two, never one) with a thin single black line for a mouth, shaggy dark-brown hair drawn as loose spiky ink strokes falling over the forehead, thin black stick-like arms and legs with simple rounded hands and feet, compact small body. Modern winter clothing in flat watercolour washes: heavy dark-navy hooded parka, thick olive-green scarf, brown wool trousers, sturdy brown boots, small canvas backpack. Expression simple, tired, wary, never shaded realistically, never glossy, never anime, never muscular, never a child, never a second survivor in the same frame.

## Supporting cast (lock when first used)
- **The driver:** broad-shouldered man, full frost-caked beard drawn in ink hatching, orange knit cap, patched canvas work jacket, one chipped front tooth, flat tired stare. No weapon ever on screen.

## Palette lock (sampled from the reference)
- Paper `#F2E8D5` · cream face `#FBF7EF` · ink `#1E1A17` · ochre `#C9973F` · burnt sienna `#8C4F2B` · olive scarf `#7A7A45`
- Cold: slate `#5C6E7E` · pale snow blue `#D8E3EA` · indigo night `#2E3552`
- Firelight: amber `#E0913A` · ember red `#B4652A`
- Snow is NEVER pure white: it is paper with a pale blue wash. Ink lines never disappear under a wash.

## Content moderation swaps
| Intended | Shipped wording |
|---|---|
| frozen corpse, dead man sitting up | "a still figure in a jacket behind the counter, face turned away, motionless, no detail, no gore" |
| frostbite, blackened skin | "fingertips pale and waxy, hands held stiffly" |
| gun, rifle | not depicted on screen at all |
| starving / emaciated | "hollow-cheeked, drawn, coat hanging loose" |

## Recurring visual motifs (must not drift)
1. Frost on the **inside** of glass — crystalline ferns on the inner pane, breath fog in the foreground.
2. The sun as a **pale coin** behind smoked glass, no rays, no glow.
3. Fire in a **metal bucket**, small and mean, never a cosy hearth.
4. Breath vapour in every exterior beat, drawn as two or three thin ink curls.
5. The protagonist's scarf is olive in every shot — the colour anchor for continuity.
6. Faces stay simple and unshaded: cream fill, dot eyes, one line mouth. No rendering.

## Master prompt formula (no re-ordering, ever)
```
[STYLE & MEDIUM verbatim block] + [PROTAGONIST ("You") verbatim block] + [DYNAMIC FRAMING & ACTION from visuals.csv]
```

## Reference-conditioning note
When a generation tool accepts a reference image, pass `refs/ref_style_02_caveman_phone_cave.jpg` with the instruction: *match the drawing technique, line quality, paper texture and character design exactly; compose an entirely different scene; do not reuse the cave, fire pit, carved panel, plant or starry sky.*

## v3 ANCHORS — **APPROVED (user, this session)**
| File | Shot | Status |
|---|---|---|
| `refs/v3_anchor_A_highway.png` | HIGH WIDE, doors-open highway | LOCKED — canonical |
| `refs/v3_anchor_B_bucketfire.png` | MEDIUM LOW, bucket fire | LOCKED — firelight lock |
| `refs/v3_anchor_C_closeup.png` | EXTREME CLOSE-UP, face | LOCKED — close-up lock |

### CANONICAL PROMPT PREFIX (v3) — use verbatim, every single frame
Pass `refs/ref_style_02_caveman_phone_cave.jpg` as the style-conditioning image, then this text, then the row's framing clause:

> Match the drawing technique, line quality, paper texture and character design of the reference image EXACTLY: clean confident black ink outlines of varying weight, loose hatching for shadow, flat transparent watercolour washes inside the lines with a few intentional bleeds, warm cream parchment paper with visible grain and a slightly uneven torn paper border. Do not reuse the cave, fire pit, carved panel, potted plant or starry sky from the reference - compose an entirely new scene. Hand-drawn comic watercolour illustration, palette of ochre, burnt sienna, warm brown and cream with cool slate blue and deep indigo for cold and night, no gradients, no airbrush, no 3D render, no photorealism, no anime, no glossy shading, no text, no lettering, no signage, no logos. A single cartoon survivor drawn in exactly the reference character's design: perfectly round cream-white head with no nose, exactly two small solid black dot eyes set wide apart and symmetrical (always two, never one) with a thin single black line for a mouth, shaggy dark-brown hair drawn as loose spiky ink strokes over the forehead, thin black stick-like arms and legs with rounded hands and feet, compact small body, heavy dark-navy hooded parka, thick olive-green scarf, brown wool trousers, sturdy boots, small canvas backpack.

- **Never in frame:** a readable word. Blankets of lettering appear if `no text` is dropped — it is load-bearing.
- **No-people beats:** close the framing clause with "NO PEOPLE anywhere in the frame" — the prefix alone will otherwise invent a figure.
- **FACE RULE (added after batch 01 defect):** never write "one eye", "single eye", "an eye", or any clause that can be read as a one-eyed face. The character has exactly two dot eyes. A tight crop must always read as a face containing two eyes, both fully inside the frame:
  - WRONG: "extreme close-up of one open eye in the dark"
  - RIGHT: "tight close-up of the face, both dot eyes wide open and symmetrical, head filling the frame"
  - If a beat needs an eye-level detail, lift the camera to a full face crop rather than a single-eye macro.

## Batch log
- **Batch 01** — `beat01m01`–`beat01m06` — 6/6 pass. Style, line quality, palette and face all match anchor A/B/C. All six frames were generated at 1393x752 (consistent), no rejects, repair budget unspent. Framing genuinely varies row to row (wide bedroom → macro eye → overhead floor → low-angle door → over-the-shoulder → macro vent).

## Declared exceptions
_(none yet)_
