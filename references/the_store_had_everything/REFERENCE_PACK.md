# The Store Had Everything — Opening Reference Pack

Status: **style direction selected by the user; identity/location pack awaiting user approval.** No pilot frame batch has been generated yet.

## Pack purpose

This pack separates character identity, character construction, environment, and geography so that later prompts do not have to reinvent them together. It supports the reusable opening pilot and then the remaining Part 1 frames.

## S00 — User character-construction source

**File:** `character_style_user.jpg`
**Role:** round-head, minimal oval-eye, thin-limb character construction only.
**Does not control:** wardrobe, colour palette, store, props, lighting or composition.

## S01 — Selected hybrid style anchor

**File:** `examples/the_store_had_everything/style_tests/hybrid_opening_establishing.png`
**Dimensions:** 1672×941
**Status:** user selected option 1 of the hybrid test.

**Approved role:** the visual relationship between simple expressive characters and a vivid, detailed environment.

**Not approved as a final story frame:** the clean background plate below is the canonical opening environment. Using both images as interchangeable backgrounds would create the kind of environmental jumping we are trying to prevent.

## C01 — Nolan identity

**File:** `nolan_identity.png`
**Dimensions:** 928×1152

- Round pale head, sparse dark-brown fringe, black vertical oval eyes, thin limbs.
- Teal fleece vest, charcoal shirt, dark trousers and dark sneakers.
- Blank badge on a dark lanyard.
- No backpack, radio or hand props in this identity image.
- Worried-but-determined expression comes from brows, mouth and posture rather than realistic facial detail.

![Nolan identity](nolan_identity.png)

## C02 — Lena identity

**File:** `lena_identity.png`
**Dimensions:** 928×1152

- The same simple character construction and approximate proportions as Nolan.
- Smooth black hair with one narrow braid over her anatomical right shoulder when visible.
- Amber delivery jacket, burgundy shirt, navy cargo trousers and dark work shoes.
- Van keys are canonical in her **anatomical right hand**; this is the viewer-left hand in the straight-on reference.
- No backpack or radio in the opening paragraph.

![Lena identity](lena_identity.png)

## L01 — Opening store background master

**File:** `opening_store_background.png`
**Dimensions:** 1376×768

- Protagonists removed; the checkout and floor are reconstructed.
- Front glass, blue night and the non-graphic infected crowd remain at frame-left.
- Shutter housing remains raised; overhead public-address speaker remains visible.
- Orange tent, blue coolers and green kayak wall are fixed landmarks.
- Rear stairs and elevated cyan-lit security office remain at rear-right.
- Amber and blue lighting is part of the master state.

**Production rule:** this is the only canonical background for opening setup A01. Later same-setup frames must preserve it rather than substituting the selected style test or a freshly invented store.

![Opening store background](opening_store_background.png)

## M01 — Store schematic and geography

**Files:** `store_floor_plan.svg`, `STORE_GEOGRAPHY.md`

The schematic fixes the front/checkouts, camping landmarks, direct aisle, rear stairs, elevated office, stockroom, loading bay, van direction and alarmed side exit. It also records the opening route and the states that may change only later in the script.

[Open the store floor plan](store_floor_plan.svg)

## Prompting and continuity rules

- `PROMPT_BIBLE.md` defines reference hierarchy, canonical descriptions, prompt order and negative constraints.
- `examples/the_store_had_everything/CONTINUITY_PROTOCOL.md` defines scene-state and sequence-review requirements.
- `examples/the_store_had_everything/OPENING_PILOT_PLAN.md` defines initial blocking and reusable-audio/frame production.

## Internal visual QA

| Asset | Result | Notes |
|---|---|---|
| S01 selected hybrid | Accepted as style anchor | Simple characters read against a rich environment; not used interchangeably with L01. |
| C01 Nolan | Pass for user review | Identity, wardrobe, blank badge and no unrequested props are readable. |
| C02 Lena | Pass for user review | Keys and braid are now explicitly canonical on her right side; no radio appears early. |
| L01 background | Pass for user review | No protagonists inside; required landmarks and infected-outside state are present. |
| M01 schematic | Pass for user review | Valid SVG; relationships match the written geography. |

## Approval requested

Approve or request changes to **C01 Nolan, C02 Lena, L01 opening background and M01 geography as a pack**. After approval, these become locked references for the opening pilot. Pilot frames will still require their own batch and sequence approval.
