# Novelty Boundary Map

## What prior work already covers
- Sampling-based motion planning covers continuous feasibility and narrow-passage exploration, so this paper must not claim novelty for finding geometric paths.
- Task-and-motion planning covers symbolic/geometric integration, optimistic sampling, and many forms of geometric precondition checking.
- Navigation among movable obstacles and rearrangement planning cover object movements that open or block access.
- Heuristic graph search covers lifted-state optimality once all irreversible effects are explicitly encoded.
- Belief-space and contingent planning cover uncertainty; uncertainty is not the mechanism here.

## Boundary this paper claims
The paper claims novelty only for treating irreversible spatial commitments as first-class objects with cut-obligation certificates: crossing a boundary is represented by the set of future obligations it would make unreachable, and the planner reasons over those certificates before crossing.

## Closest hostile categories
- TAMP systems could encode such preconditions by hand, but they usually do not derive them from spatial reachability cuts.
- Rearrangement planners reason about access blockers, but usually as object-ordering or path-existence constraints rather than reusable commitment objects attached to spatial boundaries.
- Full lifted search can solve the generated benchmark when given exact monotone effects; the contribution is the commitment certificate and pruning/ordering mechanism, not a new completeness result for graph search.

## Unsupported or deliberately weak claims
- No claim that the method handles deformable contact, stochastic dynamics, or unknown maps.
- No claim of outperforming mature TAMP systems on full robotics benchmarks.
- No claim that cut obligations are the only way to represent irreversible commitments.