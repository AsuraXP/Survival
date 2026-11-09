# STATE — long_cold_video

| Step | State | Notes |
|---|---|---|
| 0 | DONE | Repo `AsuraXP/Survival` inspected: empty apart from `README.md`. No existing pipeline scripts; patterns established here. |
| 0.5 | DONE | No existing project folders found → clean project created. |
| 1 | DONE | Brief captured: freeze premise, 10 min, 2nd person, 16:9, no captions, AndrewNeural +10%. |
| 2 | DONE (approved) | `script.md`, 1876 words, 10:05 projected. |
| 3 | DONE | `visuals.csv` — 289 rows, 46 slides, avg 6.49 words/row (~2.1 s/frame), text stream byte-identical to `script.md`. No frame budget was chosen up front. |
| 4 | **ANCHORS GENERATED — AWAITING APPROVAL** | 3 style tests in `refs/`, prompts logged in `continuity.md`. Worker split: W1 slides 01-15 (97 frames), W2 16-31 (96), W3 32-46 (96). |
| 5 | PENDING | Swarm frame generation (worker chats). |
| 5.1 | PENDING | Merge worker branches. |
| 5.5 | PENDING | `thumbnail.jpg`. |
| 6 | PENDING | `run_long_cold_kaggle.sh`. |
| 7 | PENDING | Kaggle handoff cell. |

## Declared exceptions
_(none yet)_

## Compliance log
- No audio, TTS, voice auditioning, or FFmpeg executed in this workspace. Kaggle is the only audio environment.
