# Full-Scale Experiment Report

## Scope
- Six experiment families: zone scaling, topology variants, certificate corruption, nonmonotone recovery, geometry proxy, and ablations.
- Thirty seed replicates per setting.
- Search families use bounded exact/lifted search; recovery and geometry proxy families use compact aggregate models.
- Outputs are written under `results/full_scale/` as CSV summaries, progress metadata, LaTeX tables, PDF figures, and PNG figures.

## Key Findings
- Zone scaling, 10 medium zones, pressure 2: SCP success 1.000, exact lifted success 1.000, SCP/exact expansion ratio 0.024.
- Certificate stress: 100% false negatives preserve success 1.000 but raise expansions to 2279.8; 1% false positives reduce success to 0.871.
- Nonmonotone recovery, cost 5 and 50% recoverable cuts: recovery-aware SCP success 1.000 with cost 40.3.
- Geometry proxy, 40-cell scale and 5% extraction noise: conservative SCP success 0.992 with 0.08 false-positive cuts on average.
- Ablation: lifted no-prune uses 7506.9 expansions, SCP exact certificates use 183.4, SCP without the heuristic uses 236.4, and dead-end aware A* uses 304.0.
- Runtime/RAM-light scope: 2700 zone-scaling planner runs, 900 topology runs, 510 corrupted runs, 1800 recovery aggregate rows, 2700 geometry aggregate rows, and 6 ablation summary rows.

## Plot Status
- All full-scale figures generated successfully.

## Generated Tables
- `table_main_scaling_10.tex`
- `table_topology_variants.tex`
- `table_certificate_stress.tex`
- `table_recovery_stress.tex`
- `table_geometry_proxy.tex`
- `table_ablation.tex`
- `table_runtime_memory.tex`
- `table_claim_evidence.tex`

## Generated Figures
- `figure_zone_scaling`
- `figure_topology_success`
- `figure_certificate_stress`
- `figure_recovery_stress`
- `figure_geometry_proxy`
- `figure_ablation`
