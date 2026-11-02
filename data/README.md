# Data

The dataset contains 5 scenes generated with the Blender game engine, featuring different soccer actions. Each scene is divided in 2 different sets: train and challenge. The train set includes broacasted images and camera parameters using COLMAP with known poses. For the challenge set, only the poses of the novel views are provided, but not the ground truth images. However, for the sake of compatibility with existing NVS methods, we provide dummy images (black images) in the challenge set.

The dataset follow the structure below:
```
SoccerNet-NVS/
├── scene-1/
│   ├── images/
│   └── sparse/
│       └── 0/
│           ├── cameras.bin
│           ├── images.bin
│           ├── points3D.bin
│           └── points3D.ply
├── scene-2/
```
Note that the original images/ have a 4K resolution (4096x2160), but the evaluation will be performed at a resolution of 2048x1080.

Download the scene data from [SoccerNet/SN-NVS-2027](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027):

```bash
hf download SoccerNet/SN-NVS-2027 --repo-type dataset --local-dir ./SN-NVS-2027
```

Each scene supplies the camera observations and calibration needed for reconstruction, together with the camera viewpoints to render. The 2027 scenes use a more realistic simulator and fewer input cameras than the [2026 NVS dataset](https://huggingface.co/datasets/SoccerNet/SN-NVS-2026). Evaluation target RGB images are withheld. Preserve the supplied scene and target-view identifiers when exporting renders; the [evaluation guide](../evaluation/README.md) explains how image names and dimensions are checked.
