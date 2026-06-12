# Spatial Commitment Planning

Anonymous ICLR-style mechanism paper package for paper 12 in the robotics batch.

## Reproduce

```powershell
python scripts/collect_literature.py
python scripts/run_experiments.py
python scripts/synthesize_docs.py
python scripts/write_paper.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The compiled PDF is saved by the run procedure to `C:/Users/wangz/Downloads/12.pdf`.

## Current headline result

SCP success: 1.0

Exact lifted A* success: 1.0

## Submission-Hardening v2

The v2 pass adds `results/certificate_noise_summary.csv` and a manuscript table separating certificate false negatives from false positives. False negatives preserve 100% success but raise mean expansions to 713.4 when all true cuts are missed. False positives are more damaging: 1% spurious cut entries lower success to 80.4%, and 10% lowers success to 20.0%. This narrows the claim to settings where cut extraction is conservative.
