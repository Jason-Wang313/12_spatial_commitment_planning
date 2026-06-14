# Paper 12 Full-Scale Execution Plan

Paper: Spatial Commitment Planning
Repository: `12_spatial_commitment_planning`
Date: 2026-06-14

## Current Claim

Robots should treat irreversible spatial commitments as first-class planning objects. A directed spatial boundary carries a survivor set and a cut-obligation certificate listing obligations that would become unreachable after crossing. Search may cross the boundary only after those obligations are discharged.

## Current State

- Current canonical PDF is 5 pages and stale under the current 25-page standard.
- Existing evidence is a generated commitment-zone benchmark with 240 episodes.
- Existing result: SCP matches exact lifted A* success and cost while reducing expansions from 865.5 to 61.0.
- Existing v2 stress separates certificate false negatives and false positives:
  - false negatives preserve success but reduce pruning;
  - false positives prune valid plans and reduce success sharply.
- Existing readiness decision is workshop / revise because the evidence is synthetic and monotone-zone only.

## Reviewer Attacks To Resolve

1. This is just lifted graph search with a better hand-coded state.
2. This is just TAMP, rearrangement planning, navigation among movable obstacles, or dead-end detection.
3. The benchmark is too narrow: chain zones and one-way gates only.
4. The certificate is trivial if the generator already gives the zones.
5. The baselines are too weak or intentionally broken.
6. False positives destroy completeness, so the method is brittle.
7. Real spatial commitments can be nonmonotone or reversible after recovery actions.
8. No scaling study shows when certificates help versus exact lifted search.
9. No ablation separates survivor sets, cut obligations, heuristic strength, and state lifting.
10. No continuous or geometry-inspired cut extraction proxy exists.

## Experimental Expansion

Create a RAM-light full-scale runner under `experiments/full_scale_spatial_commitment.py`, with `scripts/run_experiments.py` acting as a stable wrapper. Store outputs under `results/full_scale/`. Run settings sequentially and write progress after each family.

### Family A: Commitment-Zone Scaling

Purpose: Strengthen the original chain-zone result with larger grids, seeds, and confidence intervals.

Settings:
- Zones: 4, 6, 8, 10, 12.
- Zone sizes: small, medium, large.
- Obligations per zone: 1, 2, 3.
- Gate density: single gate, multiple gates, bypass gates.
- Episodes/seeds: enough for stable 30-seed summaries.

Baselines:
- Greedy local.
- Relaxed agenda.
- Exact lifted A*.
- SCP cut-obligation A*.
- SCP without heuristic.
- Dead-end aware A*.
- Reverse-relaxed heuristic planner.

Metrics:
- Success, cost on successful runs, expansions, pruned commitments, certificates fired, gate crossings, timeout/exhaustion rate.

### Family B: Spatial Topology Variants

Purpose: Show the mechanism is not limited to linear chains.

Task families:
- Room-door grid with one-way doors.
- Branching corridors with service rooms.
- Loop-with-collapse where crossing a bridge removes an approach path.
- Warehouse aisles where pushing a cart blocks a side aisle.
- Payload-orientation gates where entering with a bulky object removes turn-around reachability.

Baselines:
- Exact lifted A*.
- SCP.
- Relaxed graph planner.
- Local replan-after-failure planner.
- Dead-end heuristic planner.

Metrics:
- Same as Family A, plus topology class and number of independent cuts.

### Family C: Certificate Extraction And Corruption

Purpose: Deepen the v2 stress and quantify the asymmetry between false negatives and false positives.

Settings:
- False-negative rate: 0, 0.05, 0.10, 0.25, 0.50, 0.75, 1.00.
- False-positive rate: 0, 0.001, 0.005, 0.01, 0.02, 0.05, 0.10.
- Mixed corruption: low false positive plus high false negative.
- Conservative extraction mode: include only cuts with high confidence.
- Aggressive extraction mode: include noisy inferred cuts.

Metrics:
- Success, expansions, pruned commitments, valid-plan prune rate, missed-doomed-branch rate.

### Family D: Nonmonotone Recovery Stress

Purpose: Define where monotone certificates break and how fallback/recovery actions alter the claim.

Task:
- Some commitments can be reversed by paying a recovery cost, using a helper route, or moving a blocker back.
- Recovery actions are rare, expensive, or capacity-limited.

Policies:
- Strict SCP that assumes monotone cuts.
- Recovery-aware SCP with delayed certificate payment.
- Exact lifted recovery search.
- Relaxed planner.
- Greedy replan.

