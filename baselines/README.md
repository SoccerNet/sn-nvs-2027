# NVS baseline methods

The [SoccerNet NVS 2026 kit](https://github.com/SoccerNet/sn-nvs) describes the earlier challenge and links its 3D Gaussian and Triangle Splatting baselines. [Triangle Splatting](https://github.com/trianglesplatting/triangle-splatting) provides a training, rendering, and evaluation implementation. Its documented commands for a scene in its input format are:

```bash
python train.py -s <scene_directory> -m <model_directory> --eval
python render.py -m <model_directory>
python metrics.py -m <model_directory>
```

Download the [SN-NVS-2027 dataset](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027) with `hf download SoccerNet/SN-NVS-2027 --repo-type dataset --local-dir ./SN-NVS-2027`. Follow Triangle Splatting's environment and scene-format instructions, using the cameras and views allowed by the [challenge rules](../RULES.md). The [evaluation guide](../evaluation/README.md) documents the metric script's render layout and the local PSNR check. Conference citations for Convex, Triangle, and Mesh Splatting are in the [main README](../README.md#citation).
