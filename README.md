# Spatial Commitment Planning

Anonymous ICLR-style mechanism paper package for paper 12 in the robotics batch.

## Reproduce

```powershell
python scripts/run_experiments.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The stable runner dispatches to `experiments/full_scale_spatial_commitment.py` and writes the v3 evidence package under `results/full_scale/`. The final verified PDF target is `C:/Users/wangz/Downloads/12.pdf`; intermediate `paper/main.pdf` builds are local artifacts only and are removed after the final copy.

Current final export: 25 pages, 410,264 bytes, SHA256 `A2E7BE0F3316564429D507F211A6C4479F5BC6614372B327BFAE1A8448866B4B`.

VLA-style boxed-link verification:

- Link annotations: 48 total on pages `[(2, 20), (3, 21), (5, 2), (6, 4), (7, 1)]`.
- Annotation colors: green = 41, red = 7, cyan = 0.
- Border widths: `(0, 0, 1)` for all link annotations.
- Visual audit: rendered pages 2, 3, 5, 6, and 7; green citation/URL boxes and red internal-reference boxes are crisp and aligned.

## Current headline result

Submission-hardening version: v3, dated 2026-06-14.

- Final manuscript build: 25 pages after `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Full-scale scope: six experiment families with 30 seed replicates per setting where applicable.
- Main scaling result at 10 medium zones, pressure 2: SCP success 1.000, exact lifted A* success 1.000, SCP expansions 183.4 versus exact lifted A* 7506.9.
- Certificate corruption result: 100% false negatives preserve success at 1.000 but raise expansions to 2279.8; 1% false positives lower success to 0.871.
- Recovery stress result: recovery-aware SCP succeeds at 1.000 with mean cost 40.3 under 50% recoverable cuts, while the strict monotone certificate claim remains intentionally bounded.
- Geometry proxy result: conservative extracted certificates reach 0.992 success at 40-cell scale with 5% extraction noise.

## Submission-Hardening v3

The v3 pass replaces the short v2 artifact with a final-scale mechanism paper. It adds zone scaling, topology variants, certificate-corruption sweeps, nonmonotone recovery stress, geometry-inspired extraction proxies, component ablations, generated figures/tables, a full experiment report, and a 25-page manuscript. The supported claim is not hardware deployment and not general continuous TAMP; it is a finite-graph spatial-commitment mechanism whose pruning is sound when cut-obligation certificates are conservative.
