# The Store Had Everything — Continuity Protocol

Status: mandatory production rule for the new story. This responds directly to the spatial jumps in the finished _Save the Guide_ frames: a person changed position within one uninterrupted situation, and background landmarks moved or disappeared between shots.

## Diagnosis

Those jumps were not caused by one bad prompt alone. The previous process allowed a fresh image interpretation without carrying enough of the previous shot's physical state forward. Incomplete references and prompts that described appearance more strongly than space made the problem worse.

For this project, a beautiful frame with broken geography is a failed frame.

## 1. Lock the scene before generating variations

Every continuous scene receives a **scene-state record** and an approved **establishing master** before close-ups or action variations are made.

The record fixes:

- Location and exact sub-area.
- Story beat and what has physically changed in that beat.
- Fixed background landmarks and their relative positions.
- Each character's position relative to those landmarks.
- Facing direction, gaze target, posture, and current action.
- Which hand holds each prop; open/closed doors; on/off lights and equipment.
- Damage, wetness, dirt, inventory, and other accumulated state.
- Camera side and screen direction.

Example of the required level of specificity:

> Nolan is crouched behind checkout 3, left shoulder toward the front glass, facing screen-right toward Lena. Lena is one step behind him on his right, van keys closed in her left hand. The blue cooler stack remains behind them on frame-left. The orange tent display is farther back on frame-right. Neither changes position until the narration says they run.

A prompt such as “Nolan and Lena hide nervously in the store” is not sufficient.

## 2. Required reference pack

Before full story frames, approve and retain:

- Character turnaround and expression sheets for Nolan and Lena.
- Wardrobe and prop references, including Nolan's store key/lanyard and Lena's van keys/radio.
- A store floor plan with numbered landmarks and prohibited shortcuts.
- Establishing masters for each recurring camera setup.
- Detail/background masters for the storefront, camping route, security office, and loading bay.
- A palette and lighting reference for each location state.

A character portrait alone is not a scene reference. A location master alone is not a character reference. Same-scene prompts must receive the relevant approved references together.

## 3. Same situation means the same physical state

Within one uninterrupted situation:

- A cut may change framing, lens feel, or camera angle without relocating anybody.
- A close-up must preserve the position established by the preceding wide shot.
- A reverse angle must preserve eyelines and the 180-degree screen direction.
- A hand, prop, door, or light cannot switch state without a story action that changes it.
- Background landmarks cannot move closer, vanish, or exchange sides merely because the crop changes.
- A pose may progress only when the narration or shot plan calls for that movement. The next pose must be reachable from the previous one.

If a new composition cannot preserve those facts, change the shot plan or create an explicit new story beat; do not quietly reset the scene.

## 4. Generate from the right anchor

- Use the approved establishing master plus character references for all shots in that setup.
- When a shot is a direct continuation, also use the immediately preceding approved frame as an action/position reference.
- Prefer a controlled edit of the approved scene state for small pose or expression changes when that preserves the background better than a fresh generation.
- After an approved physical move, create and approve a new establishing master before generating more close-ups.
- Never use a frame from another location state, damage state, wardrobe state, or prop state as a convenient substitute.

Each generation record will list the exact reference files used. No anonymous “reference image” placeholders.

## 5. Prompt structure

Every story-frame prompt must contain, in this order:

1. **Shot purpose:** the narration moment and intended emotion.
2. **Continuity anchor:** scene ID, master ID, and previous approved frame if applicable.
3. **Fixed spatial state:** landmarks, character positions, facing, gaze, props, and equipment state.
4. **The one intended change:** camera, expression, or specific action.
5. **Identity and style references.**
6. **Preservation constraints:** unchanged background/positions except the stated change; no new objects, people, damage, text, borders, or watermarks.

Do not ask for several unrelated pose changes in one frame. Do not solve a weak composition by moving a landmark that the scene has already locked.

## 6. Frame-plan fields

The visual plan must include at least:

- `moment_id`, `scene_id`, `setup_id`, `narration_text`
- `establishing_master`, `previous_approved_frame`, `reference_files`
- `camera`, `nolan_state`, `lena_state`, `background_state`, `prop_state`, `lighting_state`
- `intended_change`, `continuity_risk`, `approval_status`

If any state is not applicable, mark it explicitly rather than leaving its meaning ambiguous.

## 7. Review in sequence, not only as isolated images

Every batch receives two reviews:

1. **Single-frame review:** identity, eyes, expression, anatomy, colour, readability, unwanted objects/text.
2. **Sequence review:** play or contact-sheet the adjacent approved frames in narration order and check movement, screen direction, landmark placement, prop continuity, and lighting.

A frame that passes alone but breaks the sequence is rejected. Any corrected frame must be re-checked against both its predecessor and successor, not only against the original rejection note.

## 8. Pilot gate

The 30–45 second opening pilot must pass this sequence review before full production. Its purpose is to test the finished combination of expressive art, Andrew at 0%, actual word timing, pacing, and spatial continuity. Approval of isolated style candidates will not be treated as approval of continuity.
