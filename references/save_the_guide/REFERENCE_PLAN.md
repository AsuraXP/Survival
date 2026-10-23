# Save the Guide — Reference Image Plan

**Status:** All seven character references and all five location references are approved and locked. All seven prop candidates have been generated and are awaiting user review.

## Purpose

These references are continuity anchors, not video frames. They define the cast, wardrobe, geography, props, and recurring visual states before any narrative frame is generated.

The approved global art-style anchor is:

- `references/art_style_v1.png`

## Reference rules

1. Generate character and prop anchors on plain, scene-free backgrounds so environmental details do not leak into unrelated frames.
2. Generate locations separately from the characters.
3. Use the approved art style, not the PFP character design: rough hand-drawn linework, simple anatomy, flat muted colour, pale offset accents, and uncluttered compositions.
4. Do not lock a reference until it is approved. An approved file is never silently overwritten.
5. Any deliberate redesign receives a new version, such as `mara_base_v02.png`, and requires fresh approval.
6. A story frame receives only the relevant anchors: global style + character + location + important prop. Do not overload a generation with every reference.

## A. Character references

| File | Required content | Continuity purpose |
|---|---|---|
| `C01_mara_base.png` | Full-body Mara, neutral stance, tied-back dark-auburn hair, rust-orange shell, charcoal snow trousers, dark gloves and boots | Master identity, proportions, hair, wardrobe, and colour |
| `C02_mara_face_calm.png` | Close portrait with the same face and hair; calm, economical expression | Prevents facial identity changing between scenes |
| `C03_mara_post_immersion.png` | Same Mara immediately after rescue: soaked outerwear, hair loosened by water, shivering, no graphic injury | River-bank state only |
| `C04_mara_shelter_wrap.png` | Same Mara in dry dark base layers, wrapped in Evan's sleeping bag with foam pad beneath and bivy outside; right knee kept still | Main shelter state for Parts 1–3 |
| `C05_evan_base.png` | Full-body Evan, simple dark hair, teal jacket, grey winter trousers, brown boots, mustard backpack | Master identity, proportions, wardrobe, and colour |
| `C06_evan_panic.png` | Close portrait of Evan frightened and hesitating, without changing his face or hair | River and fire-failure expressions |
| `C07_evan_determined.png` | Close portrait of Evan afraid but focused; no superhero jawline or redesign | Later rescue, night, and signalling expressions |

### Character design guardrails

- Mara must look like an experienced adult instructor, not a helpless victim or a stylised fashion model.
- Evan must look like an ordinary adult beginner, not a child and not an instantly muscular action hero.
- Faces stay simple and consistent with the approved loose drawing style.
- Mara remains recognisable with wet hair, dry layers, and wrapped in bedding.
- Evan's determination must still contain fear; his expression does not become a different character.

## B. Location references

| File | Required content | Continuity purpose |
|---|---|---|
| `L01_blackpine_river_day.png` | Narrow, slow side channel; snow-covered ice; near bank with a usable spruce root; far bank with the concealed current-weakened area; no people | Master geography before the accident |
| `L02_broken_ice_site.png` | Same river and banks after the break, with the opening and broken shelf in fixed positions; no people or equipment | Accident and rescue continuity |
| `L03_spruce_shelter_day.png` | Sheltered spruce stand near the river; fixed tree positions, dry branch supply, space for windbreak and outdoor fire platform; no people | Main Part 1 environment |
| `L04_spruce_shelter_night.png` | Exactly the same site at night with wind, snow, dark-blue ambience, and a safe exterior fire area | Part 2 continuity, not a new location |
| `L05_rescue_meadow_dawn.png` | Nearby open snowy meadow with a recognisable treeline leading back toward the same spruce stand; clearing weather at dawn | Part 3 signal geography |

### Geography to lock

- The river rescue begins from the **near bank**, where Evan remains with the rope.
- The weak patch is near the **far bank**, not a random hole elsewhere in later frames.
- The spruce shelter is a short assisted walk from the near bank.
- The meadow is close enough for Evan to reach briefly at dawn; it is not a mountain climb.
- Once these relationships are approved, camera angles may change but geography may not.

## C. Prop and wardrobe references

| File | Required content | Story purpose |
|---|---|---|
| `P01_mara_group_pack.png` | Large navy expedition pack with identifiable outer pockets; satellite messenger visible in an early explanatory insert only | Establishes what is lost beneath the ice |
| `P02_evan_mustard_pack.png` | Mustard personal backpack with fixed pocket and strap layout | Evan's recurring personal kit |
| `P03_throw_rope.png` | Red throw rope with a simple loop and storage bag | River rescue and later storage on Evan's pack |
| `P04_sleep_shelter_kit.png` | Dark-green sleeping bag, blue foam pad, silver emergency bivy, and spare dry sweater as one simple still life | Shelter continuity; prevents kit changing between frames |
| `P05_fire_first_aid_kit.png` | Small fire kit, dry tinder container, metal cup, and waterproof first-aid booklet | Fire sequence and Part 2 decision-making |
| `P06_navigation_signal_kit.png` | Compass with sighting mirror and a simple emergency whistle | Part 3 signalling |
| `P07_orange_shell_jacket.png` | Mara's rust-orange shell as a standalone garment | Wet-layer tracking and the final visible signal |

### Prop continuity rules

- The navy group pack and its contents disappear in Part 1 and do not return.
- Evan's sleeping bag, pad, bivy, and sweater remain at the shelter unless explicitly used elsewhere.
- The orange jacket is wet after the rescue but remains with them; it is not lost with the navy pack.
- The compass and whistle must not appear in an emergency frame unless established in Evan's kit.
- Small wear—snow, moisture, and soot—may accumulate, but colours and identifying shapes remain fixed.

## D. Character-state ledger

| Story point | Mara | Evan |
|---|---|---|
| Training and crossing | Dry base outfit, orange shell, tied-back hair | Dry teal outfit, mustard pack |
| Immediately after rescue | Soaked, shivering, hair loosened, right-knee injury begins | Snow at knees and gloves, frightened |
| Shelter setup | Wet outer layers removed; dry base layers and sleeping insulation | Same base outfit, increasingly wet and tired |
| Part 1 cliffhanger | Sheltered, confused, no longer shivering | Fire lit, alarmed by her condition |
| Part 2 night | Same wrapped state; gradual, medically plausible response to warming | Soot, snow, exhaustion; no costume change |
| Part 3 signal | Same sheltered state, still unable to walk | Same clothing, using her orange jacket only as the signal marker |
| Rescue | Still injured and receiving assistance | Relieved but exhausted, not transformed into an action hero |

## E. Colour and lighting anchors

- **Base environment:** White snow, icy pale blue, muted spruce green, charcoal outlines.
- **Mara:** Rust orange, charcoal, dark auburn.
- **Evan:** Muted teal, grey, brown, mustard.
- **Fire:** Warm amber used sparingly against the cold palette.
- **Night:** Dark navy and blue-grey, with warm firelight rather than a new palette.
- **Dawn:** Pale icy blue with restrained peach light; no polished cinematic gradients.

## F. Approval and generation order

1. Approve this plan and any changes to names, outfits, or geography.
2. Generate `C01_mara_base.png` and `C05_evan_base.png`; review identity and style first.
3. Generate the remaining character states and expressions using the approved base images as anchors.
4. Generate river and shelter locations; review geography before adding characters.
5. Generate props and the dawn meadow.
6. Lock the complete pack and record the approved files in a reference manifest.
7. Only then write the moment-by-moment visual plan and generate narrative frames.

No frame should be used to “figure out” what a main character or recurring location looks like after production has already started.
