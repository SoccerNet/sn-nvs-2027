# SoccerNet Challenge 2027 — Novel View Synthesis (NVS)

📢 **Novel View Synthesis (NVS) Challenge!** 🚀

📅 **Submission deadline:** April 25, 2027, 23:59 Anywhere on Earth (AoE; UTC−12).\
👥 **Task leads:** Renaud Vandeghen, [Giulia Martinelli](https://giuli13.github.io/), and [Niccoló Bisagno](https://scholar.google.com/citations?user=I6vOrqkAAAAJ&hl=it&oi=ao)

🏠 [Challenge website](https://www.soccer-net.org/challenges/2027) · 🗂️ [Data on Hugging Face](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027) · 💻 [Baseline](baselines/README.md) · 📚 [Rules](RULES.md) · 📊 [Evaluation](evaluation/README.md) · 📊 [Evaluation Server](https://www.codabench.org/competitions/18448/)

## Task

Given calibrated images from a limited set of cameras, render each soccer scene from the supplied target camera viewpoints. The 2027 scenes come from a more realistic simulator and provide fewer input cameras than [SoccerNet NVS 2026](https://github.com/SoccerNet/sn-nvs). The target images are withheld; submitted RGB renders are evaluated at **2048 × 1080** using PSNR.

## Data

Get the scene data from [SN-NVS-2027](https://huggingface.co/datasets/SoccerNet/SN-NVS-2027). The [data guide](data/README.md) describes the repository's role and the separation between released inputs and evaluation target images.

## Baseline

The [baseline guide](baselines/README.md) gives a complete setup and scene workflow for [Triangle Splatting](https://github.com/trianglesplatting/triangle-splatting), including training, rendering, and local metrics. It also links the previous SoccerNet NVS kit for its challenge-view renderer. The method references are cited below.

## Evaluation

The [evaluation guide](evaluation/README.md) provides a launcher for Triangle Splatting's metric script and a local PSNR calculation with image and filename validation. The ranking metric is PSNR.

## Codabench

For the challenge submission, we use Codabench as the submission platform. You can find the challenge page here: https://www.codabench.org/competitions/18448/.

For the challenge submission, participants should use the provided `render_challenge.py` script (equivalent to render.py from 3DGS). To use it, you need to specify the model path you used during training, but you need to specify the challenge scene path. An example can be found below, using the 3DGS method:

```bash
conda activate gaussian_splatting
python render_challenge.py 3dgs -s <path_to_challenge_scene> -m <path_to_trained_model> -i images -r 1
```
Depending on the method you use, you may need to change the render function. You can also directly copy and modify the `render_challenge.py` script to your own repository to fit your method.


The participants need to submit their results in a zip file with the following structure:

```
├── scene-1-challenge/
│   ├── renders/
│   │   ├── 000000.png
│   │   ├── 000001.png
│   │   └── ...
├── scene-2-challenge/
│   ├── renders/
│   │   ├── 000000.png
│   │   ├── 000001.png
│   │   └── ...
```

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
