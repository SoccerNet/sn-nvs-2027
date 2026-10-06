# SoccerNet Challenge 2027 — Novel View Synthesis (NVS)

📢 **Novel View Synthesis (NVS) Challenge!** 🚀

📅 **Submission deadline:** April 25, 2027, 23:59 Anywhere on Earth (AoE; UTC−12).\
👥 **Task leads:** Renaud Vandeghen, Giulia Martinelli, and Niccolo Bisagno

🏠 [Challenge website](https://www.soccer-net.org/challenges/2027) · 🗂️ [Data on Hugging Face](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027) · 💻 [Baseline](baselines/README.md) · 📚 [Rules](RULES.md) · 📊 [Evaluation](evaluation/README.md)

## Task

Synthesize target views of soccer scenes from calibrated camera observations. This edition uses a more realistic simulator and fewer input cameras than [SoccerNet NVS 2026](https://github.com/SoccerNet/sn-nvs). Rendered views are evaluated at **2048 × 1080** using PSNR.

## Data

Get the scene data from [SN-NVS-2027](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027). The [data guide](data/README.md) describes the repository's role and the separation between released inputs and evaluation target images.

## Baseline

The [baseline guide](baselines/README.md) links the previous SoccerNet NVS kit and the [Triangle Splatting implementation](https://github.com/trianglesplatting/triangle-splatting), with its training, rendering, and metric commands. The method references are cited below.

## Evaluation

The [evaluation guide](evaluation/README.md) provides a launcher for Triangle Splatting's metric script and a local PSNR calculation with image and filename validation. The ranking metric is PSNR.

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

## Community

Follow the [SoccerNet challenge website](https://www.soccer-net.org/challenges/2027) and [Discord](https://discord.gg/cPbqf2mAwF) for challenge announcements and discussion.
