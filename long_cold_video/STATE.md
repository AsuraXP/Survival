# STATE — long_cold_video

| Step | State | Notes |
|---|---|---|
| 0 | DONE | Repo `AsuraXP/Survival` inspected: empty apart from `README.md`. No existing pipeline scripts; patterns established here. |
| 0.5 | DONE | No existing project folders found → clean project created. |
| 1 | DONE | Brief captured: freeze premise, 10 min, 2nd person, 16:9, no captions, AndrewNeural +10%. |
| 2 | DONE (approved) | `script.md`, 1876 words, 10:05 projected. |
| 3 | DONE | `visuals.csv` — 289 rows, 46 slides, avg 6.49 words/row (~2.1 s/frame), text stream byte-identical to `script.md`. No frame budget was chosen up front. |
| 4 | DONE | Style relocked to the user's reference (v3). v1 and v2 looks REJECTED and archived. 3 anchors approved. Canonical prompt prefix + reference image conditioning logged in `continuity.md`. |
| 5 | **IN PROGRESS — 6/289** | Batch 01 (slides 01m01-01m06) generated, QC pass, contact sheet `.build/contact_batch01.png`. |
| 5.1 | PENDING | Merge worker branches. |
| 5.5 | PENDING | `thumbnail.jpg`. |
| 6 | PENDING | `run_long_cold_kaggle.sh`. |
| 7 | PENDING | Kaggle handoff cell. |

## Declared exceptions
_(none yet)_

## Compliance log
- No audio, TTS, voice auditioning, or FFmpeg executed in this workspace. Kaggle is the only audio environment.
