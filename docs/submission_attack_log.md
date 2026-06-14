# Submission Attack Log

## Paper 12: Spatial Commitment Planning

Date: 2026-06-14
Decision: final under bounded mechanism-paper scope

## Harsh Attacks

1. Full lifted A* already solves the benchmark.
   - Response: acknowledged and quantified. SCP preserves exact lifted success while reducing expansions from 7506.9 to 183.4 in the main 10-zone setting.
2. The benchmark is synthetic and monotone.
   - Response: accepted as a scope boundary. The final paper does not claim hardware deployment or general continuous TAMP.
3. Cut extraction errors can be dangerous.
   - Response: v3 expands certificate-corruption stress. False negatives preserve success but lose pruning; false positives can prune valid plans and drop success to 0.000 at 10%.
4. Continuous cut extraction may be expensive.
   - Response: left as a future-work boundary, with a geometry-inspired extraction proxy added to test noise sensitivity.
5. NAMO/rearrangement planning already handles access.
   - Response: novelty is narrowed to reusable boundary-attached obligation certificates.
6. The chain benchmark is too narrow.
   - Response: v3 adds six topology variants and keeps SCP success at 1.000 across them.
7. Monotone commitments are unrealistic when recovery actions exist.
   - Response: v3 adds recovery stress and explicitly separates strict SCP from recovery-aware SCP.
8. The gains might be heuristic-only.
   - Response: v3 ablations show no-heuristic SCP still reduces expansions from 7506.9 to 236.4.

## Remaining Non-Recoverable Weaknesses In This Pass

- No real robot.
- No mature TAMP/NAMO benchmark.
- No full continuous-space cut extraction.
- Finite monotone survivor-set assumption for the formal guarantee.
- False-positive certificates can break completeness.
