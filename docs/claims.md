# Claims

## Formal claims
1. In a finite graph with monotone survivor-set effects, a transition that would remove an unserved required object or terminal goal from the survivor set cannot be part of any successful plan. This supports sound pruning by cut-obligation certificates.
2. Lifted search over `(configuration, completed obligations, survivor set)` is complete and cost-optimal for finite nonnegative-cost graphs when using an admissible heuristic; cut-obligation pruning preserves those properties because it only removes provably doomed transitions.
3. When commitments can be undone only through explicit recovery actions, strict monotone certificates are no longer the right model; a recovery-aware lifted state must represent recovery cost and availability rather than silently assuming monotonicity.

## Empirical claims supported by this repo
- V3 full-scale runner completed six families: zone scaling, topology variants, certificate corruption, nonmonotone recovery, geometry proxy, and ablations.
- Main 10-zone scaling setting: SCP success 1.000, exact lifted A* success 1.000, greedy local success 0.174, relaxed agenda success 0.000.
- Main scaling efficiency: SCP uses 183.4 mean expansions versus 7506.9 for exact lifted A*, an expansion ratio of 0.024 while preserving success.
- Topology variants: SCP succeeds at 1.000 across chain, bypass, room-grid, loop-collapse, warehouse, and payload-orientation settings.
- Certificate false-negative stress: 100% omitted true cuts keeps success at 1.000 but raises mean expansions to 2279.8.
- Certificate false-positive stress: 1% spurious cuts lowers success to 0.871; 10% spurious cuts drives success to 0.000.
- Nonmonotone recovery stress: recovery-aware SCP succeeds at 1.000 with mean cost 40.3 in the 50% recoverable, cost-5 setting; relaxed planning succeeds at 0.445 and greedy at 0.540.
- Geometry proxy stress: conservative SCP reaches 0.992 success at 40-cell scale with 5% extraction noise; aggressive extracted cuts trade lower expansions for lower success.
- Ablations show the certificate mechanism, not only the heuristic, drives the expansion reduction: exact certificates use 183.4 expansions, no-heuristic SCP uses 236.4, and lifted no-prune uses 7506.9.

## Honest limits
- Evidence is synthetic and targets the mechanism, not real-robot deployment.
- The formal guarantee is finite-graph and monotone unless recovery actions are modeled explicitly.
- Continuous cut extraction is represented by a geometry-inspired proxy, not by a deployed continuous TAMP extractor.
- Cut extraction must be conservative; false-positive cut obligations can prune valid plans and break completeness.
- Literature extraction is broad and adversarial, but metadata/abstract based.
