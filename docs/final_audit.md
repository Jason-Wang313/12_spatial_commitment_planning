# Final Audit

1. **Chosen thesis:** Robots should plan with irreversible spatial commitments as first-class objects. The paper introduces cut-obligation certificates for spatial boundaries whose traversal would make future obligations unreachable.

2. **Field assumption broken:** Navigation/manipulation planners often assume local spatial feasibility is enough and that reversibility failures can be repaired later. The paper breaks the assumption that future access remains available after crossing a doorway, moving an object, or entering a constrained region.

3. **New central mechanism:** A directed spatial boundary carries a survivor set and a cut-obligation certificate listing the unserved obligations outside that survivor set. Search prunes or orders boundary crossings until those obligations are paid.

4. **Genuine novelty:** The narrow novelty claim is not TAMP, rearrangement, uncertainty, or a verifier. It is the boundary-attached obligation certificate derived from reachability loss and used as a first-class planning object.

5. **Closest hostile prior work:** Task-and-motion planning, PDDLStream/optimistic sampling, logic-geometric programming, navigation among movable obstacles, and object rearrangement planning. These are documented in `docs/hostile_prior_work.md`.

6. **Literature coverage:** 1109 OpenAlex-derived entries in `docs/related_work_matrix.csv`; top 300 serious skim; top 250 deep extraction; top 100 hostile prior-work set.

7. **Proof/formal-claim status:** Finite monotone reachability graph claims are proved in the paper: sound pruning and preservation of completeness/optimality for lifted shortest-path search with admissible heuristic. No continuous-space completeness claim is made.

8. **Strongest evidence:** Generated commitment-zone experiments: SCP success 1.0, exact lifted A* success 1.0, greedy local success 0.39166666666666666, relaxed agenda success 0.0; SCP expansion reduction 92.95607172945 percent. V2 certificate-corruption stress: false negatives preserve success but raise mean expansions to 713.4 at 100% omission, while false positives lower success to 0.804 at 1% spurious entries and 0.200 at 10%.

9. **Biggest weaknesses:** Synthetic benchmark; monotone survivor-set assumption; no real robot or mature TAMP benchmark; cut extraction in continuous contact-rich domains remains future work. The v2 stress shows that spurious cut obligations can prune valid plans, so conservative cut extraction is required.

10. **Paper-readiness judgment:** workshop / revise. The mechanism is crisp and runnable, but the evidence needs real robotics domains before a confident ICLR submission.

11. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/12.pdf` (168,720 bytes).

12. **GitHub URL:** https://github.com/Jason-Wang313/12_spatial_commitment_planning

13. **Visible Desktop PDF copy status:** pending orchestrator copy.

## Submission-Hardening v2

Checked: 2026-06-12 22:55:13 +01:00
Action: Added certificate false-negative/false-positive stress, generated CSV/table artifacts, and manuscript claim-boundary text.
Decision: Workshop-only / revise before main-conference submission.
Reason: The mechanism is crisp and reproducible, but evidence remains a synthetic monotone-zone benchmark without hardware, mature TAMP benchmarks, or continuous cut-extraction validation.
Downloads PDF: C:/Users/wangz/Downloads/12.pdf (168,720 bytes)
Desktop policy: no new Desktop copy created during v2 hardening.

## Orchestrator Desktop Copy

Checked: 2026-06-11 12:15:48 +01:00
Downloads PDF: C:/Users/wangz/Downloads/12.pdf
Result: copy script exit 0 log C:\Users\wangz\robotics_60_paper_batch\logs\desktop_copy_12_20260611_121546.log
