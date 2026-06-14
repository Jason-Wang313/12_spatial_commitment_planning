# Hostile Reviewer Response

We agree that the benchmark does not establish deployment-ready robot planning. The v3 paper is framed as a finite-graph mechanism paper: cut-obligation certificates expose which boundary crossings would strand unpaid obligations and prune those branches before search expands them.

Exact lifted A* already solves the synthetic tasks when the correct irreversible state is exposed. The v3 evidence therefore makes the efficiency claim explicit rather than pretending SCP is the only complete solver: in the 10-zone medium-pressure setting, exact lifted A* succeeds at 1.000 with 7506.9 expansions, while SCP succeeds at 1.000 with 183.4 expansions. Ablations show the certificate matters even without the heuristic.

The strongest implementation dependency is conservative certificate extraction. If certificates omit true cut obligations, SCP remains successful but loses pruning: at 100% false negatives, mean expansions rise to 2279.8. If certificates hallucinate cut obligations, SCP can prune valid plans: 1% false positives lower success to 0.871 and 10% lowers success to 0.000.

The final claim is therefore precise: finite monotone spatial-commitment planning is improved by boundary-attached cut-obligation certificates; nonmonotone recovery must be modeled explicitly; geometry extraction quality controls whether the mechanism is safe. Stronger robotics claims would require real TAMP/NAMO benchmarks, hardware or high-fidelity simulation, and a validated continuous cut-extraction procedure.
