# SoccerNet Challenge 2027 — Novel View Synthesis

📢 **Novel View Synthesis Challenge!** 🚀

Can AI show the game from a new perspective? Participants will synthesize target views of football scenes from a **new, more realistic simulator** with **fewer input cameras** than the 2026 edition. The ranking metric follows the 2026 NVS task: PSNR at 2048 × 1080. The exact 2027 scene package and scorer still need validation.

⏳ **Status:** In preparation — submissions are not open.  
📅 **Submission deadline:** April 25, 2027; cutoff time and timezone to be announced.  
👥 **Task lead(s):** ULiège and Nicolo from the University of Trento  
🤝 **Sponsor:** To be announced

🏠 [Challenge website](https://www.soccer-net.org/challenges/2027) / 🗂️ [Private dataset placeholder](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027) / 💻 [Prior baseline repository](https://github.com/SoccerNet/sn-nvs) / 📚 [Rules](docs/rules.md) / 📊 [Evaluation](evaluation/README.md)

## Task

[Task specification and open decisions](docs/task.md) describes the current scope. This repository will hold the versioned evaluation code and submission instructions for the 2027 challenge. Baselines may live here or in an external repository linked below.

## Data

The [SN-NVS-2027 dataset repository](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027) has been created privately as an empty placeholder. Its forthcoming data will use a new simulator and fewer cameras; contents and splits are pending.

See [the data guide](docs/data.md) for release status and split details. Dataset availability does not mean that the challenge is open. Private evaluation labels are not included in this repository.

## Baseline

Prior-edition NVS code, provided as background. Its data, image resolution, rendering format and scoring protocol have not been adopted for 2027. The 2027 baseline and compatible version will be announced by the task leads.

See [baseline instructions](baselines/README.md). Existing research baselines must be checked against the final challenge format before their scores are advertised as 2027 reference results.

## Evaluation

PSNR at 2048 × 1080 is confirmed as the ranking metric, following the 2026 NVS task. A [local per-scene evaluator](evaluation/psnr.py) is included; the exact ULiege CodaBench cross-scene aggregation and target-view list still need verification.

See [evaluation instructions](evaluation/README.md) for current code, submission formats and remaining decisions. CodaBench test and challenge links will be added after the servers have been validated.

## Release readiness

| Item | Current state |
| --- | --- |
| Task definition | New, more realistic simulator with fewer cameras; target protocol still pending |
| Data and splits | Private Hugging Face placeholder created; 2027 contents and splits pending |
| Baseline | Prior code linked; 2027 predictions pending |
| Evaluation | PSNR at 2048 × 1080 confirmed; local per-scene code included; CodaBench aggregation pending |
| Benchmark | CodaBench server pending |
| Sponsor | Not confirmed |

Each task launches independently after its rules, data, baseline, evaluator and benchmark are verified. See the [task specification](docs/task.md) for remaining technical decisions.

## Getting started

1. Read the [task specification](docs/task.md) and [draft rules](docs/rules.md).
2. Follow the [data access guide](docs/data.md).
3. Consult the [baseline instructions](baselines/README.md).
4. Check the [evaluation status](evaluation/README.md) before generating submissions.

## Updates and support

Each task launches independently once ready. Follow the [challenge website](https://www.soccer-net.org/challenges/2027) and [SoccerNet Discord](https://discord.gg/cPbqf2mAwF). Use repository issues for reproducible code problems; do not post access tokens, restricted data or private labels.

## Citation and licensing

Related methods include [3D Convex Splatting (CVPR 2025)](https://openaccess.thecvf.com/content/CVPR2025/html/Held_3D_Convex_Splatting_Radiance_Field_Rendering_with_3D_Smooth_Convexes_CVPR_2025_paper.html), [Triangle Splatting (3DV 2026)](https://doi.org/10.1109/3DV69130.2026.00123), and [MeshSplatting (CVPR 2026)](https://openaccess.thecvf.com/content/CVPR2026/html/Held_MeshSplatting_Differentiable_Rendering_with_Opaque_Meshes_CVPR_2026_paper.html). Cite the methods used with `\cite{Held_2025_CVPR,Held_2026_3DV,Held_2026_CVPR}` as appropriate; conference BibTeX is in [CITATION.bib](CITATION.bib). The 2027 challenge citation and code license will be confirmed before release.
