# Claims

## Formal claims
1. In a finite graph with monotone survivor-set effects, a transition that would remove an unserved required object or terminal goal from the survivor set cannot be part of any successful plan. This supports sound pruning by cut-obligation certificates.
2. Lifted search over `(configuration, completed obligations, survivor set)` is complete and cost-optimal for finite nonnegative-cost graphs when using an admissible heuristic; cut-obligation pruning preserves those properties because it only removes provably doomed transitions.

## Empirical claims supported by this repo
- SCP success rate in generated tasks: 1.000.
- Exact lifted A* success rate: 1.000.
- Greedy local success rate: 0.392.
- Relaxed agenda success rate: 0.000.
- SCP mean expansion fraction of exact A*: 0.070.
- V2 certificate false-negative stress: success remains 1.000, but mean expansions rise to 713.4 when all true cut obligations are omitted.
- V2 certificate false-positive stress: success falls to 0.804 at 1% spurious cut entries and 0.200 at 10%.

## Honest limits
- Evidence is synthetic and targets the mechanism, not real-robot deployment.
- The generator uses monotone zone commitments; richer manipulation contacts can violate this structure.
- Cut extraction must be conservative; false-positive cut obligations can prune valid plans.
- Literature extraction is broad and adversarial, but metadata/abstract based.
