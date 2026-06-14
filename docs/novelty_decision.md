# Novelty Decision

## Chosen thesis
Robots should plan with irreversible spatial commitments as first-class objects. A spatial commitment is a directed boundary crossing or placement whose effect is not just local motion cost, but a certificate that some region/approach/obligation becomes unreachable unless discharged beforehand.

## New central mechanism
Cut-obligation certificates. For each candidate boundary, compute the obligations outside the survivor set that would be lost after crossing. The planner lifts state by the active survivor region and prunes or orders actions whose certificates still carry unpaid obligations.

## Why this is stronger than the seed
The seed suggested planning with irreversible commitments. The literature sweep points to a sharper contribution: commitments are not just labels or costs; they are boundary-attached certificates that generate ordering constraints and sound search pruning.

## Why other directions were rejected
- Larger models, additional training data, RL, and LLM planners do not change the central mechanism.
- A benchmark alone would only expose the failure mode.
- A verifier would detect failure after proposing a branch; the proposed mechanism changes what search expands.
- Generic uncertainty handling misidentifies the issue: the benchmark is fully known and still breaks reversible abstractions.

## v3 Claim Boundary

The full-scale pass strengthens the mechanism rather than broadening it into a different paper. The final claim remains boundary-attached cut-obligation certificates for finite spatial commitments. The new evidence shows scaling, topology transfer, corruption asymmetry, recovery boundaries, geometry-proxy sensitivity, and ablation separation. The paper still does not claim hardware deployment, full continuous TAMP extraction, or robustness to hallucinated cut obligations.
