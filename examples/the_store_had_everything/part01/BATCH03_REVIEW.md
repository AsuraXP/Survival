# Part 1 Continuation — Batch 3 Review (P013–P018)

Status: all six active frames passed assistant per-image and adjacent-sequence QA on 2026-10-24. Opening P001–P012 is user-approved and unchanged.

## Narration coverage

> “Turn it off,” Lena whispered. “Working on it,” Nolan said. He had a store key, a box cutter, and no plan beyond reaching that door. Lena had the keys to her delivery van in the loading bay. Neither of them knew whether the van was a better bet than the building. They knew only that the glass could not take another hour of this.

The six manifest rows reproduce approved Part 1 paragraph 2 exactly. Actual timing will be derived from the existing full-master WordBoundary events.

## Frame dispositions

| Frame | Result | Review note |
|---|---|---|
| P013 | Accepted | Crossing resumes toward screen-right/office; Lena whispers while following; black braid and anatomical-right-hand keys preserved; Nolan has three strokes. |
| P014 | Accepted after correction | Initial version omitted Nolan's hair strokes and was rejected. Corrected response preserves the speaker change, route, identities and key hand. |
| P015 | Accepted after correction | Initial version put Lena on the wrong side and was rejected. Nolan-only objective insert preserves offscreen following blocking; store key, retracted box cutter, blank badge and office goal are readable. |
| P016 | Accepted after correction | Initial version put keys in Lena's left hand and was rejected. Corrected keys hang on viewer-left beside the right-side braid; no van teleport or radio. |
| P017 | Accepted | Two-shot uncertainty without destination change. Nolan's key/box cutter and Lena's keys remain; enlarged review confirmed exactly three hair strokes. |
| P018 | Accepted | Crowd remains outside intact glass; no cracks, breach, infected inside or premature shutter descent. |

All rejected candidates are isolated under `part01/rejected/` and are not active references.

## Sequence review

- P012's exterior/crowd angle cuts back to the established P010 crossing direction in P013; no character position reset occurs.
- P013 → P014 changes the speaker and expression while retaining lead/follow order and continuous motion.
- P015 and P016 are single-character inserts; the offscreen character retains the established route rather than being silently moved.
- P017 restores the two-shot with Nolan ahead and Lena behind. Neither chooses the van yet.
- P018 is a threat cutaway only; it does not advance the shutter, glass damage or office entry.
- All six active frames are native 1376×768. Every listed reference exists and no rejected path is listed.

## Deferred production dependency

The existing Kaggle master narration and saved word timings will be reused for the final full Part 1 build. Per the user's latest instruction, no intermediate paragraph-2 video run is requested. Do not enable `FORCE_TTS`. The final run script will be delivered only after every Part 1 frame is finished; a fresh-session build will require the exported approved master assets described in `opening_pilot/APPROVAL.md`.
