# Data

The [SoccerNet/SN-NVS-2027 dataset repository](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027) has been created as a **private, empty placeholder**. The 2027 content, access conditions and split manifests are pending. Do not assume earlier-edition data is the official 2027 release.

The new release will use a more realistic simulator and fewer cameras than 2026. The exact camera count, calibration files, scene list, target-view poses and train/valid/test/challenge split boundaries are pending. The 2026 [scene/renders ZIP layout](https://github.com/SoccerNet/sn-nvs#codabench) is a useful submission reference, but 2027 filenames must be frozen from the new dataset.

See [the explicit split layout](../data/README.md).

## Release requirements

Before opening submissions, freeze the release version, stable sample IDs, split boundaries and public versus private fields. Verify that final-ranking labels have not already been released. Keep ground truth outside public Git history.
