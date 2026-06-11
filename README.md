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
