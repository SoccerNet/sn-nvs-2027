# Evaluation — awaiting 2027 specification

No official 2027 scorer is released in this repository yet. The task leads must confirm the protocol before implementation.

The organizers confirmed the [2026 NVS task](https://github.com/SoccerNet/sn-nvs#evaluation) metric for 2027: **PSNR on 2048 × 1080 rendered views**. In 2026, SSIM and LPIPS were supplementary and submissions used `scene-*-challenge/renders/*.png`. The exact prior scoring implementation and aggregation order are being recovered; the new simulator's target-view list, masks (if any) and filename mapping must be frozen before a scorer can be called final.

## Required decisions

- Confirm supplied cameras, calibration, target views and timestamps.
- Specify scene-specific training versus generalization to unseen scenes.
- Freeze target resolution, color space, image format and filename mapping.
- Choose primary metric and aggregation across frames, views and scenes.
- Decide foreground masking, temporal evaluation and compute restrictions.

## Planned deliverables

A versioned local scoring command, environment, format example, malformed-submission checks, baseline predictions and score, and CodaBench integration if selected. Use the same [train/valid/test/challenge layout](../data/README.md) as the other 2027 repositories, with public target-view IDs but no challenge target images in Git. Earlier-edition scores and formats are background only.

See [baseline references](../baselines/README.md) and [draft rules](../docs/rules.md).
