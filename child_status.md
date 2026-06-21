# Child Status: Paper 12

## Current stage
VLA-style boxed-link hardening complete; final artifact exported and verified.

## v3 commands run
- Ran six Paper12 experiment families with 30 seed replicates per setting.
- Wrote full-scale CSV summaries, figures, tables, metadata, progress, and experiment report.
- Built the v3 manuscript with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Added explicit VLA-style hyperref policy to `paper/main.tex`: green citation/URL boxes, red internal-reference boxes, and one-point PDF borders.
- Verified local build is 25 pages and hard-error log scan is clean.
- Copied final verified PDF to `C:/Users/wangz/Downloads/12.pdf` (25 pages, 410,264 bytes, SHA256 `A2E7BE0F3316564429D507F211A6C4479F5BC6614372B327BFAE1A8448866B4B`).
- Final link inventory: 48 annotations on pages `[(2, 20), (3, 21), (5, 2), (6, 4), (7, 1)]`; colors green = 41, red = 7, cyan = 0; all borders `(0, 0, 1)`.
- Rendered and visually inspected pages 2, 3, 5, 6, and 7; highlighted boxes are crisp and aligned.
- Plot failures: 0.

## v3 findings
- Zone scaling, 10 medium zones, pressure 2: SCP success 1.000, exact lifted success 1.000, SCP expansions 183.4 versus exact lifted A* 7506.9.
- Certificate corruption: 100% false negatives preserve success at 1.000 but raise expansions to 2279.8; 1% false positives lower success to 0.871.
- Nonmonotone recovery: recovery-aware SCP succeeds at 1.000 with mean cost 40.3 under 50% recoverable cuts.
- Geometry proxy: conservative extracted certificates reach 0.992 success at 40-cell scale with 5% extraction noise.

## Failures and recovery
- None in the VLA-style link hardening pass.

## Remaining steps
- Commit, push, and verify clean/upstream before starting Paper 11.
