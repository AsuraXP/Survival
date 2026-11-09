# WORKER PACKETS — `long_cold_video` (v3 look, post-batch-01)

Hand these to the worker chats. **289 frames total, 6 already done** (`beat01m01`–`beat01m06`) → **283 frames** split 91 / 96 / 96.

---

## SHARED BLOCK — every worker copies this verbatim

```
REPO / BRANCH
  git clone --depth 1 --branch arena/3185860a-survival https://github.com/AsuraXP/Survival.git
  Work ONLY on that existing branch. Do NOT create a branch. Commit after every batch.

YOUR SOURCE OF TRUTH
  long_cold_video/visuals.csv — row N = one frame.
    moment_text    = the exact words that frame illustrates (drives the cut, never rewrite it)
    visual_prompt  = the framing/action clause you append after the locked prefix

STYLE CONDITIONING IMAGE (mandatory on every generation)
  long_cold_video/refs/ref_style_02_caveman_phone_cave.jpg
  Instruction: "Match the drawing technique, line quality, paper texture and character design of the
  reference image EXACTLY. Do NOT reuse the cave, fire pit, carved panel, potted plant or starry sky —
  compose an entirely new scene."

LOCKED PREFIX — paste verbatim in front of every row's visual_prompt
Match the drawing technique, line quality, paper texture and character design of the reference image EXACTLY: clean confident black ink outlines of varying weight, loose hatching for shadow, flat transparent watercolour washes inside the lines with a few intentional bleeds, warm cream parchment paper with visible grain and a slightly uneven torn paper border. Do not reuse the cave, fire pit, carved panel, potted plant or starry sky from the reference - compose an entirely new scene. Hand-drawn comic watercolour illustration, palette of ochre, burnt sienna, warm brown and cream with cool slate blue and deep indigo for cold and night, no gradients, no airbrush, no 3D render, no photorealism, no anime, no glossy shading, no text, no lettering, no signage, no logos. A single cartoon survivor drawn in exactly the reference character's design: perfectly round cream-white head with no nose, EXACTLY TWO small solid black dot eyes set wide apart and symmetrical, both eyes fully visible inside the frame, never one eye, never a single eye, never three eyes, with a thin single black line for a mouth, shaggy dark-brown hair drawn as loose spiky ink strokes over the forehead, thin black stick-like arms and legs with rounded hands and feet, compact small body, heavy dark-navy hooded parka over a thick olive-green scarf, brown wool trousers, sturdy boots, small canvas backpack.

FACE RULE (learned the hard way in batch 01)
  Never write or imply "one eye", "single eye", "an eye". If a beat is eye-level, widen it to a full
  face crop containing BOTH eyes. A one-eyed face = automatic QC fail.

NO-TEXT RULE
  "no text, no lettering, no signage, no logos" stays in every prompt. Drop it and you get signage
  gibberish. Screens, gauges, notices and packaging are always blank or abstract.

NO-PEOPLE BEATS
  If the row has no figure (empty room, macro object), close the clause with
  "NO PEOPLE anywhere in the frame" or the prefix will invent a survivor.

OUTPUT
  long_cold_video/frames/beat{slide:02d}m{moment:02d}.png   e.g. beat07m03.png
  Slide/moment come from the CSV columns (zero-padded, 2 digits). NEVER overwrite an existing file.

BATCH CADENCE
  6 frames per turn → build a contact sheet (~380px thumbs, include rejects) → commit → push.
  Repair budget: 2 re-rolls per turn, changing ONE clause only. After 3 failures on one frame,
  ship the closest version and append a DECLARED EXCEPTION line to long_cold_video/STATE.md.

NEVER
  crossfades / dissolves / fades · on-screen captions · extra characters · visible weapons · gore ·
  photoreal, 3D, anime or glossy rendering · pure-white snow (snow is pale blue wash on paper).
  NO TTS, NO VOICE WORK, NO AUDIO MIXING, NO FFMPEG. Frames only.

COMMIT
  git add long_cold_video/frames && git commit -m "w<N> batch <k>: beats <first>..<last>" && git push
```

---

## WORKER 1 — rows 7-97 · 91 frames · `beat01m07` → `beat15m07`
```
- Scan: apartment wake-up (row 7 = end of slide 01) → phone/sister → frozen tiles → frost inside glass →
  dead taps → street & snow → front door → hallway → lock → waiting on the bed → dawn + thermometer →
  numb hands → inventory → dressing → lighter/matches/book → final message → car won't start
- Skip: beat01m01-m06 already exist. Start at CSV row 7.
- Firelight rows: none. This whole chunk is cold slate/indigo against warm paper — keep the contrast.
- Scene shifts inside your range: bedroom → kitchen → exterior street → hallway → bed → kitchen again.
  Change the room's angle every cut; never repeat a previous setup.
- Specular care: taps, thermometer and phone screens must be BLANK — no numbers, no icons, no lettering.
- Deliver: 91 frames, contact sheet per batch, declared exceptions in STATE.md.
```

## WORKER 2 — rows 98-193 · 96 frames · `beat16m01` → `beat31m05`
```
- Scan: dressing detail → car/kerb → eight-lane frozen highway + open doors → garden gate & wreath house →
  peaches/blanket/photograph → gas station at dusk → the still figure behind the counter → lighter →
  bucket fire → crying → day 2-3 cold maths → water inside the coat
- Skip: nothing — your range is clean. Start at CSV row 98.
- Firelight rows: slides 26-29 (gas station interior, bucket fire, tears). Amber/ochre on one side of the
  face, slate/indigo on the other. The fire is small and mean, never a cosy hearth.
- The still figure (slide 26, moments that mention the man): face turned away, motionless, NO DETAIL, NO GORE.
  Render him as a jacket and a still shape at the counter, nothing more.
- The photograph (slide 24): figures inside abstract and faceless — no readable portrait.
- Scene shifts inside your range: interior → street → highway → suburb → roadside commerce → open road.
- Deliver: 96 frames, contact sheet per batch, declared exceptions in STATE.md.
```

## WORKER 3 — rows 194-289 · 96 frames · `beat32m01` → `beat46m13`
```
- Scan: hypothermia maths → clapping hands → the polite exit → church at night → candles & noticeboard →
  names said out loud → dawn → truck arrives → driver at the window → family question → terms → the deal →
  the coast → surf → coda
- Skip: nothing — your range is clean. Start at CSV row 194.
- Firelight rows: candle beats in the church (slide 36) and the roadside bucket fire (slide 44).
  Use the firelight lock anchor: refs/v3_anchor_B_bucketfire.png.
- The driver: broad shoulders, frost-caked beard in ink hatching, orange knit cap, patched canvas jacket,
  chipped front tooth, flat tired stare. NEVER armed on screen; the glove box stays shut and closed.
- The coast (slides 45-46): thaw, not tropics. Grey-green water, pale wash sky, no palms, no sunshine glow.
- Final frame beat46m13 is the film's last image — a figure walking into pale watercolour light.
- Deliver: 96 frames, contact sheet per batch, declared exceptions in STATE.md.
```

---

## QC CHECKLIST (run on every frame before commit)
1. Does it show its `moment_text`? If the words and the picture don't match, it fails regardless of beauty.
2. Face: two dot eyes, cream round head, shaggy ink-stroke hair — or no face at all.
3. Line quality: black ink outlines + flat wash. Photoreal, glossy, 3D, anime = fail.
4. No text anywhere. No extra people. No weapons. No gore. No pure-white snow.
5. Framing must differ from the frame before it. Two identical setups in a row = re-roll.
6. Filename matches the CSV row exactly and does not overwrite an existing frame.
