# Opening Pilot — User Approval and Reuse Lock

Date: 2026-10-24

The user approved the assembled opening after the corrected Kaggle run: **“the opening is good now lets continue.”**

## Locked assets

- P001–P012 remain the accepted native 1376×768 opening frames and must not be regenerated or replaced during continuation.
- The opening remains the measured first paragraph of the single full Part 1 `en-US-AndrewNeural` master take at normal `+0%`.
- The successful pre-fix Kaggle log reported a 5:27 full master and a 32.500-second measured opening. Commit `2d93259` corrected only the opening-video trim; it did not change the narration or approved frames.
- Opening cuts remain hard cuts at the actual WordBoundary-derived moments, with no captions or Ken Burns motion.

## Continuation rule

Continue from paragraph 2 with P013 onward. Do not use `FORCE_TTS`; reuse the approved master narration and its saved word timings. In the existing Kaggle session, the normal runner already reuses that cache.

The exact master audio/timing currently exists only in the Kaggle output. Before a fresh-session or independent full-episode build, export and retain `STORE_OPENING_PILOT_DELIVERABLE.zip` (at minimum `production/master/narration.mp3`, `beats_with_timing.json`, `moments_timing.json` and `narration.log`). Do not silently record a replacement opening.
