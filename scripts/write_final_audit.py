"""Write docs/final_audit.md from current repository facts."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RESULTS = ROOT / "results"
DOWNLOAD_PDF = Path("C:/Users/wangz/Downloads/12.pdf")
DESKTOP_PDF = Path("C:/Users/wangz/OneDrive/Desktop/12.pdf")


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def git_remote() -> str:
    try:
        out = subprocess.check_output(
            ["git", "remote", "get-url", "origin"],
            cwd=str(ROOT),
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=10,
        ).strip()
    except Exception:
        return "pending GitHub push"
    if out.endswith(".git"):
        out = out[:-4]
    if out.startswith("git@github.com:"):
        out = "https://github.com/" + out.split(":", 1)[1]
    return out or "pending GitHub push"


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    summary = load_json(RESULTS / "summary.json")
    lit = load_json(ROOT / "data" / "literature_collection_summary.json")
    scp = summary.get("scp_cut_obligations", {})
    exact = summary.get("exact_lifted_astar", {})
    greedy = summary.get("greedy_local", {})
    agenda = summary.get("relaxed_agenda", {})
    comp = summary.get("comparison", {})
    desktop_status = "copied to visible Desktop" if DESKTOP_PDF.exists() else "pending orchestrator copy"
    text = f"""# Final Audit

1. **Chosen thesis:** Robots should plan with irreversible spatial commitments as first-class objects. The paper introduces cut-obligation certificates for spatial boundaries whose traversal would make future obligations unreachable.

2. **Field assumption broken:** Navigation/manipulation planners often assume local spatial feasibility is enough and that reversibility failures can be repaired later. The paper breaks the assumption that future access remains available after crossing a doorway, moving an object, or entering a constrained region.

3. **New central mechanism:** A directed spatial boundary carries a survivor set and a cut-obligation certificate listing the unserved obligations outside that survivor set. Search prunes or orders boundary crossings until those obligations are paid.

4. **Genuine novelty:** The narrow novelty claim is not TAMP, rearrangement, uncertainty, or a verifier. It is the boundary-attached obligation certificate derived from reachability loss and used as a first-class planning object.

5. **Closest hostile prior work:** Task-and-motion planning, PDDLStream/optimistic sampling, logic-geometric programming, navigation among movable obstacles, and object rearrangement planning. These are documented in `docs/hostile_prior_work.md`.

6. **Literature coverage:** {lit.get('rows', 'unknown')} OpenAlex-derived entries in `docs/related_work_matrix.csv`; top 300 serious skim; top 250 deep extraction; top 100 hostile prior-work set.

7. **Proof/formal-claim status:** Finite monotone reachability graph claims are proved in the paper: sound pruning and preservation of completeness/optimality for lifted shortest-path search with admissible heuristic. No continuous-space completeness claim is made.

8. **Strongest evidence:** Generated commitment-zone experiments: SCP success {scp.get('success_rate', 'pending')}, exact lifted A* success {exact.get('success_rate', 'pending')}, greedy local success {greedy.get('success_rate', 'pending')}, relaxed agenda success {agenda.get('success_rate', 'pending')}; SCP expansion reduction {comp.get('scp_expansion_reduction_percent', 'pending')} percent.

9. **Biggest weaknesses:** Synthetic benchmark; monotone survivor-set assumption; no real robot or mature TAMP benchmark; cut extraction in continuous contact-rich domains remains future work.

10. **Paper-readiness judgment:** workshop / revise. The mechanism is crisp and runnable, but the evidence needs real robotics domains before a confident ICLR submission.

11. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/12.pdf` ({'exists' if DOWNLOAD_PDF.exists() else 'missing'}).

12. **GitHub URL:** {git_remote()}

13. **Visible Desktop PDF copy status:** {desktop_status}.
"""
    (DOCS / "final_audit.md").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
