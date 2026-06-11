"""Synthesize audit documents from literature and experiment artifacts."""

from __future__ import annotations

import csv
import json
import math
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RESULTS = ROOT / "results"
PAPER = ROOT / "paper"


HIDDEN_ASSUMPTIONS = [
    "Spatial actions are locally reversible unless the domain author explicitly marks them otherwise.",
    "If a motion is geometrically feasible now, its long-horizon consequence can be postponed to later search.",
    "A symbolic predicate such as at(room) captures the relevant spatial state for future planning.",
    "A robot can return to a previous approach region after passing through a narrow passage.",
    "Object placements are static facts rather than changes to the topology of future reachability.",
    "Manipulation actions only change object poses, not the robot's future maneuvering options.",
    "Dead ends are rare enough that backtracking search will discover them cheaply.",
    "Reachability loss can be represented as ordinary action cost.",
    "The set of future obligations is independent of the spatial boundary just crossed.",
    "Roadmap or sampling density is the main reason a narrow passage is hard.",
    "The planner can evaluate feasibility one subgoal at a time.",
    "A learned or heuristic high-level agenda can be repaired after geometric failure.",
    "Topological access is fixed during execution.",
    "The relevant failure mode is uncertainty, not irreversible commitment under known geometry.",
    "All preconditions worth reasoning about are attached to actions, not to spatial cuts.",
    "Rearrangement constraints are object-ordering constraints only, not access-loss constraints.",
    "The cost-to-go heuristic may ignore whether a necessary return path survives.",
    "Execution monitors can catch commitment mistakes without needing to change the planner's state space.",
    "Navigation and manipulation commitments can be handled by separate modules.",
    "A future geometric plan exists if every local transition has an inverse somewhere in the roadmap.",
    "The robot's body/cargo footprint does not turn a corridor traversal into a one-way commitment.",
    "Deleting a reachable region is equivalent to increasing its traversal cost.",
    "The planner need not expose why a branch became impossible.",
    "A failure certificate after the fact is as useful as a commitment certificate before the fact.",
    "Task-level abstractions can be complete without representing spatial accessibility basins.",
    "The same symbolic state is valid on both sides of a one-way spatial boundary.",
]


DIRECTIONS = [
    (
        "Commitment-cut planning",
        "Derive directed spatial cuts whose traversal deletes access to obligations; promote the cut and its outstanding obligations into the planning state.",
    ),
    (
        "Manipulation-mode foreclosure",
        "Track grasp, cargo, and placement choices as commitments that remove approach manifolds before a placement is made.",
    ),
    (
        "Reversible-region contracts",
        "Compile each local roadmap region into a contract saying which tasks remain reversible from that region.",
    ),
    (
        "Commitment-aware agenda repair",
        "Instead of validating an agenda, insert ordering constraints induced by impending access loss.",
    ),
    (
        "Spatial debt accounting",
        "Measure how many future obligations a partial plan owes before crossing each boundary.",
    ),
    (
        "Cut-derived symbolic predicates",
        "Generate PDDL-like predicates from geometric reachability cuts rather than hand-writing all dead-end preconditions.",
    ),
    (
        "Contact-as-topology planning",
        "Treat pushes and placements as topological edits to accessibility, not only continuous contact dynamics.",
    ),
    (
        "Commitment certificates for demonstrations",
        "Annotate robot demonstrations with the first point at which future alternatives are lost.",
    ),
]


