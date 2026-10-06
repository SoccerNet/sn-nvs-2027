# Evaluation — local 2026-style PSNR check

The local [psnr.py](psnr.py) checks render filenames and dimensions, computes per-image PSNR using the 2026 baseline formula, and averages per-image values within each scene. It is a development check, **not yet the official 2027 CodaBench scorer**.

The organizers confirmed the [2026 NVS task](https://github.com/SoccerNet/sn-nvs#evaluation) metric for 2027: **PSNR on 2048 × 1080 rendered views**. In 2026, SSIM and LPIPS were supplementary and submissions used `scene-*-challenge/renders/*.png`. The exact prior scoring implementation and aggregation order are being recovered; the new simulator's target-view list, masks (if any) and filename mapping must be frozen before a scorer can be called final.

The per-image formula and per-scene averaging follow the [Triangle Splatting baseline `metrics.py`](https://github.com/trianglesplatting/triangle-splatting/blob/685ff270a8273afc3a2b094ae3148dd0b98e31e9/metrics.py) and [PSNR helper](https://github.com/trianglesplatting/triangle-splatting/blob/685ff270a8273afc3a2b094ae3148dd0b98e31e9/utils/image_utils.py). The [Convex Splatting baseline](https://github.com/convexsplatting/convex-splatting/blob/27f83f8b6fbeecef98530e6b56dbd76b73760685/metrics.py) uses the same calculation. These baseline scripts do not reveal how the ULiege CodaBench node combines multiple scenes; the local script intentionally reports each scene separately.

## Local use

Install `numpy` and `Pillow`. Put private reference target views and predicted PNGs in matching scene folders:

```text
reference/scene-1-challenge/renders/00000.png
predictions/scene-1-challenge/renders/00000.png
```

Then run `python3 evaluation/psnr.py --reference /path/to/reference --predictions /path/to/predictions`. The script requires exact scene/image-name coverage and 2048 × 1080 RGB(A) images. Ground-truth target views stay outside this Git repository.

## Required decisions

- Confirm supplied cameras, calibration, target views and timestamps.
- Specify scene-specific training versus generalization to unseen scenes.
- Freeze target resolution, color space, image format and filename mapping.
- Choose primary metric and aggregation across frames, views and scenes.
- Decide foreground masking, temporal evaluation and compute restrictions.

## Planned deliverables

Recover the ULiege 2026 CodaBench scoring program, confirm cross-scene aggregation and any color/mask preprocessing, and validate the local check against its output. Then add the final 2027 scene manifest, baseline renders and score, and an organizer-only CodaBench reference package. Use the same [train/valid/test/challenge layout](../data/README.md) as the other 2027 repositories, with public target-view IDs but no challenge target images in Git. Earlier-edition scores remain background only.

See [baseline references](../baselines/README.md) and [draft rules](../docs/rules.md).
