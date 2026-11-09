# STATE — long_cold_video

| Step | State | Notes |
|---|---|---|
| 0 | DONE | Repo `AsuraXP/Survival` inspected: empty apart from `README.md`. No existing pipeline scripts; patterns established here. |
| 0.5 | DONE | No existing project folders found → clean project created. |
| 1 | DONE | Brief captured: freeze premise, 10 min, 2nd person, 16:9, no captions, AndrewNeural +10%. |
| 2 | DONE (approved) | `script.md`, 1876 words, 10:05 projected. |
| 3 | DONE | `visuals.csv` — 289 rows, 46 slides, avg 6.49 words/row (~2.1 s/frame), text stream byte-identical to `script.md`. No frame budget was chosen up front. |
| 4 | DONE | Style relocked to the user's reference (v3). v1 and v2 looks REJECTED and archived. 3 anchors approved. Canonical prompt prefix + reference image conditioning logged in `continuity.md`. |
| 5 | **IN PROGRESS — 6/289** | Batch 01 generated. 1 defect (beat01m02 drew a ONE-EYED face) → row prompt rewritten + FACE RULE added to `continuity.md`, re-rolled, now passes. Repair budget for batch 01: 1/2 used. |
| 5.1 | PENDING | Merge worker branches. |
| 5.5 | PENDING | `thumbnail.jpg`. |
| 6 | PENDING | `run_long_cold_kaggle.sh`. |
| 7 | PENDING | Kaggle handoff cell. |

## Declared exceptions
_(none yet)_

## Repairs
- **beat01m02** — defect: character rendered with a single eye. Cause: row prompt literally said "one open eye". Fix: framing clause rewritten to a two-eye face crop, prefix hardened with "EXACTLY TWO ... never one eye", FACE RULE added to `continuity.md`. Re-roll passed 1/3.

## Compliance log
- No audio, TTS, voice auditioning, or FFmpeg executed in this workspace. Kaggle is the only audio environment.
