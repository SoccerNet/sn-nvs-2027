# NVS baseline methods

[Triangle Splatting](https://github.com/trianglesplatting/triangle-splatting) is the reference implementation for training a scene representation, rendering camera views, and computing image metrics. The [2026 SoccerNet NVS kit](https://github.com/SoccerNet/sn-nvs) also documents its 3D Gaussian and Triangle Splatting baselines and provides a [challenge-view renderer](https://github.com/SoccerNet/sn-nvs/blob/main/render_challenge.py) for both methods. Conference citations for Triangle, Convex, and Mesh Splatting are in the [main README](../README.md#citation).

Download the [SN-NVS-2027 dataset](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027):

```bash
hf download SoccerNet/SN-NVS-2027 --repo-type dataset --local-dir ./SN-NVS-2027
```

The Triangle Splatting authors document Python 3.11 and CUDA 12.6. Clone its submodules and install its environment and CUDA extensions:

```bash
git clone https://github.com/trianglesplatting/triangle-splatting --recursive
cd triangle-splatting
git checkout 685ff270a8273afc3a2b094ae3148dd0b98e31e9
git submodule update --init --recursive
micromamba create -f requirements.yaml
micromamba activate triangle_splatting
bash compile.sh
cd submodules/simple-knn
pip install .
cd ../..
```

Triangle Splatting accepts a COLMAP-style scene: observed images under `images/` (or a selected image directory) and camera/reconstruction files under `sparse/0/`. Convert each scene to that format while keeping the supplied camera poses and using only observed RGB images for training. Then train one model per scene:

```bash
python train.py -s <scene_directory> -m <model_directory> --eval
```

For outdoor scenes, Triangle Splatting also documents the optional `--outdoor` training flag.

For a local split with known target images, render and measure the model:

```bash
python render.py -m <model_directory>
python metrics.py -m <model_directory>
```

`render.py` writes images under `test/<method>/renders/` and corresponding local reference images under `test/<method>/gt/`. The [evaluation guide](../evaluation/README.md) can run Triangle Splatting's metric script over one or more such scene models. For the challenge views, render from the supplied target cameras without using their withheld RGB images; the [2026 challenge-view renderer](https://github.com/SoccerNet/sn-nvs/blob/main/render_challenge.py) illustrates that separation. Save renders using the scene and view identifiers supplied by the 2027 dataset at **2048 × 1080**.
