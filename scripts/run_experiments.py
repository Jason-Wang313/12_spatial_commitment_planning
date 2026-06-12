"""Run commitment-planning experiments.

The benchmark is deliberately small enough to audit. Each problem is a sequence
of spatial zones linked by irreversible gates. Moving through gate i permanently
removes access to zones <= i. Objects in removed zones are then impossible to
service. This captures the paper's core failure mode: a locally feasible spatial
move can silently destroy a future obligation.
"""

from __future__ import annotations

import csv
import heapq
import json
import math
import random
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
RESULTS.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)


@dataclass(frozen=True)
class Edge:
    to: int
    cost: int
    gate_index: Optional[int] = None


@dataclass
class Episode:
    episode_id: int
    zones: int
    nodes: int
    zone_of: List[int]
    start: int
    goal: int
    object_nodes: List[int]
    graph: Dict[int, List[Edge]]
    relaxed_graph: Dict[int, List[Tuple[int, int]]]
    anchors_in: List[int]
    anchors_out: List[int]


def add_undirected(graph: Dict[int, List[Edge]], relaxed: Dict[int, List[Tuple[int, int]]], a: int, b: int, cost: int = 1) -> None:
    graph[a].append(Edge(b, cost, None))
    graph[b].append(Edge(a, cost, None))
    relaxed[a].append((b, cost))
    relaxed[b].append((a, cost))


def add_gate(graph: Dict[int, List[Edge]], relaxed: Dict[int, List[Tuple[int, int]]], a: int, b: int, gate_index: int, cost: int = 1) -> None:
    graph[a].append(Edge(b, cost, gate_index))
    relaxed[a].append((b, cost))
    relaxed[b].append((a, cost))


def make_episode(rng: random.Random, episode_id: int) -> Episode:
    zones = rng.randint(4, 8)
    zone_sizes = [rng.randint(4, 7) for _ in range(zones)]
    zone_of: List[int] = []
    anchors_in: List[int] = []
    anchors_out: List[int] = []
    graph: Dict[int, List[Edge]] = defaultdict(list)
    relaxed: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
    node = 0
    zone_nodes: List[List[int]] = []
    for z, size in enumerate(zone_sizes):
        nodes = list(range(node, node + size))
        zone_nodes.append(nodes)
        zone_of.extend([z] * size)
        anchors_in.append(nodes[0])
        anchors_out.append(nodes[-1])
        node += size
        for i in range(size - 1):
            add_undirected(graph, relaxed, nodes[i], nodes[i + 1], 1)
        extra_edges = rng.randint(1, max(1, size - 2))
        for _ in range(extra_edges):
            a, b = rng.sample(nodes, 2)
            if abs(a - b) > 1:
                add_undirected(graph, relaxed, a, b, rng.choice([1, 2]))
    for z in range(zones - 1):
        add_gate(graph, relaxed, anchors_out[z], anchors_in[z + 1], z, 1)

    start = anchors_in[0]
    goal = anchors_out[-1]
    object_nodes: List[int] = []
    for z, nodes in enumerate(zone_nodes):
        candidates = [n for n in nodes if n not in {anchors_in[z], anchors_out[z], start, goal}]
        rng.shuffle(candidates)
        count = 1 if z < zones - 1 else rng.choice([0, 1])
        if z in (0, zones - 1):
            count = max(1 if z == 0 else 0, count)
        object_nodes.extend(candidates[:count])
        if rng.random() < 0.35 and len(candidates) > count:
            object_nodes.append(candidates[count])
    # Make early-zone obligations common and a little far from the exit anchor.
    if len(zone_nodes[0]) > 4 and zone_nodes[0][1] not in object_nodes:
        object_nodes.append(zone_nodes[0][1])
    object_nodes = sorted(set(object_nodes), key=lambda n: (zone_of[n], n))
    return Episode(
        episode_id=episode_id,
        zones=zones,
        nodes=node,
        zone_of=zone_of,
        start=start,
        goal=goal,
        object_nodes=object_nodes,
        graph=dict(graph),
        relaxed_graph=dict(relaxed),
        anchors_in=anchors_in,
        anchors_out=anchors_out,
    )