MANUAL_BIB = r"""
@book{lavalle2006planning,
  title={Planning Algorithms},
  author={LaValle, Steven M.},
  year={2006},
  publisher={Cambridge University Press}
}

@article{kavraki1996probabilistic,
  title={Probabilistic roadmaps for path planning in high-dimensional configuration spaces},
  author={Kavraki, Lydia E. and Svestka, Petr and Latombe, Jean-Claude and Overmars, Mark H.},
  journal={IEEE Transactions on Robotics and Automation},
  year={1996},
  volume={12},
  number={4},
  pages={566--580}
}

@article{lavalle1998rapidly,
  title={Rapidly-exploring random trees: A new tool for path planning},
  author={LaValle, Steven M.},
  year={1998}
}

@article{hart1968formal,
  title={A formal basis for the heuristic determination of minimum cost paths},
  author={Hart, Peter E. and Nilsson, Nils J. and Raphael, Bertram},
  journal={IEEE Transactions on Systems Science and Cybernetics},
  year={1968},
  volume={4},
  number={2},
  pages={100--107}
}

@inproceedings{stilman2005navigation,
  title={Navigation among movable obstacles},
  author={Stilman, Mike and Kuffner, James J.},
  booktitle={Algorithmic Foundations of Robotics VI},
  year={2005}
}

@inproceedings{stilman2007manipulation,
  title={Manipulation planning among movable obstacles},
  author={Stilman, Mike and Schamburek, Jan-Ullrich and Kuffner, James and Asfour, Tamim},
  booktitle={IEEE International Conference on Robotics and Automation},
  year={2007}
}

@inproceedings{srivastava2014combined,
  title={Combined task and motion planning through an extensible planner-independent interface layer},
  author={Srivastava, Siddharth and Fang, Eugene and Riano, Lorenzo and Chitnis, Rohan and Russell, Stuart and Abbeel, Pieter},
  booktitle={IEEE International Conference on Robotics and Automation},
  year={2014}
}

@inproceedings{kaelbling2011hierarchical,
  title={Hierarchical task and motion planning in the now},
  author={Kaelbling, Leslie Pack and Lozano-Perez, Tomas},
  booktitle={IEEE International Conference on Robotics and Automation},
  year={2011}
}

@inproceedings{toussaint2015logic,
  title={Logic-geometric programming: An optimization-based approach to combined task and motion planning},
  author={Toussaint, Marc},
  booktitle={International Joint Conference on Artificial Intelligence},
  year={2015}
}

@article{garrett2021pddlstream,
  title={PDDLStream: Integrating symbolic planners and blackbox samplers via optimistic adaptive planning},
  author={Garrett, Caelan Reed and Lozano-Perez, Tomas and Kaelbling, Leslie Pack},
  journal={International Conference on Automated Planning and Scheduling},
  year={2020}
}

@article{krontiris2015dealing,
  title={Dealing with difficult instances of object rearrangement},
  author={Krontiris, Athanasios and Bekris, Kostas E.},
  journal={Robotics: Science and Systems},
  year={2015}
}

@inproceedings{dogar2011pushgrasping,
  title={A framework for push-grasping in clutter},
  author={Dogar, Mehmet R. and Srinivasa, Siddhartha S.},
  booktitle={Robotics: Science and Systems},
  year={2011}
}

@book{ghallab2004automated,
  title={Automated Planning: Theory and Practice},
  author={Ghallab, Malik and Nau, Dana and Traverso, Paolo},
  year={2004},
  publisher={Morgan Kaufmann}
}
"""


def read_rows() -> List[Dict[str, str]]:
    path = DOCS / "related_work_matrix.csv"
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def clean(text: str, limit: int = 500) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:limit]


def top_rows(rows: List[Dict[str, str]], n: int) -> List[Dict[str, str]]:
    return rows[: min(n, len(rows))]


def count_terms(rows: Iterable[Dict[str, str]]) -> Counter:
    counts: Counter = Counter()
    for row in rows:
        for term in (row.get("actual_mechanism_introduced") or "").split(";"):
            term = term.strip()
            if term:
                counts[term] += 1
    return counts


