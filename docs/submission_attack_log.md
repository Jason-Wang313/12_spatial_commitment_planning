# Submission Attack Log

## Paper 12: Spatial Commitment Planning

Date: 2026-06-12
Decision: workshop-only / revise before main-conference submission

## Harsh Attacks

1. Full lifted A* already solves the benchmark.
   - Response: acknowledged; SCP's contribution is the cut-obligation certificate that prunes doomed branches before expansion.
2. The benchmark is synthetic and monotone.
   - Response: terminal decision remains workshop-only; no real robot or mature TAMP benchmark claim is made.
3. Cut extraction errors can be dangerous.
   - Response: added v2 certificate-corruption stress. False negatives preserve success but lose pruning; false positives can prune valid plans.
4. Continuous cut extraction may be expensive.
   - Response: left as future work and narrowed the formal claim to finite survivor-set graphs.
5. NAMO/rearrangement planning already handles access.
   - Response: novelty is narrowed to reusable boundary-attached obligation certificates.

## Remaining Non-Recoverable Weaknesses In This Pass

- No real robot.
- No mature TAMP/NAMO benchmark.
- No continuous-space cut extraction.
- Monotone survivor-set assumption.
- False-positive certificates can break completeness.