def dijkstra_path(relaxed: Dict[int, List[Tuple[int, int]]], start: int, goal: int) -> Optional[List[int]]:
    frontier = [(0, start)]
    parent = {start: None}
    dist = {start: 0}
    while frontier:
        cost, node = heapq.heappop(frontier)
        if node == goal:
            path = []
            cur: Optional[int] = node
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            return list(reversed(path))
        if cost != dist[node]:
            continue
        for nxt, edge_cost in relaxed.get(node, []):
            new_cost = cost + edge_cost
            if new_cost < dist.get(nxt, 10**9):
                dist[nxt] = new_cost
                parent[nxt] = node
                heapq.heappush(frontier, (new_cost, nxt))
    return None


def relaxed_distance(relaxed: Dict[int, List[Tuple[int, int]]], start: int, goals: Iterable[int]) -> Dict[int, int]:
    goal_set = set(goals)
    dist = {start: 0}
    frontier = [(0, start)]
    found: Dict[int, int] = {}
    while frontier and len(found) < len(goal_set):
        cost, node = heapq.heappop(frontier)
        if cost != dist[node]:
            continue
        if node in goal_set:
            found[node] = cost
        for nxt, edge_cost in relaxed.get(node, []):
            new_cost = cost + edge_cost
            if new_cost < dist.get(nxt, 10**9):
                dist[nxt] = new_cost
                heapq.heappush(frontier, (new_cost, nxt))
    return found


def edge_lookup(ep: Episode) -> Dict[Tuple[int, int], Edge]:
    lookup: Dict[Tuple[int, int], Edge] = {}
    for src, edges in ep.graph.items():
        for edge in edges:
            lookup[(src, edge.to)] = edge
    return lookup


def execute_path(ep: Episode, path: Sequence[int]) -> Tuple[bool, int, int, str]:
    lookup = edge_lookup(ep)
    min_zone = 0
    collected = set()
    cost = 0
    gate_crossings = 0
    for node in path:
        if ep.zone_of[node] < min_zone:
            return False, cost, gate_crossings, "entered_zone_cut_off_by_prior_commitment"
        if node in ep.object_nodes:
            collected.add(node)
    for a, b in zip(path, path[1:]):
        edge = lookup.get((a, b))
        if edge is None:
            return False, cost, gate_crossings, "attempted_reverse_or_nonexistent_committed_edge"
        if ep.zone_of[a] < min_zone or ep.zone_of[b] < min_zone:
            return False, cost, gate_crossings, "traversed_cut_off_region"
        cost += edge.cost
        if edge.gate_index is not None:
            gate_crossings += 1
            min_zone = max(min_zone, edge.gate_index + 1)
        if b in ep.object_nodes:
            collected.add(b)
    if path[-1] != ep.goal:
        return False, cost, gate_crossings, "did_not_reach_goal"
    missed = [n for n in ep.object_nodes if n not in collected]
    if missed:
        return False, cost, gate_crossings, "missed_object_after_commitment"
    return True, cost, gate_crossings, "success"


def greedy_local_plan(ep: Episode) -> Tuple[bool, int, int, int, str]:
    pos = ep.start
    remaining = set(ep.object_nodes)
    full_path = [pos]
    expansions = 0
    while remaining:
        distances = relaxed_distance(ep.relaxed_graph, pos, remaining)
        expansions += len(distances)
        if not distances:
            return False, 0, 0, expansions, "no_relaxed_target_path"
        # Progress-biased local navigation is common when the task endpoint lies
        # deeper in the workspace: a nearby forward object can look better than
        # a slightly farther obligation behind the next irreversible gate.
        target = min(distances, key=lambda n: (distances[n] - 3 * ep.zone_of[n], distances[n], n))
        path = dijkstra_path(ep.relaxed_graph, pos, target)
        if path is None:
            return False, 0, 0, expansions, "no_relaxed_path"
        full_path.extend(path[1:])
        pos = target
        remaining.remove(target)
    path = dijkstra_path(ep.relaxed_graph, pos, ep.goal)
    if path is None:
        return False, 0, 0, expansions, "no_relaxed_goal_path"
    full_path.extend(path[1:])
    ok, cost, gates, reason = execute_path(ep, full_path)
    return ok, cost, gates, expansions, reason


