# ESDD-Review

Recent progress in audio generation has made it increasingly easy to create highly realistic environmental soundscapes, which can be misused to produce deceptive content, such as fake alarms, gunshots, and crowd sounds, raising concerns for public safety and trust. While deepfake detection for speech and singing voice has been extensively studied, environmental sound deepfake detection (ESDD) remains underexplored. To advance ESDD, the first edition of the ESDD challenge was launched, attracting 97 registered teams and receiving 1,748 valid submissions. This paper presents the task formulation, dataset construction, evaluation protocols, baseline systems, and key insights from the challenge results. Furthermore, we analyze common architectural choices and training strategies among top-performing systems. Finally, we discuss potential future research directions for ESDD, outlining key opportunities and open problems to guide subsequent studies in this field.

**Paper Link:** https://arxiv.org/abs/2603.04865 


# Run

1. Install the environment: conda env create -f environment.yml

2. Run the evaluation code: python eval.py


# Citation
If you find this work useful, please cite:
```bibtex
@inproceedings{yin2026esdd,
  title     = {The First Environmental Sound Deepfake Detection Challenge: Benchmarking Robustness, Evaluation, and Insights},
  author    = {Han Yin and Yang Xiao and Rohan Kumar Das and Jisheng Bai and Ting Dang},
  booktitle = {Proc. Interspeech 2026},
  year      = {2026},
}
```


