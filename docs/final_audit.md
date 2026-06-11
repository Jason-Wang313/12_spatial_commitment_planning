# Final Audit

1. **Chosen thesis:** Robots should plan with irreversible spatial commitments as first-class objects. The paper introduces cut-obligation certificates for spatial boundaries whose traversal would make future obligations unreachable.

2. **Field assumption broken:** Navigation/manipulation planners often assume local spatial feasibility is enough and that reversibility failures can be repaired later. The paper breaks the assumption that future access remains available after crossing a doorway, moving an object, or entering a constrained region.

3. **New central mechanism:** A directed spatial boundary carries a survivor set and a cut-obligation certificate listing the unserved obligations outside that survivor set. Search prunes or orders boundary crossings until those obligations are paid.

4. **Genuine novelty:** The narrow novelty claim is not TAMP, rearrangement, uncertainty, or a verifier. It is the boundary-attached obligation certificate derived from reachability loss and used as a first-class planning object.

5. **Closest hostile prior work:** Task-and-motion planning, PDDLStream/optimistic sampling, logic-geometric programming, navigation among movable obstacles, and object rearrangement planning. These are documented in `docs/hostile_prior_work.md`.

6. **Literature coverage:** 1109 OpenAlex-derived entries in `docs/related_work_matrix.csv`; top 300 serious skim; top 250 deep extraction; top 100 hostile prior-work set.

7. **Proof/formal-claim status:** Finite monotone reachability graph claims are proved in the paper: sound pruning and preservation of completeness/optimality for lifted shortest-path search with admissible heuristic. No continuous-space completeness claim is made.

8. **Strongest evidence:** Generated commitment-zone experiments: SCP success 1.0, exact lifted A* success 1.0, greedy local success 0.39166666666666666, relaxed agenda success 0.0; SCP expansion reduction 92.95607172945 percent.

9. **Biggest weaknesses:** Synthetic benchmark; monotone survivor-set assumption; no real robot or mature TAMP benchmark; cut extraction in continuous contact-rich domains remains future work.

10. **Paper-readiness judgment:** workshop / revise. The mechanism is crisp and runnable, but the evidence needs real robotics domains before a confident ICLR submission.

11. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/12.pdf` (exists).

12. **GitHub URL:** https://github.com/Jason-Wang313/12_spatial_commitment_planning

13. **Visible Desktop PDF copy status:** pending orchestrator copy.
