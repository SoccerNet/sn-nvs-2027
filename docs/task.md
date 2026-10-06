# Novel View Synthesis task specification

Status: draft; technical choices below are not final rules.

The 2027 data will come from a more realistic simulator with fewer cameras than [SN-NVS-2026](https://github.com/SoccerNet/sn-nvs). As in 2026, the main ranking metric is PSNR computed on 2048 × 1080 rendered views. SSIM and LPIPS may be reported as supplementary measures, as they were in 2026; confirm their exact role before launch.

Can AI show the game from a new perspective? This challenge explores the generation of unseen viewpoints from football footage. Participants will develop methods to reconstruct the scene and render new views of players and the pitch, opening possibilities for immersive viewing and match analysis.

## Decisions before launch

- [ ] Confirm supplied cameras, calibration, target views and timestamps.
- [ ] Specify scene-specific training versus generalization to unseen scenes.
- [ ] Freeze target resolution, color space, image format and filename mapping.
- [x] Primary metric: PSNR at 2048 × 1080, as in 2026.
- [ ] Recover the 2026 scorer and confirm aggregation across frames, views and scenes; verify whether SSIM/LPIPS will still be reported.
- [ ] Decide foreground masking, temporal evaluation and compute restrictions.