def write_literature_map(rows: List[Dict[str, str]]) -> None:
    years = [int(r["year"]) for r in rows if r.get("year", "").isdigit()]
    mechanisms = count_terms(rows[:300]).most_common(12)
    query_counts = Counter(r["query_source"] for r in rows[:1000]).most_common()
    lines = [
        "# Literature Map",
        "",
        "## Field box",
        "Robotics planning for embodied agents that must navigate and manipulate in spatial environments where actions can change future reachability. The center of mass is task-and-motion planning, navigation among movable obstacles, object rearrangement, mobile manipulation, and sampling/heuristic motion planning.",
        "",
        "## Sweep accounting",
        f"- Landscape sweep: {min(1000, len(rows))} ranked entries in `docs/related_work_matrix.csv`.",
        f"- Serious skim: top {min(300, len(rows))} entries by relevance score.",
        f"- Deep read: top {min(250, len(rows))} entries, using abstract/metadata-grounded extraction columns.",
        f"- Hostile prior-work set: top {min(100, len(rows))} entries most likely to reduce novelty.",
        f"- Year span in collected set: {min(years) if years else 'unknown'}-{max(years) if years else 'unknown'}.",
        "",
        "## Dominant mechanisms observed in the serious skim",
    ]
    for mechanism, count in mechanisms:
        lines.append(f"- {mechanism}: {count}")
    lines += [
        "",
        "## Query sources represented in the landscape",
    ]
    for query, count in query_counts:
        lines.append(f"- `{query}`: {count}")
    lines += [
        "",
        "## Hidden assumptions that may be false",
    ]
    for idx, assumption in enumerate(HIDDEN_ASSUMPTIONS, 1):
        lines.append(f"{idx}. {assumption}")
    lines += [
        "",
        "## Direction candidates that break assumptions",
    ]
    for name, desc in DIRECTIONS:
        lines.append(f"- **{name}.** {desc}")
    lines += [
        "",
        "## Top hostile papers and what they leave open",
    ]
    for i, row in enumerate(top_rows(rows, 30), 1):
        lines += [
            f"### {i}. {clean(row['title'], 160)} ({row.get('year','')})",
            f"- Problem claimed: {clean(row.get('problem_claimed',''))}",
            f"- Mechanism: {clean(row.get('actual_mechanism_introduced',''))}",
            f"- Hidden assumptions: {clean(row.get('hidden_assumptions',''))}",
            f"- Makes less novel: {clean(row.get('what_it_makes_less_novel',''))}",
            f"- Leaves open: {clean(row.get('what_it_leaves_open',''))}",
            "",
        ]
    (DOCS / "literature_map.md").write_text("\n".join(lines), encoding="utf-8")


def write_hostile_prior(rows: List[Dict[str, str]]) -> None:
    lines = [
        "# Hostile Prior Work Set",
        "",
        "This is the 100-paper set most likely to attack novelty. Each entry records the requested extraction fields. The extraction is grounded in title, venue metadata, concepts, and available abstracts in the matrix, not a claim of exhaustive full-text reading.",
        "",
    ]
    for i, row in enumerate(top_rows(rows, 100), 1):
        lines += [
            f"## {i}. {clean(row['title'], 180)}",
            f"- Year/venue: {row.get('year','')} / {clean(row.get('venue',''), 140)}",
            f"- Problem claimed: {clean(row.get('problem_claimed',''), 700)}",
            f"- Actual mechanism introduced: {clean(row.get('actual_mechanism_introduced',''), 500)}",
            f"- Hidden assumptions: {clean(row.get('hidden_assumptions',''), 700)}",
            f"- Variables treated as fixed: {clean(row.get('variables_treated_as_fixed',''), 500)}",
            f"- Failure modes ignored: {clean(row.get('failure_modes_ignored',''), 700)}",
            f"- What it makes less novel: {clean(row.get('what_it_makes_less_novel',''), 500)}",
            f"- What it leaves open: {clean(row.get('what_it_leaves_open',''), 700)}",
            f"- URL: {row.get('url','')}",
            "",
        ]
    (DOCS / "hostile_prior_work.md").write_text("\n".join(lines), encoding="utf-8")


