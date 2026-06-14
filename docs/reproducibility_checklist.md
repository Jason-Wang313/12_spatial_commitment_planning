# Reproducibility Checklist

- [x] Main experiment can be rerun with `python scripts/run_experiments.py`.
- [x] Stable wrapper dispatches to `experiments/full_scale_spatial_commitment.py`.
- [x] Generated full-scale result files are under `results/full_scale/`.
- [x] `results/full_scale/progress.json` reports `stage` as `complete`.
- [x] Generated figures include scaling, topology, certificate, recovery, geometry, and ablation plots in both PDF and PNG forms.
- [x] Generated tables include main scaling, topology, certificate stress, recovery stress, geometry proxy, ablation, runtime/memory, and claim evidence.
- [x] Edited Python files pass `python -m py_compile`.
- [x] Manuscript builds with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` from `paper/`.
- [x] Local final-build PDF is 25 pages before canonical copy.
- [x] Canonical PDF target is `C:/Users/wangz/Downloads/12.pdf`.
- [x] No new Desktop PDF copy is created in the v3 hardening pass.
- [ ] Dependency versions are pinned.
- [ ] Hardware data exists.
- [ ] Full continuous cut-extraction implementation exists.