def relaxed_agenda_plan(ep: Episode) -> Tuple[bool, int, int, int, str]:
    # A common abstraction mistake: build an agenda by relaxed proximity to the
    # final route, then execute without promoting irreversible boundaries.
    agenda = sorted(ep.object_nodes, key=lambda n: (abs(ep.zone_of[n] - ep.zones), n))
    pos = ep.start
    full_path = [pos]
    expansions = 0
    for target in agenda + [ep.goal]:
        path = dijkstra_path(ep.relaxed_graph, pos, target)
        expansions += ep.nodes
        if path is None:
            return False, 0, 0, expansions, "no_relaxed_path"
        full_path.extend(path[1:])
        pos = target
    ok, cost, gates, reason = execute_path(ep, full_path)
    return ok, cost, gates, expansions, reason


def heuristic(ep: Episode, pos: int, collected_mask: int) -> int:
    remaining = [n for i, n in enumerate(ep.object_nodes) if not (collected_mask & (1 << i))]
    targets = remaining if remaining else [ep.goal]
    distances = relaxed_distance(ep.relaxed_graph, pos, targets)
    return min(distances.values()) if distances else 0


def exact_search(
    ep: Episode,
    use_commitment_pruning: bool,
    certificate_map: Optional[Dict[int, Set[int]]] = None,
) -> Tuple[bool, int, int, int, int, str]:
    object_index = {n: i for i, n in enumerate(ep.object_nodes)}
    full_mask = (1 << len(ep.object_nodes)) - 1
    start_mask = 0
    if ep.start in object_index:
        start_mask |= 1 << object_index[ep.start]
    start = (ep.start, start_mask, 0)
    frontier = [(heuristic(ep, ep.start, start_mask), 0, start)]
    best = {start: 0}
    expansions = 0
    pruned = 0
    while frontier:
        _, cost, state = heapq.heappop(frontier)
        pos, mask, min_zone = state
        if cost != best[state]:
            continue
        expansions += 1
        if pos == ep.goal and mask == full_mask:
            return True, cost, 0, expansions, pruned, "success"
        for edge in ep.graph.get(pos, []):
            nxt = edge.to
            if ep.zone_of[nxt] < min_zone:
                continue
            next_min_zone = min_zone
            if edge.gate_index is not None:
                next_min_zone = max(next_min_zone, edge.gate_index + 1)
                if use_commitment_pruning:
                    blocked = False
                    certified = certificate_map.get(edge.gate_index, set()) if certificate_map is not None else None
                    for idx, obj in enumerate(ep.object_nodes):
                        if mask & (1 << idx):
                            continue
                        if certified is not None:
                            blocks_obj = idx in certified
                        else:
                            blocks_obj = ep.zone_of[obj] < next_min_zone
                        if blocks_obj:
                            blocked = True
                            break
                    if blocked:
                        pruned += 1
                        continue
            next_mask = mask
            if nxt in object_index:
                next_mask |= 1 << object_index[nxt]
            new_state = (nxt, next_mask, next_min_zone)
            new_cost = cost + edge.cost
            if new_cost < best.get(new_state, 10**12):
                best[new_state] = new_cost
                priority = new_cost + heuristic(ep, nxt, next_mask)
                heapq.heappush(frontier, (priority, new_cost, new_state))
    return False, 0, 0, expansions, pruned, "search_exhausted"


def commitment_certificate_count(ep: Episode) -> int:
    count = 0
    for gate in range(ep.zones - 1):
        blocked_objects = [n for n in ep.object_nodes if ep.zone_of[n] <= gate]
        if blocked_objects:
            count += 1
    return count


def build_certificate_map(
    ep: Episode,
    rng: random.Random,
    false_negative_rate: float = 0.0,
    false_positive_rate: float = 0.0,
) -> Dict[int, Set[int]]:
    certificate_map: Dict[int, Set[int]] = {}
    for gate in range(ep.zones - 1):
        included: Set[int] = set()
        for idx, obj in enumerate(ep.object_nodes):
            truly_blocked = ep.zone_of[obj] <= gate
            if truly_blocked and rng.random() >= false_negative_rate:
                included.add(idx)
            if (not truly_blocked) and rng.random() < false_positive_rate:
                included.add(idx)
        certificate_map[gate] = included
    return certificate_map