Metrics:
- Success, cost, unnecessary avoidance, recovery action use, false pruning under nonmonotone effects.

### Family E: Geometry-Inspired Cut Extraction Proxy

Purpose: Move beyond hand-given zone cuts without claiming full continuous TAMP.

Task:
- Generate 2D grid maps with rooms, doorways, payload widths, movable blockers, and obligation locations.
- Derive approximate survivor sets by flood fill after simulated gate crossing or blocker placement.
- Add extraction noise by eroding/dilating traversable cells.

Policies:
- SCP from extracted cuts.
- Exact grid lifted A*.
- Relaxed grid A*.
- Local planner.
- Conservative SCP with only high-confidence cuts.

Metrics:
- Success, cost, expansions, extraction false positive/negative counts, cells explored, cut size.

### Family F: Ablations And Scaling

Purpose: Separate mechanism components.

Ablations:
- Lifted state without cut pruning.
- Cut pruning without obligation ordering.
- Certificates without survivor-set update.
- Heuristic-only dead-end penalties.
- SCP with exact certificates.
- SCP with noisy certificates.

Metrics:
- Expansion ratio to exact lifted search.
- Success difference.
- Cost difference on successful episodes.
- Memory proxy: frontier peak and unique states.

## Figures And Tables

Required figures:
- Scaling: expansions versus zones/obligations.
- Topology variants: success and expansion ratio by topology.
- Certificate corruption: success and expansions versus false-positive/false-negative rate.
- Nonmonotone recovery: success/cost tradeoff.
- Geometry proxy: extracted cut quality versus planning success.
- Ablation waterfall: which component gives the expansion reduction.

Required tables:
- Main scaling table.
- Topology table.
- Certificate stress table.
- Nonmonotone recovery table.
- Geometry proxy table.
- Ablation table.
- Claim-to-evidence table.
- Runtime/RAM-light table.

## Manuscript Expansion

Target structure:
- Abstract with v3 full-scale numbers and honest boundary.
- Introduction framing spatial commitments as access-option consumption.
- Related work boundary against TAMP, rearrangement, NAMO, dead-end detection, graph search, and irreversible planning.
- Formal definitions: survivor sets, obligations, cut certificates, lifted state, sound pruning, completeness/optimality under monotonicity.
- Algorithm section: certificate construction, SCP A*, recovery-aware variant, and failure handling.
- Experiment design across six families.
- Results with figures/tables.
- Failure analysis: false positives, nonmonotone recovery, noisy cut extraction, baseline fairness.
- Limitations: synthetic evidence, no hardware, no full continuous TAMP, conservative cut extraction requirement.
- Appendices: parameter grids, pseudocode, self-attacks, reproducibility, artifact audit.

Page strategy:
- Minimum internal threshold is 25 pages.
- Length must come from real content: expanded theory, new experiments, richer baseline descriptions, negative results, detailed appendix, and reproducibility.

## RAM-Light Execution Strategy

- Run experiment families sequentially.
- Store per-seed or per-setting aggregate rows, not full search trees.
- Track frontier peak and unique states as numeric summaries.
- Avoid storing map cell histories beyond current episode.
- Write progress JSON after each family.
- Generate figures/tables from summaries.
- Keep exact lifted search timeouts bounded and recorded.

## Documentation Updates

Update after the full-scale pass:
- `README.md`
- `child_status.md`
- `docs/claims.md`
- `docs/experiment_report.md` if added
- `docs/experiment_rigor_checklist.md`
- `docs/reproducibility_checklist.md`
- `docs/reviewer_attacks.md`
- `docs/hostile_reviewer_response.md`
- `docs/submission_attack_log.md`
- `docs/submission_version_log.md`
- `docs/final_audit.md`
- `docs/submission_readiness_decision.md`

## Acceptance Checklist

Paper12 is not final until all are true:
- Full-scale runner completes and writes `results/full_scale/progress.json` with stage `complete`.
- `python -m py_compile` passes for edited scripts.
- Figures and tables are regenerated from v3 summaries.
- Manuscript compiles with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Final PDF has at least 25 pages.
- Claims match generated CSVs/tables.
- Limitations explicitly include synthetic evidence, monotone assumptions, false-positive certificate risk, no hardware, and no full continuous TAMP claim.
- Canonical PDF is copied to `C:/Users/wangz/Downloads/12.pdf` only after final verification.
- Local `paper/main.pdf` is removed after final copy.
- Commit is pushed.
- Worktree is clean and `HEAD` matches upstream before moving to Paper13.
