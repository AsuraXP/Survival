# COLD SURVIVAL — Episode 1 (project folder)

Animated story-video project, produced under the SWARM SPEC v5.0 state machine.

- **Slug:** `cold_survival`
- **Series:** *Cold Survival* — Episode 1 of an ongoing story series
- **Platform:** YouTube, 16:9, no burned captions
- **Voice:** `en-US-AndrewNeural` @ `+10%` rate (Edge-TTS, runs on Kaggle only)
- **POV:** second person ("you wake up cold…")
- **Art style:** hand-drawn ink linework + loose watercolor wash on aged cream paper (see `refs/style_ref_source.jpg`)

## Folder map

| Path | Purpose |
|---|---|
| `brief.md` | Locked production brief (STATE 1) |
| `script.md` | Plain-text narration (STATE 2) |
| `visuals.csv` | The spine: word-reactive micro-beat frame rows (STATE 3) |
| `refs/` | Art-style & character inspiration ONLY (never spatial templates) |
| `continuity.md` | Locked anchor prompts + verbatim style/character invariants (STATE 4) |
| `frames/` | Accepted frames `beat{slide:02d}m{moment:02d}.png` (STATE 5) |
| `metadata.json` | Machine-readable project metadata |
| `youtube.txt` | Title / description / tags draft |
| `STATE.md` | State-machine log |

Repo root holds `run_cold_survival_kaggle.sh` (STATE 6) — the ONLY place TTS, audio mix and FFmpeg encode happen is Kaggle. This workspace never produces audio.
