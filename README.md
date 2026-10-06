# SoccerNet Challenge 2027 — Novel View Synthesis (NVS)

📢 **Novel View Synthesis (NVS) Challenge!** 🚀

⏳ **Status:** In preparation — submissions are not open.\
📅 **Submission deadline:** April 25, 2027, 23:59 Anywhere on Earth (AoE; UTC−12).\
👥 **Task leads:** Renaud Vandeghen, Giulia Martinelli, and Niccolo Bisagno\
🤝 **Sponsor:** To be announced

🏠 [Challenge website](https://www.soccer-net.org/challenges/2027) · 🗂️ [Data on Hugging Face](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027) · 💻 [Baseline](baselines/README.md) · 📚 [Rules](RULES.md) · 📊 [Evaluation](evaluation/README.md) · 🏆 [Evaluation server](https://www.codabench.org/) (task URL TBD)

## Task

Synthesize unseen views of soccer scenes from calibrated camera observations. The 2027 data will come from a **more realistic simulator with fewer cameras** than the 2026 edition, increasing the challenge of reconstruction from sparse views. As in [SoccerNet NVS 2026](https://github.com/SoccerNet/sn-nvs), the ranking metric is PSNR on 2048 × 1080 target images.

## Data

The [SN-NVS-2027 Hugging Face repository](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027) exists as a **private, empty placeholder**. Scene lists, cameras, poses, target-view IDs, and train/valid/test/challenge boundaries are not yet released. The [split inventory](data/README.md) will track the release. Challenge target images must remain in the organizer reference package, outside this Git repository.

## Baseline

The [baseline folder](baselines/README.md) links the previous [SoccerNet NVS kit](https://github.com/SoccerNet/sn-nvs) and the [Triangle Splatting implementation](https://github.com/trianglesplatting/triangle-splatting). It gives the Hugging Face download and run sequence. A 2027-compatible checkpoint and rendered prediction set are still pending.

## Evaluation

The [evaluation folder](evaluation/README.md) includes a launcher for Triangle Splatting's `metrics.py` and a local PSNR parity check. The primary metric is confirmed, but the ULiege CodaBench node's exact cross-scene aggregation and the new target-view mapping still need validation. The task evaluation server is TBD.

## Citation

Cite the methods used. The conference versions for Convex Splatting, Triangle Splatting, and MeshSplatting are:

```bibtext
@InProceedings{Held_2025_CVPR,
  author = {Held, Jan and Vandeghen, Renaud and Hamdi, Abdullah and Deliege, Adrien and Cioppa, Anthony and Giancola, Silvio and Vedaldi, Andrea and Ghanem, Bernard and Van Droogenbroeck, Marc},
  title = {3D Convex Splatting: Radiance Field Rendering with 3D Smooth Convexes},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  month = {June},
  year = {2025},
  pages = {21360--21369},
  url = {https://openaccess.thecvf.com/content/CVPR2025/html/Held_3D_Convex_Splatting_Radiance_Field_Rendering_with_3D_Smooth_Convexes_CVPR_2025_paper.html}
}

@InProceedings{Held_2026_3DV,
  author = {Held, Jan and Vandeghen, Renaud and Deliege, Adrien and Hamdi, Abdullah and Giancola, Silvio and Rebain, Daniel and Cioppa, Anthony and Ghanem, Bernard and Vedaldi, Andrea and Tagliasacchi, Andrea and Van Droogenbroeck, Marc},
  title = {Triangle Splatting for Real-Time Radiance Field Rendering},
  booktitle = {Proceedings of the International Conference on 3D Vision (3DV)},
  year = {2026},
  pages = {1248--1257},
  doi = {10.1109/3DV69130.2026.00123},
  url = {https://doi.org/10.1109/3DV69130.2026.00123}
}

@InProceedings{Held_2026_CVPR,
  author = {Held, Jan and Son, Sanghyun and Vandeghen, Renaud and Rebain, Daniel and Gadelha, Matheus and Zhou, Yi and Cioppa, Anthony and Lin, Ming C. and Van Droogenbroeck, Marc and Tagliasacchi, Andrea},
  title = {MeshSplatting: Differentiable Rendering with Opaque Meshes},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  month = {June},
  year = {2026},
  pages = {7320--7329},
  url = {https://openaccess.thecvf.com/content/CVPR2026/html/Held_MeshSplatting_Differentiable_Rendering_with_Opaque_Meshes_CVPR_2026_paper.html}
}
```

## Updates and support

Each task launches independently when ready. Follow the [challenge website](https://www.soccer-net.org/challenges/2027) and [SoccerNet Discord](https://discord.gg/cPbqf2mAwF) for announcements. Use repository issues for reproducible code problems; do not post access tokens or restricted data.

## Release readiness

| Item | Current state |
| --- | --- |
| Task definition | New simulator and fewer cameras confirmed; target-view protocol pending |
| Data | Private Hugging Face placeholder created; dataset and splits pending |
| Baseline | Prior methods linked; 2027 checkpoint and renders pending |
| Evaluation | PSNR at 2048 × 1080 confirmed; Triangle Splatting metric code identified; server adapter pending |
| Benchmark | ULiege-backed CodaBench server TBD |
| Sponsor | TBD |

This section is for preparation and will be removed when this task is ready for release.
