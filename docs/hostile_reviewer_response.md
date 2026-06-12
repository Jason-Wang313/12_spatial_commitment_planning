# Hostile Reviewer Response

We agree that the benchmark does not establish deployment-ready robot planning. Exact lifted A* already solves the synthetic tasks when the correct irreversible state is exposed. The contribution is narrower: cut-obligation certificates expose which boundary crossings would strand unpaid obligations and prune those branches before search expands them.

The v2 stress clarifies the strongest implementation dependency. If certificates omit true cut obligations, SCP remains successful but loses pruning: at 100% false negatives, mean expansions rise to 713.4. If certificates hallucinate cut obligations, SCP can prune valid plans: success falls to 0.804 at 1% false positives and 0.200 at 10%.

The paper should therefore claim a finite-graph mechanism under conservative cut extraction, not general continuous planning robustness. A stronger submission needs real TAMP/NAMO benchmarks, hardware or high-fidelity simulation, and a validated continuous cut-extraction procedure.
