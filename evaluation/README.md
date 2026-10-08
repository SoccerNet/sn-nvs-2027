# NVS evaluation

The ranking metric is **PSNR** on 2048 × 1080 target views. PSNR is computed from RGB values in `[0, 1]` as `10 log10(1 / MSE)` in decibels. The reference implementation is [Triangle Splatting `metrics.py`](https://github.com/trianglesplatting/triangle-splatting/blob/685ff270a8273afc3a2b094ae3148dd0b98e31e9/metrics.py), which computes per-image PSNR, SSIM, and LPIPS using PyTorch/CUDA and averages each metric over images within a scene. The [launcher](run_triangle_metrics.py) invokes that implementation. Pin Triangle Splatting to commit `685ff270a8273afc3a2b094ae3148dd0b98e31e9` for the linked version.

Prepare matching image names in each scene model directory:

```text
<model>/test/<method>/renders/00000.png
<model>/test/<method>/gt/00000.png
```

In Triangle Splatting's environment, run from this repository root. Repeat `--model-path` for additional scenes:

```bash
python evaluation/run_triangle_metrics.py --triangle-repo /path/to/triangle-splatting --model-path /path/to/scene-model
```

It writes `results.json` and `per_view.json` in each model directory. These local metrics require reference images, so they apply to development views with known RGB images. Challenge reference images stay in the scoring environment.

The local [psnr.py](psnr.py) provides a CPU check of PNG names, dimensions, and per-scene mean PSNR. Install `numpy` and `Pillow`; arrange matching `scene/renders/*.png` files under two roots and run:

```bash
python evaluation/psnr.py --reference /path/to/reference --predictions /path/to/predictions
```

The CPU script rejects missing or extra scenes, mismatched PNG names, and images that are not 2048 × 1080. It reports one PSNR value per scene; the full challenge score is determined by the evaluation server. Keep evaluation target images separate from the participant repository.