def write_novelty_docs(rows: List[Dict[str, str]]) -> None:
    boundary = [
        "# Novelty Boundary Map",
        "",
        "## What prior work already covers",
        "- Sampling-based motion planning covers continuous feasibility and narrow-passage exploration, so this paper must not claim novelty for finding geometric paths.",
        "- Task-and-motion planning covers symbolic/geometric integration, optimistic sampling, and many forms of geometric precondition checking.",
        "- Navigation among movable obstacles and rearrangement planning cover object movements that open or block access.",
        "- Heuristic graph search covers lifted-state optimality once all irreversible effects are explicitly encoded.",
        "- Belief-space and contingent planning cover uncertainty; uncertainty is not the mechanism here.",
        "",
        "## Boundary this paper claims",
        "The paper claims novelty only for treating irreversible spatial commitments as first-class objects with cut-obligation certificates: crossing a boundary is represented by the set of future obligations it would make unreachable, and the planner reasons over those certificates before crossing.",
        "",
        "## Closest hostile categories",
        "- TAMP systems could encode such preconditions by hand, but they usually do not derive them from spatial reachability cuts.",
        "- Rearrangement planners reason about access blockers, but usually as object-ordering or path-existence constraints rather than reusable commitment objects attached to spatial boundaries.",
        "- Full lifted search can solve the generated benchmark when given exact monotone effects; the contribution is the commitment certificate and pruning/ordering mechanism, not a new completeness result for graph search.",
        "",
        "## Unsupported or deliberately weak claims",
        "- No claim that the method handles deformable contact, stochastic dynamics, or unknown maps.",
        "- No claim of outperforming mature TAMP systems on full robotics benchmarks.",
        "- No claim that cut obligations are the only way to represent irreversible commitments.",
    ]
    (DOCS / "novelty_boundary_map.md").write_text("\n".join(boundary), encoding="utf-8")

    decision = [
        "# Novelty Decision",
        "",
        "## Chosen thesis",
        "Robots should plan with irreversible spatial commitments as first-class objects. A spatial commitment is a directed boundary crossing or placement whose effect is not just local motion cost, but a certificate that some region/approach/obligation becomes unreachable unless discharged beforehand.",
        "",
        "## New central mechanism",
        "Cut-obligation certificates. For each candidate boundary, compute the obligations outside the survivor set that would be lost after crossing. The planner lifts state by the active survivor region and prunes or orders actions whose certificates still carry unpaid obligations.",
        "",
        "## Why this is stronger than the seed",
        "The seed suggested planning with irreversible commitments. The literature sweep points to a sharper contribution: commitments are not just labels or costs; they are boundary-attached certificates that generate ordering constraints and sound search pruning.",
        "",
        "## Why other directions were rejected",
        "- Larger models, additional training data, RL, and LLM planners do not change the central mechanism.",
        "- A benchmark alone would only expose the failure mode.",
        "- A verifier would detect failure after proposing a branch; the proposed mechanism changes what search expands.",
        "- Generic uncertainty handling misidentifies the issue: the benchmark is fully known and still breaks reversible abstractions.",
    ]
    (DOCS / "novelty_decision.md").write_text("\n".join(decision), encoding="utf-8")


