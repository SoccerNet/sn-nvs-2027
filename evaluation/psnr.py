"""Local PSNR check for SoccerNet NVS renders.

Matches the per-image formula and per-scene averaging in the Triangle
Splatting baseline.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np
from PIL import Image


def psnr_pair(reference: Path, prediction: Path, expected_size=(2048, 1080)) -> float:
    with Image.open(reference) as gt_image, Image.open(prediction) as render_image:
        if gt_image.size != expected_size or render_image.size != expected_size:
            raise ValueError(f"Expected {expected_size[0]}x{expected_size[1]} images")
        if gt_image.mode not in ("RGB", "RGBA") or render_image.mode not in ("RGB", "RGBA"):
            raise ValueError("Expected RGB or RGBA PNG images")
        gt = np.asarray(gt_image.convert("RGB"), dtype=np.float64) / 255.0
        render = np.asarray(render_image.convert("RGB"), dtype=np.float64) / 255.0
    mse = float(np.mean((gt - render) ** 2))
    return math.inf if mse == 0 else 20.0 * math.log10(1.0 / math.sqrt(mse))


def evaluate(reference_root: Path, prediction_root: Path, expected_size=(2048, 1080)):
    """Return per-scene mean PSNR."""
    scenes = sorted(p.name for p in reference_root.iterdir() if p.is_dir() and (p / "renders").is_dir())
    if not scenes:
        raise ValueError("No reference scene/renders directories found")
    if {p.name for p in prediction_root.iterdir() if p.is_dir()} != set(scenes):
        raise ValueError("Prediction scene directories must match the reference exactly")
    result = {}
    for scene in scenes:
        ref_files = {p.name: p for p in (reference_root / scene / "renders").glob("*.png")}
        pred_files = {p.name: p for p in (prediction_root / scene / "renders").glob("*.png")}
        if not ref_files or set(ref_files) != set(pred_files):
            raise ValueError(f"Missing, extra, or empty renders for {scene}")
        scores = [psnr_pair(ref_files[name], pred_files[name], expected_size) for name in sorted(ref_files)]
        result[scene] = sum(scores) / len(scores)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--predictions", type=Path, required=True)
    parser.add_argument("--width", type=int, default=2048)
    parser.add_argument("--height", type=int, default=1080)
    args = parser.parse_args()
    per_scene = evaluate(args.reference, args.predictions, (args.width, args.height))
    for scene, value in per_scene.items():
        print(f"{scene}: {value:.6f} dB")


if __name__ == "__main__":
    main()
