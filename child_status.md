# Child Status

stage: complete
latest_update: repo committed and pushed to public GitHub; final PDF exists at the exact Downloads path; final audit exists
commands:
- python scripts/synthesize_docs.py
- python scripts/write_paper.py
- pdflatex/bibtex/pdflatex/pdflatex in paper/
- Copy-Item paper/main.pdf C:/Users/wangz/Downloads/12.pdf
- gh repo create Jason-Wang313/12_spatial_commitment_planning --public --source . --remote origin
- python scripts/write_final_audit.py
- git add -A
- git commit -m "Build spatial commitment planning paper package"
- git push -u origin master
failures:
- `scripts/write_paper.py` initially had one unmatched f-string brace; patched and reran successfully
- initial `gh repo view` confirmed the target repo did not exist; created it
recovery:
- sanitized BibTeX non-ASCII before build
- removed stale build PDF/intermediates after copying final PDF to the exact Downloads path
- ignored transient OpenAlex cache and local template zip
current_results:
- related_work_matrix rows: 1109
- hostile prior flags: 100
- SCP success: 1.0
- exact lifted A* success: 1.0
- greedy local success: 0.39166666666666666
- relaxed agenda success: 0.0
- final PDF: C:/Users/wangz/Downloads/12.pdf
- GitHub URL: https://github.com/Jason-Wang313/12_spatial_commitment_planning
- Desktop PDF status in final audit: pending orchestrator copy
next: none

Exit code: 0
End time: 2026-06-11 12:15:46 +01:00
PDF exists: True

## Submission-Hardening v2

End time: 2026-06-12 22:55:13 +01:00
Stage: terminal workshop-only / revise

Added facts:
- Added certificate-corruption stress separating false-negative and false-positive cut obligations.
- False-negative certificates preserve 100% success but raise mean expansions to 713.4 when all true cuts are missed.
- False-positive certificates lower success to 0.804 at 1% spurious cut entries and 0.200 at 10%.
- Generated `results/certificate_noise_summary.csv` and `results/certificate_noise_table.tex`.
- Updated manuscript abstract, results, limitations, and v2 marker.
- Added submission attack/version/readiness/reproducibility/rigor docs.
- Rebuilt the PDF with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Copied canonical PDF to `C:/Users/wangz/Downloads/12.pdf` (168,720 bytes).
- Removed local `paper/main.pdf` after copying the canonical PDF.
- No new Desktop PDF copy was created during v2 hardening.

Latest terminal decision:
- Workshop-only / revise. The mechanism is crisp, but evidence remains a synthetic monotone-zone benchmark without hardware, mature TAMP benchmarks, or continuous cut-extraction validation.