def read_summary() -> Dict[str, Dict[str, float]]:
    path = RESULTS / "summary.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_claims_and_attacks(rows: List[Dict[str, str]]) -> None:
    summary = read_summary()
    scp = summary.get("scp_cut_obligations", {})
    exact = summary.get("exact_lifted_astar", {})
    greedy = summary.get("greedy_local", {})
    agenda = summary.get("relaxed_agenda", {})
    comparison = summary.get("comparison", {})
    claims = [
        "# Claims",
        "",
        "## Formal claims",
        "1. In a finite graph with monotone survivor-set effects, a transition that would remove an unserved required object or terminal goal from the survivor set cannot be part of any successful plan. This supports sound pruning by cut-obligation certificates.",
        "2. Lifted search over `(configuration, completed obligations, survivor set)` is complete and cost-optimal for finite nonnegative-cost graphs when using an admissible heuristic; cut-obligation pruning preserves those properties because it only removes provably doomed transitions.",
        "",
        "## Empirical claims supported by this repo",
        f"- SCP success rate in generated tasks: {scp.get('success_rate', float('nan')):.3f}.",
        f"- Exact lifted A* success rate: {exact.get('success_rate', float('nan')):.3f}.",
        f"- Greedy local success rate: {greedy.get('success_rate', float('nan')):.3f}.",
        f"- Relaxed agenda success rate: {agenda.get('success_rate', float('nan')):.3f}.",
        f"- SCP mean expansion fraction of exact A*: {comparison.get('scp_expansion_fraction_of_exact', float('nan')):.3f}.",
        "",
        "## Honest limits",
        "- Evidence is synthetic and targets the mechanism, not real-robot deployment.",
        "- The generator uses monotone zone commitments; richer manipulation contacts can violate this structure.",
        "- Literature extraction is broad and adversarial, but metadata/abstract based.",
    ]
    (DOCS / "claims.md").write_text("\n".join(claims), encoding="utf-8")

    closest = [r["title"] for r in top_rows(rows, 8)]
    attacks = [
        "# Reviewer Attacks",
        "",
        "1. This is just TAMP with another predicate. Response: the boundary predicate is derived from a reachability cut and carries unpaid obligations; it is not hand-authored per action.",
        "2. Full lifted A* already solves the benchmark. Response: yes, when exact irreversible effects are exposed. The contribution is the first-class commitment certificate that exposes and prunes those effects before branch expansion.",
        "3. Navigation among movable obstacles already handles blocked access. Response: hostile NAMO/rearrangement work reduces novelty for access reasoning; the remaining boundary is reusable spatial commitment objects spanning navigation and manipulation obligations.",
        "4. The experiments are synthetic. Response: true; the paper should be viewed as a mechanism paper/workshop-to-revise unless real robot/TAMP benchmarks are added.",
        "5. Cut obligations may be expensive to compute in high-dimensional spaces. Response: the paper only proves finite-graph soundness; practical continuous extraction is future work.",
        "6. Monotonicity is restrictive. Response: deliberately so; it isolates irreversible spatial commitments rather than reversible rearrangements.",
        "",
        "## Closest hostile titles from the sweep",
    ]
    attacks.extend(f"- {title}" for title in closest)
    (DOCS / "reviewer_attacks.md").write_text("\n".join(attacks), encoding="utf-8")


def tex_escape(text: str) -> str:
    text = text or ""
    text = (
        text.replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u00a0", " ")
    )
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    replacements = {
        "\\": "",
        "{": "",
        "}": "",
        "&": "\\&",
        "%": "\\%",
        "$": "\\$",
        "#": "\\#",
        "_": "\\_",
        "~": " ",
        "^": " ",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def bib_entries_from_rows(rows: List[Dict[str, str]], n: int = 45) -> str:
    entries = [MANUAL_BIB.strip()]
    used = set()
    for row in top_rows(rows, n):
        key = re.sub(r"[^A-Za-z0-9]", "", row.get("bib_key_hint", "paper")) or "paper"
        base = key
        suffix = 2
        while key in used:
            key = f"{base}{suffix}"
            suffix += 1
        used.add(key)
        authors = " and ".join(a.strip() for a in row.get("authors", "").split(";")[:6] if a.strip())
        if not authors:
            authors = "Anonymous"
        year = row.get("year") if row.get("year", "").isdigit() else "2025"
        venue = row.get("venue") or "Collected literature"
        doi = row.get("doi", "")
        entry = [
            f"@article{{{key},",
            f"  title={{{tex_escape(row.get('title','Untitled'))}}},",
            f"  author={{{tex_escape(authors)}}},",
            f"  journal={{{tex_escape(venue)}}},",
            f"  year={{{year}}},",
        ]
        if doi:
            entry.append(f"  doi={{{tex_escape(doi.replace('https://doi.org/', ''))}}},")
        entry.append("}")
        entries.append("\n".join(entry))
    return "\n\n".join(entries) + "\n"


def write_bib(rows: List[Dict[str, str]]) -> None:
    PAPER.mkdir(exist_ok=True)
    (PAPER / "references.bib").write_text(bib_entries_from_rows(rows), encoding="utf-8")


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    rows = read_rows()
    write_literature_map(rows)
    write_hostile_prior(rows)
    write_novelty_docs(rows)
    write_claims_and_attacks(rows)
    write_bib(rows)
    print(
        json.dumps(
            {
                "rows": len(rows),
                "docs": [
                    "literature_map.md",
                    "hostile_prior_work.md",
                    "novelty_boundary_map.md",
                    "novelty_decision.md",
                    "claims.md",
                    "reviewer_attacks.md",
                ],
                "bib": "paper/references.bib",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
