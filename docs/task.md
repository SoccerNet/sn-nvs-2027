# Novel View Synthesis task specification

Status: draft; technical choices below are not final rules.

Can AI show the game from a new perspective? This challenge explores the generation of unseen viewpoints from football footage. Participants will develop methods to reconstruct the scene and render new views of players and the pitch, opening possibilities for immersive viewing and match analysis.

## Decisions before launch

- [ ] Confirm supplied cameras, calibration, target views and timestamps.
- [ ] Specify scene-specific training versus generalization to unseen scenes.
- [ ] Freeze target resolution, color space, image format and filename mapping.
- [ ] Choose primary metric and aggregation across frames, views and scenes.
- [ ] Decide foreground masking, temporal evaluation and compute restrictions.
