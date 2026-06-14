# Submission Version Log

## v1

- Initial anonymous ICLR-style artifact.
- Commitment-zone benchmark with greedy local, relaxed agenda, exact lifted A*, and SCP.
- Canonical PDF: `C:/Users/wangz/Downloads/12.pdf`.

## v2 - 2026-06-12

- Added certificate-corruption stress in `scripts/run_experiments.py`.
- Generated `results/certificate_noise_summary.csv` and `results/certificate_noise_table.tex`.
- Updated manuscript abstract, results, limitations, and v2 marker.
- Updated claims, reviewer attacks, and final audit docs.
- Added submission attack, readiness, rigor, and reproducibility docs.
- Terminal decision remains workshop-only / revise.

## v3 - 2026-06-14

- Wrote `docs/full_scale_execution_plan.md` before the full-scale pass.
- Added RAM-light full-scale runner `experiments/full_scale_spatial_commitment.py`; `scripts/run_experiments.py` now dispatches to it.
- Generated six evidence families under `results/full_scale/`: zone scaling, topology variants, certificate corruption, recovery stress, geometry proxy, and ablations.
- Generated full-scale CSV summaries, progress metadata, figures, tables, and `docs/experiment_report.md`.
- Rewrote `paper/main.tex` into a 25-page final-scale manuscript with expanded theory, experiment design, results, limitations, appendices, and reproducibility notes.
- Verified local build with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`; hard-error log scan returned no matches.
- Final decision: ready as a bounded mechanism-paper submission package, while explicitly not claiming real-robot deployment or full continuous TAMP validation.