def run(seed: int = 12, episodes: int = 240) -> List[Dict[str, object]]:
    rng = random.Random(seed)
    rows: List[Dict[str, object]] = []
    for episode_id in range(episodes):
        ep = make_episode(rng, episode_id)
        certs = commitment_certificate_count(ep)
        methods = {
            "greedy_local": greedy_local_plan(ep),
            "relaxed_agenda": relaxed_agenda_plan(ep),
        }
        for method, result in methods.items():
            ok, cost, gates, expansions, reason = result
            rows.append(
                {
                    "episode_id": episode_id,
                    "method": method,
                    "success": int(ok),
                    "cost": cost if ok else "",
                    "gate_crossings": gates,
                    "expansions": expansions,
                    "pruned_commitments": 0,
                    "zones": ep.zones,
                    "nodes": ep.nodes,
                    "objects": len(ep.object_nodes),
                    "certificates": certs,
                    "failure_reason": reason,
                }
            )
        ok, cost, gates, expansions, pruned, reason = exact_search(ep, False)
        rows.append(
            {
                "episode_id": episode_id,
                "method": "exact_lifted_astar",
                "success": int(ok),
                "cost": cost if ok else "",
                "gate_crossings": "",
                "expansions": expansions,
                "pruned_commitments": pruned,
                "zones": ep.zones,
                "nodes": ep.nodes,
                "objects": len(ep.object_nodes),
                "certificates": certs,
                "failure_reason": reason,
            }
        )
        ok, cost, gates, expansions, pruned, reason = exact_search(ep, True)
        rows.append(
            {
                "episode_id": episode_id,
                "method": "scp_cut_obligations",
                "success": int(ok),
                "cost": cost if ok else "",
                "gate_crossings": "",
                "expansions": expansions,
                "pruned_commitments": pruned,
                "zones": ep.zones,
                "nodes": ep.nodes,
                "objects": len(ep.object_nodes),
                "certificates": certs,
                "failure_reason": reason,
            }
        )
        if (episode_id + 1) % 40 == 0:
            print(f"[experiments] completed {episode_id + 1}/{episodes} episodes")
    return rows


