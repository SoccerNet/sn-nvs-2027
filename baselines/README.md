# Baseline

Prior-edition NVS code, provided as background. Its data, image resolution, rendering format and scoring protocol have not been adopted for 2027. The 2027 baseline and compatible version will be announced by the task leads.

Repository: [https://github.com/SoccerNet/sn-nvs](https://github.com/SoccerNet/sn-nvs).

For 2027, [Triangle Splatting](https://github.com/trianglesplatting/triangle-splatting) is the reference implementation to adapt. After cloning it and following its environment setup, its [documented run sequence](https://github.com/trianglesplatting/triangle-splatting#running) is:

```bash
python train.py -s <scene_directory> -m <model_directory> --eval
python render.py -m <model_directory>
python metrics.py -m <model_directory>
```

Request access to [SN-NVS-2027](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027) when available; it is currently a private, empty placeholder. Download it with `hf download SoccerNet/SN-NVS-2027 --repo-type dataset --local-dir ./SN-NVS-2027`. Map the released calibrated scene/camera layout to Triangle Splatting's input format and render only the published target views. The reduced-camera protocol and data converter are pending. The [evaluation guide](../evaluation/README.md) explains metric inputs.

The 2026 repository links to 3D Gaussian and Triangle Splatting baselines, plus its view-rendering submission helper. The 2027 baseline method and prediction renders are TBD; none of those prior outputs is presented here as a 2027 result. The relevant conference citations for Convex, Triangle and Mesh Splatting are in [README.md#citation](../README.md#citation).

Before the challenge release, record a tested commit or tag, environment, weights, inference command, output conversion, expected scores and compute requirements. External code remains in its upstream repository and under its own license.
