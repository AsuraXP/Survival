# STATE — long_cold_video

| Step | State | Notes |
|---|---|---|
| 0 | DONE | Repo `AsuraXP/Survival` inspected: empty apart from `README.md`. No existing pipeline scripts; patterns established here. |
| 0.5 | DONE | No existing project folders found → clean project created. |
| 1 | DONE | Brief captured: freeze premise, 10 min, 2nd person, 16:9, no captions, AndrewNeural +10%. |
| 2 | DONE (approved) | `script.md`, 1876 words, 10:05 projected. |
| 3 | DONE | `visuals.csv` — 289 rows, 46 slides, avg 6.49 words/row (~2.1 s/frame), text stream byte-identical to `script.md`. No frame budget was chosen up front. |
| 4 | DONE | Style relocked to the user's reference (v3). v1 and v2 looks REJECTED and archived. 3 anchors approved. Canonical prompt prefix + reference image conditioning logged in `continuity.md`. |
| 5 | **IN PROGRESS — 12/289** | Master batch 01: 6/6 (`beat01m01`–`beat01m06`). Worker 2 batch 01: data rows 98–103, 6/6 (`beat16m01`–`beat17m01`); contact sheet saved. Two repairs used (one clause each); initial rejected frames preserved under `rejects/`. |
| 5.1 | PENDING | Merge worker branches. |
| 5.5 | PENDING | `thumbnail.jpg`. |
| 6 | PENDING | `run_long_cold_kaggle.sh`. |
| 7 | PENDING | Kaggle handoff cell. |

## Declared exceptions
_(none yet)_

## Repairs
- **beat01m02** — defect: character rendered with a single eye. Cause: row prompt literally said "one open eye". Fix: framing clause rewritten to a two-eye face crop, prefix hardened with "EXACTLY TWO ... never one eye", FACE RULE added to `continuity.md`. Re-roll passed 1/3.
- **beat16m04** — first render clipped the survivor's face. Re-rolled with the full head and both eyes visible (one framing-clause change); rejected original preserved at `rejects/beat16m04_r0.png`.
- **beat17m01** — first render included a partial face obscured by a sock. Re-rolled with the crop limited to hands and lower leg (one framing-clause change); rejected original preserved at `rejects/beat17m01_r0.png`.

## Compliance log
- No audio, TTS, voice auditioning, or FFmpeg executed in this workspace. Kaggle is the only audio environment.
