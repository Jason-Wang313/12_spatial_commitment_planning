# Plan: Spatial Commitment Planning

## Mission
Produce a complete anonymous ICLR-style robotics paper package for paper 12, including a broad literature audit, honest novelty boundary, runnable evidence, compiled PDF at `C:/Users/wangz/Downloads/12.pdf`, and a pushed public GitHub repository named `12_spatial_commitment_planning`.

## Safety and Run Discipline
- Keep commands non-interactive and bounded with explicit timeouts for long jobs.
- Prefer scripts for complex data retrieval, parsing, experiments, plotting, and LaTeX preparation.
- Keep `child_status.md` compact and current after each major stage.
- Reuse existing artifacts if valid; do not delete expensive caches unless inadequate.
- Keep all claims honest and mark unsupported claims clearly.

## Execution Stages
1. Inspect workspace and tool availability without brittle probes.
2. Create repository structure and status ledger.
3. Retrieve the latest official ICLR LaTeX template source available at runtime.
4. Build literature pipeline:
   - 1000-paper landscape sweep into `docs/related_work_matrix.csv`.
   - 300-paper serious skim summary.
   - 200-250-paper deep read extraction.
   - 100-paper hostile prior-work set.
5. Derive field box, hidden assumptions, candidate directions, novelty boundary, and final decision.
6. Implement runnable evidence for the selected mechanism.
7. Generate plots/tables and write paper source.
8. Compile with direct `pdflatex`/`bibtex` passes where available; save final PDF exactly to `C:/Users/wangz/Downloads/12.pdf`.
9. Audit repo reproducibility and write `docs/final_audit.md`.
10. Commit, create public GitHub repo `12_spatial_commitment_planning`, and push; document any failure.

## Expected Artifacts
- `docs/related_work_matrix.csv`
- `docs/literature_map.md`
- `docs/hostile_prior_work.md`
- `docs/novelty_boundary_map.md`
- `docs/novelty_decision.md`
- `docs/claims.md`
- `docs/reviewer_attacks.md`
- `docs/final_audit.md`
- Runnable experiment scripts, cached results, plots, LaTeX source, final PDF.