def summarize(rows: List[Dict[str, object]]) -> Dict[str, Dict[str, float]]:
    by_method: Dict[str, List[Dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_method[str(row["method"])].append(row)
    summary: Dict[str, Dict[str, float]] = {}
    for method, items in sorted(by_method.items()):
        successes = [r for r in items if int(r["success"]) == 1]
        costs = [float(r["cost"]) for r in successes if r["cost"] != ""]
        expansions = [float(r["expansions"]) for r in items]
        pruned = [float(r["pruned_commitments"]) for r in items]
        summary[method] = {
            "episodes": float(len(items)),
            "success_rate": len(successes) / max(1, len(items)),
            "mean_cost_successes": sum(costs) / max(1, len(costs)),
            "mean_expansions": sum(expansions) / max(1, len(expansions)),
            "mean_pruned_commitments": sum(pruned) / max(1, len(pruned)),
        }
    exact = summary.get("exact_lifted_astar", {}).get("mean_expansions", 0.0)
    scp = summary.get("scp_cut_obligations", {}).get("mean_expansions", 0.0)
    if exact and scp:
        summary["comparison"] = {
            "scp_expansion_fraction_of_exact": scp / exact,
            "scp_expansion_reduction_percent": 100.0 * (1.0 - scp / exact),
        }
    return summary


def certificate_noise_stress(seed: int = 1212, episodes: int = 240) -> List[Dict[str, object]]:
    episode_rng = random.Random(seed)
    episodes_list = [make_episode(episode_rng, episode_id) for episode_id in range(episodes)]
    configs = [("false_negative", r) for r in [0.0, 0.25, 0.50, 0.75, 1.0]]
    configs.extend(("false_positive", r) for r in [0.0, 0.01, 0.02, 0.05, 0.10])
    rows: List[Dict[str, object]] = []
    for corruption_type, rate in configs:
        successes = 0
        expansions: List[float] = []
        pruned: List[float] = []
        for ep in episodes_list:
            cert_rng = random.Random(seed + ep.episode_id * 7919 + int(rate * 10000) + (0 if corruption_type == "false_negative" else 500000))
            certificate_map = build_certificate_map(
                ep,
                cert_rng,
                false_negative_rate=rate if corruption_type == "false_negative" else 0.0,
                false_positive_rate=rate if corruption_type == "false_positive" else 0.0,
            )
            ok, _cost, _gates, expanded, pruned_count, _reason = exact_search(ep, True, certificate_map)
            successes += int(ok)
            expansions.append(float(expanded))
            pruned.append(float(pruned_count))
        rows.append(
            {
                "corruption_type": corruption_type,
                "rate": rate,
                "episodes": episodes,
                "success_rate": successes / episodes,
                "mean_expansions": sum(expansions) / episodes,
                "mean_pruned_commitments": sum(pruned) / episodes,
            }
        )
    return rows


def write_certificate_noise_table(rows: List[Dict[str, object]]) -> None:
    lines = [
        "\\begin{tabular}{llrrr}",
        "\\toprule",
        "Corruption & Rate & Success & Mean expansions & Pruned \\\\",
        "\\midrule",
    ]
    labels = {"false_negative": "False negative", "false_positive": "False positive"}
    for row in rows:
        lines.append(
            f"{labels[str(row['corruption_type'])]} & {100 * float(row['rate']):.0f}\\% & "
            f"{float(row['success_rate']):.3f} & {float(row['mean_expansions']):.1f} & "
            f"{float(row['mean_pruned_commitments']):.1f} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (RESULTS / "certificate_noise_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_outputs(rows: List[Dict[str, object]]) -> None:
    fields = [
        "episode_id",
        "method",
        "success",
        "cost",
        "gate_crossings",
        "expansions",
        "pruned_commitments",
        "zones",
        "nodes",
        "objects",
        "certificates",
        "failure_reason",
    ]
    out_csv = RESULTS / "episode_results.csv"
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    summary = summarize(rows)
    (RESULTS / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    certificate_rows = certificate_noise_stress()
    with (RESULTS / "certificate_noise_summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "corruption_type",
                "rate",
                "episodes",
                "success_rate",
                "mean_expansions",
                "mean_pruned_commitments",
            ],
        )
        writer.writeheader()
        writer.writerows(certificate_rows)
    write_certificate_noise_table(certificate_rows)
    print(json.dumps(summary, indent=2))
    try:
        import matplotlib.pyplot as plt

        methods = [m for m in summary.keys() if m != "comparison"]
        labels = {
            "greedy_local": "Greedy",
            "relaxed_agenda": "Relaxed agenda",
            "exact_lifted_astar": "Exact A*",
            "scp_cut_obligations": "SCP",
        }
        fig, ax = plt.subplots(figsize=(6.4, 3.4))
        ax.bar([labels.get(m, m) for m in methods], [summary[m]["success_rate"] for m in methods])
        ax.set_ylim(0, 1.05)
        ax.set_ylabel("success rate")
        ax.set_title("Irreversible spatial commitments strand deferred obligations")
        ax.tick_params(axis="x", rotation=15)
        fig.tight_layout()
        fig.savefig(FIGURES / "success_rates.pdf")
        fig.savefig(FIGURES / "success_rates.png", dpi=180)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(6.4, 3.4))
        ax.bar([labels.get(m, m) for m in methods], [summary[m]["mean_expansions"] for m in methods])
        ax.set_ylabel("mean search expansions / probes")
        ax.set_title("Commitment cuts prune doomed branches before search spends them")
        ax.tick_params(axis="x", rotation=15)
        fig.tight_layout()
        fig.savefig(FIGURES / "expansions.pdf")
        fig.savefig(FIGURES / "expansions.png", dpi=180)
        plt.close(fig)
    except Exception as exc:
        (FIGURES / "plot_failure.txt").write_text(str(exc), encoding="utf-8")
        print(f"[warn] plotting failed: {exc}")


def main() -> None:
    rows = run()
    write_outputs(rows)


if __name__ == "__main__":
    main()
