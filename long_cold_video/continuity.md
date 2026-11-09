# CONTINUITY — long_cold_video

> Status: **DRAFT** — style anchors get locked at STATE 4 after 2–3 style tests. Copy the blocks below VERBATIM into every prompt.

## Art direction reference
`refs/ref_style_01_modern_caveman_3panel.jpg`, `refs/ref_style_02_caveman_phone_cave.jpg`
**Use:** rendering medium, line weight, shading, palette, face/hair shapes.
**Never use:** their composition, cave layout, props, or framing as a template. Environment changes per row.

## STYLE & MEDIUM (verbatim block)
> Ink-and-watercolour cartoon on warm off-white parchment paper, loose confident black ink outlines with visible line weight variation, soft wet-on-wet watercolour washes that bleed slightly past the linework, visible cold-press paper grain and a subtle uneven paper edge framing the image, limited palette of slate blue-grey and pale cyan for cold, amber and burnt ochre for firelight, desaturated shadows, no gradients, no 3D render, no photorealism, no digital airbrush, no text, no lettering, no signage, no logos.

## PROTAGONIST ("You") (verbatim block)
> A single everyman survivor drawn in the same ink-and-watercolour cartoon style: perfectly round white head with no nose, two simple black dot eyes and a small thin-line mouth, shaggy dark-brown hair falling over the forehead, thin black stick-like limbs with rounded hands and feet, slender cartoon body. Clothing: layered winter wear — oversized dark-navy wool coat over a grey jumper, thick olive scarf, dark trousers, scuffed boots, worn knitted gloves, small canvas backpack. Face reads tired, wary, determined. Never photorealistic, never muscular, never a child, never a second protagonist in the same frame.

## Supporting cast (lock when first used)
- **The driver:** broad-shouldered man, full frost-caked beard, orange knit cap, patched canvas work jacket, one chipped front tooth, calm flat stare. Never armed on screen; rifle stays out of frame.

## Palette lock
- Cold exteriors: slate `#5A6B7B`, pale cyan snow `#DCE8EE`, bruise-violet sky `#3C3F5C`, paper `#F2E8D5`.
- Firelight: amber `#E0913A`, burnt ochre `#B4652A`, deep brown shadow `#3A2A22`.
- Snow is NEVER pure white; it always carries paper warmth or blue shadow.

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
4. Breath vapour in every exterior beat.
5. The protagonist's scarf is olive in every shot — a colour anchor for continuity.

## Declared exceptions
_(none yet)_

---

## LOCKED ANCHORS (STATE 4) — 3 style tests, one hand

All three were generated with the identical **master prompt formula** and came back interchangeable in style. Use `style_test_A` as the canonical wide-shot anchor, `B` for firelight interiors, `C` for close-ups. Any drift from these three is a QC fail.

```
refs/style_test_A_highway.png    HIGH WIDE — the doors-open highway (canonical anchor)
refs/style_test_B_bucketfire.png MEDIUM LOW — bucket fire, amber vs slate split
refs/style_test_C_face.png       EXTREME CLOSE-UP — frost brows, olive scarf, breath plume
```

### Master prompt formula (no re-ordering, ever)
```
[STYLE & MEDIUM verbatim block] + [PROTAGONIST ("You") verbatim block] + [DYNAMIC FRAMING & ACTION from visuals.csv]
```

### Exact prompts used for the anchors (copy these verbatim, swap only the final framing clause)

**A — canonical anchor**
> 16:9 widescreen cinematic illustration. Ink-and-watercolour cartoon on warm off-white parchment paper, loose confident black ink outlines with visible line weight variation, soft wet-on-wet watercolour washes that bleed slightly past the linework, visible cold-press paper grain and a subtle uneven paper edge framing the image, limited palette of slate blue-grey and pale cyan for cold, amber and burnt ochre for firelight, desaturated shadows, no gradients, no 3D render, no photorealism, no digital airbrush, no text, no lettering, no signage, no logos. A single everyman survivor drawn in the same ink-and-watercolour cartoon style: perfectly round white head with no nose, two simple black dot eyes and a small thin-line mouth, shaggy dark-brown hair falling over the forehead, thin black stick-like limbs with rounded hands and feet, slender cartoon body. Clothing: layered winter wear, oversized dark-navy wool coat over a grey jumper, thick olive scarf, dark trousers, scuffed boots, worn knitted gloves, small canvas backpack. Face reads tired, wary, determined. Never photorealistic, never muscular, never a child, never a second protagonist in the same frame. + HIGH WIDE SHOT: the survivor stands tiny between lanes of an eight-lane highway jammed with snow-covered abandoned cars, their driver doors hanging open in a sawtooth line receding to the horizon, heavy straight snowfall, a dead streetlight overhead, pale cyan drifts against slate-blue bodies, bruised violet-grey sky, breath vapour, no warm light anywhere.

**B — firelight lock**
> [same style + protagonist blocks] + MEDIUM SHOT, slightly low angle: the survivor crouched on a concrete floor beside a small paper fire burning in a dented metal bucket, both hands held out to the flames, orange amber light on one cheek and cold slate-blue on the other, dark shelving and blank cardboard boxes behind, steam and smoke curling upward, firelight pooling on the floor; mean small fire, not a cosy hearth.

**C — close-up lock**
> [same style + protagonist blocks] + EXTREME CLOSE-UP of the survivor's face filling the frame, olive scarf pulled up under the chin, hoar frost crusting the eyebrows and eyelashes, cracked lips, a plume of breath vapour catching pale grey light, snow blurring out of focus behind, cold slate-blue wash on the skin, one tiny warm amber highlight in each dot eye, the paper edge of the drawing visible at the top corner.

### Anchor observations (QC notes for workers)
- The model renders the face **rounder and softer** than the stick figure in the original refs. This is the locked look — do not fight it.
- Hair renders long and shaggy with visible individual strands. Consistent across all three.
- Hands render semi-realistic (4 fingers), not pure circles. Accept it; do not re-roll for finger count unless a hand is melted or duplicated.
- `no lettering` in the style block is doing real work — keep it in every prompt or signage text will appear.
- Fire is **small and mean** (bucket, paper). Any prompt that implies a generous hearth breaks the film's physics.
