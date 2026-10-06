# Data

Download the scene data from [SoccerNet/SN-NVS-2027](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027):

```bash
hf download SoccerNet/SN-NVS-2027 --repo-type dataset --local-dir ./SN-NVS-2027
```

The challenge uses calibrated camera observations from a more realistic simulator with fewer input cameras than the previous edition. Evaluation target images are withheld. See the [evaluation guide](../evaluation/README.md) for render matching and PSNR.
