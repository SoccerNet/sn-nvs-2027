# Data

Download the scene data from [SoccerNet/SN-NVS-2027](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027):

```bash
hf download SoccerNet/SN-NVS-2027 --repo-type dataset --local-dir ./SN-NVS-2027
```

Each scene supplies the camera observations and calibration needed for reconstruction, together with the camera viewpoints to render. The 2027 scenes use a more realistic simulator and fewer input cameras than the [2026 NVS dataset](https://huggingface.co/datasets/SoccerNet/SN-NVS-2026). Evaluation target RGB images are withheld. Preserve the supplied scene and target-view identifiers when exporting renders; the [evaluation guide](../evaluation/README.md) explains how image names and dimensions are checked.
