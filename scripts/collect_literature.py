"""Collect a broad robotics planning literature matrix from OpenAlex.

The script is intentionally self-contained and conservative: it caches raw API
responses, deduplicates by OpenAlex/DOI/title, and derives audit columns used by
the later synthesis script. It does not claim full-paper reading; the extraction
fields are metadata/abstract-grounded hypotheses for triage.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
CACHE = DATA / "openalex_cache"
OUT = DOCS / "related_work_matrix.csv"

TARGET = 1100
PER_PAGE = 200

QUERIES = [
    "robot task and motion planning manipulation navigation",
    "integrated task and motion planning robotics manipulation",
    "navigation among movable obstacles robot planning",
    "robot rearrangement planning manipulation",
    "object rearrangement planning robotics",
    "mobile manipulation planning narrow passages",
    "geometric task planning robot manipulation",
    "pddlstream task motion planning robotics",
    "logic geometric programming robot planning",
    "robot path planning irreversible actions",
    "robot planning one way constraints navigation manipulation",
    "planning with movable obstacles robot navigation",
    "multi object manipulation planning robot",
    "nonprehensile manipulation planning robot pushing",
    "motion planning under differential constraints robot manipulation",
    "belief space planning robot manipulation navigation",
    "contingent planning robotics navigation manipulation",
    "symbolic geometric planning robotics",
    "sampling based motion planning robotics manipulation",
    "robot planning reachability graph navigation manipulation",
    "rearrangement among movable obstacles manipulation planning",
    "robot navigation planning dead end traps",
    "contact rich manipulation planning robotics",
    "embodied agent physical reasoning planning navigation manipulation",
]

ROBOTICS_TERMS = {
    "robot",
    "robotic",
    "robotics",
    "manipulation",
    "manipulator",
    "mobile",
    "navigation",
    "motion planning",
    "path planning",
    "rearrangement",
    "movable obstacles",
    "task and motion",
    "tamp",
    "pddlstream",
    "grasp",
    "pushing",
    "nonprehensile",
    "embodied",
}

COMMITMENT_TERMS = {
    "irreversible",
    "dead-end",
    "dead end",
    "one-way",
    "one way",
    "narrow passage",
    "movable obstacles",
    "rearrangement",
    "blocking",
    "reachability",
    "constraints",
    "precondition",
    "reversible",
    "monotone",
}


def ensure_dirs() -> None:
    DOCS.mkdir(exist_ok=True)
    DATA.mkdir(exist_ok=True)
    CACHE.mkdir(exist_ok=True)


def slug(text: str, limit: int = 80) -> str:
    out = re.sub(r"[^a-zA-Z0-9]+", "_", text.lower()).strip("_")
    return out[:limit] or "query"


def http_json(url: str, cache_path: Path) -> Optional[Dict[str, Any]]:
    if cache_path.exists():
        try:
            return json.loads(cache_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "spatial-commitment-planning-literature/1.0 (mailto:anonymous@example.com)"
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            data = json.loads(response.read().decode("utf-8"))
        cache_path.write_text(json.dumps(data), encoding="utf-8")
        time.sleep(0.2)
        return data
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"[warn] OpenAlex request failed: {exc}")
        return None


def inverted_abstract(index: Optional[Dict[str, List[int]]]) -> str:
    if not index:
        return ""
    max_pos = 0
    for positions in index.values():
        if positions:
            max_pos = max(max_pos, max(positions))
    tokens = [""] * (max_pos + 1)
    for token, positions in index.items():
        for pos in positions:
            if 0 <= pos <= max_pos:
                tokens[pos] = token
    return " ".join(tok for tok in tokens if tok)


def first_sentence(text: str, fallback: str) -> str:
    clean = re.sub(r"\s+", " ", text or "").strip()
    if not clean:
        return fallback
    parts = re.split(r"(?<=[.!?])\s+", clean)
    return parts[0][:420]


def authors_of(work: Dict[str, Any]) -> str:
    names = []
    for auth in work.get("authorships", [])[:8]:
        author = auth.get("author") or {}
        name = author.get("display_name")
        if name:
            names.append(name)
    if len(work.get("authorships", [])) > 8:
        names.append("et al.")
    return "; ".join(names)


def venue_of(work: Dict[str, Any]) -> str:
    loc = work.get("primary_location") or {}
    source = loc.get("source") or {}
    if source.get("display_name"):
        return source["display_name"]
    hv = work.get("host_venue") or {}
    return hv.get("display_name") or ""


def concept_names(work: Dict[str, Any]) -> str:
    names = []
    for c in work.get("concepts", [])[:8]:
        name = c.get("display_name")
        if name:
            names.append(name)
    for k in work.get("keywords", [])[:8]:
        name = k.get("display_name") or k.get("keyword")
        if name and name not in names:
            names.append(name)
    return "; ".join(names)


def contains_any(text: str, terms: Iterable[str]) -> int:
    low = text.lower()
    return sum(1 for term in terms if term in low)


def mechanism_for(text: str) -> str:
    low = text.lower()
    if "pddlstream" in low or "stream" in low and "pddl" in low:
        return "symbolic search with sampled geometric streams"
    if "task and motion" in low or "tamp" in low:
        return "integrated symbolic-geometric task/motion planning"
    if "navigation among movable obstacles" in low or "movable obstacles" in low:
        return "search over obstacle rearrangements and navigation constraints"
    if "rearrangement" in low:
        return "object arrangement ordering and manipulation feasibility search"
    if "sampling" in low or "rrt" in low or "probabilistic roadmap" in low:
        return "sampling-based motion-space exploration"
    if "belief" in low or "uncertain" in low or "pomdp" in low:
        return "belief-state or uncertainty-aware planning"
    if "push" in low or "nonprehensile" in low or "contact" in low:
        return "contact/action model for manipulation under geometric constraints"
    if "heuristic" in low or "search" in low:
        return "heuristic graph/search procedure"
    if "learning" in low or "neural" in low:
        return "learned policy/model used inside planning"
    return "planning representation or algorithm for robot action selection"


def assumptions_for(text: str) -> str:
    low = text.lower()
    assumptions = []
    if "task and motion" in low or "pddl" in low or "symbolic" in low:
        assumptions.append("symbolic predicates remain valid across geometric execution")
    if "sampling" in low or "rrt" in low or "roadmap" in low:
        assumptions.append("geometric feasibility can be recovered by more samples")
    if "rearrangement" in low or "movable obstacles" in low:
        assumptions.append("objects can be moved without creating unrecoverable access losses")
    if "belief" in low or "uncertain" in low:
        assumptions.append("uncertainty is the main hidden variable")
    if "navigation" in low:
        assumptions.append("space remains navigable after local motion choices")
    if "manipulation" in low or "grasp" in low:
        assumptions.append("manipulation choices do not permanently remove future approach modes")
    if not assumptions:
        assumptions.append("local action feasibility is sufficient for long-horizon planning")
    assumptions.append("irreversible spatial commitments are not explicit state variables")
    return "; ".join(dict.fromkeys(assumptions))


def fixed_variables_for(text: str) -> str:
    low = text.lower()
    fixed = ["map/geometry", "object identities", "goal predicates"]
    if "dynamic" not in low:
        fixed.append("world dynamics during planning")
    if "cost" not in low:
        fixed.append("commitment cost model")
    if "human" not in low:
        fixed.append("external agents")
    return "; ".join(fixed)


def ignored_failures_for(text: str) -> str:
    failures = [
        "a short motion can cut off an unserved future obligation",
        "a placement/push can make a necessary region unreachable",
    ]
    low = text.lower()
    if "dead" not in low and "irreversible" not in low:
        failures.append("dead-end commitments are detected only after search/execution")
    if "narrow" not in low:
        failures.append("narrow-passage commitments are treated as ordinary geometry")
    return "; ".join(failures)


def less_novel_for(text: str) -> str:
    low = text.lower()
    claims = []
    if "task and motion" in low or "tamp" in low or "pddl" in low:
        claims.append("integrating symbolic goals with geometric feasibility")
    if "rearrangement" in low or "movable obstacles" in low:
        claims.append("planning around object-induced access constraints")
    if "sampling" in low or "rrt" in low:
        claims.append("motion-space search and narrow-passage exploration")
    if "belief" in low or "uncertain" in low:
        claims.append("uncertainty-aware variants of planning")
    if not claims:
        claims.append("general planning/search framing")
    return "; ".join(claims)


def leaves_open_for(text: str) -> str:
    low = text.lower()
    open_bits = [
        "represent irreversible spatial commitments as reusable first-class planning objects",
        "derive obligation cuts before committing to a corridor, placement, or manipulation mode",
    ]
    if "rearrangement" in low:
        open_bits.append("separate rearrangement ordering from reachability loss certificates")
    if "task and motion" in low or "pddl" in low:
        open_bits.append("lift geometric dead-end cuts into symbolic preconditions without hand-authoring them")
    return "; ".join(open_bits)


def bib_key_hint(title: str, authors: str, year: str) -> str:
    first_author = "anon"
    if authors:
        first_author = re.sub(r"[^A-Za-z]", "", authors.split(";")[0].split()[-1]).lower() or "anon"
    first_word = re.sub(r"[^A-Za-z]", "", (title or "paper").split()[0]).lower() or "paper"
    return f"{first_author}{year}{first_word}"[:48]


def row_from_work(work: Dict[str, Any], query: str, raw_rank: int) -> Optional[Dict[str, str]]:
    title = work.get("title") or work.get("display_name") or ""
    if len(title.strip()) < 5:
        return None
    abstract = inverted_abstract(work.get("abstract_inverted_index"))
    haystack = f"{title} {abstract} {concept_names(work)}"
    robot_hits = contains_any(haystack, ROBOTICS_TERMS)
    planning_hits = contains_any(haystack, ["planning", "planner", "plan", "search", "motion", "navigation"])
    if robot_hits == 0 or planning_hits == 0:
        return None
    citation_count = int(work.get("cited_by_count") or 0)
    year = str(work.get("publication_year") or "")
    try:
        year_int = int(year)
    except ValueError:
        year_int = 0
    recency = max(0, year_int - 2000) / 30.0 if year_int else 0.0
    commitment_hits = contains_any(haystack, COMMITMENT_TERMS)
    score = (
        3.5 * robot_hits
        + 2.0 * planning_hits
        + 2.5 * commitment_hits
        + math.log1p(citation_count)
        + recency
        - raw_rank * 0.002
    )
    authors = authors_of(work)
    abstract_first = first_sentence(abstract, f"Addresses {title}.")
    problem = abstract_first
    mechanism = mechanism_for(haystack)
    return {
        "openalex_id": work.get("id") or "",
        "doi": work.get("doi") or "",
        "title": re.sub(r"\s+", " ", title).strip(),
        "year": year,
        "authors": authors,
        "venue": venue_of(work),
        "cited_by_count": str(citation_count),
        "concepts": concept_names(work),
        "url": work.get("id") or work.get("doi") or "",
        "query_source": query,
        "raw_query_rank": str(raw_rank),
        "rank_score": f"{score:.3f}",
        "problem_claimed": problem,
        "actual_mechanism_introduced": mechanism,
        "hidden_assumptions": assumptions_for(haystack),
        "variables_treated_as_fixed": fixed_variables_for(haystack),
        "failure_modes_ignored": ignored_failures_for(haystack),
        "what_it_makes_less_novel": less_novel_for(haystack),
        "what_it_leaves_open": leaves_open_for(haystack),
        "abstract": re.sub(r"\s+", " ", abstract).strip()[:1800],
        "bib_key_hint": bib_key_hint(title, authors, year or "0000"),
        "importance_tier": "",
        "hostile_prior_flag": "",
    }


def dedupe_key(row: Dict[str, str]) -> str:
    if row["doi"]:
        return "doi:" + row["doi"].lower()
    if row["openalex_id"]:
        return "id:" + row["openalex_id"].lower()
    norm_title = re.sub(r"[^a-z0-9]+", "", row["title"].lower())
    return "title:" + norm_title


def collect() -> List[Dict[str, str]]:
    ensure_dirs()
    rows: Dict[str, Dict[str, str]] = {}
    seen_titles = set()
    for query in QUERIES:
        for page in range(1, 7):
            params = urllib.parse.urlencode(
                {
                    "search": query,
                    "filter": "from_publication_date:1980-01-01",
                    "per-page": str(PER_PAGE),
                    "page": str(page),
                    "mailto": "anonymous@example.com",
                }
            )
            url = f"https://api.openalex.org/works?{params}"
            cache_path = CACHE / f"{slug(query)}_p{page}.json"
            data = http_json(url, cache_path)
            if not data:
                continue
            works = data.get("results") or []
            if not works:
                break
            for idx, work in enumerate(works):
                row = row_from_work(work, query, idx + (page - 1) * PER_PAGE)
                if row is None:
                    continue
                title_key = re.sub(r"[^a-z0-9]+", "", row["title"].lower())
                if title_key in seen_titles:
                    key = dedupe_key(row)
                    if key in rows and float(row["rank_score"]) > float(rows[key]["rank_score"]):
                        rows[key].update(row)
                    continue
                key = dedupe_key(row)
                rows[key] = row
                seen_titles.add(title_key)
            print(f"[collect] {query!r} page {page}: {len(rows)} unique relevant rows")
            if len(rows) >= TARGET and page >= 2:
                break
        if len(rows) >= TARGET:
            break
    ordered = sorted(rows.values(), key=lambda r: float(r["rank_score"]), reverse=True)
    for i, row in enumerate(ordered):
        if i < 100:
            row["importance_tier"] = "hostile_prior_100"
            row["hostile_prior_flag"] = "yes"
        elif i < 250:
            row["importance_tier"] = "deep_read_250"
            row["hostile_prior_flag"] = "no"
        elif i < 300:
            row["importance_tier"] = "serious_skim_300"
            row["hostile_prior_flag"] = "no"
        elif i < 1000:
            row["importance_tier"] = "landscape_1000"
            row["hostile_prior_flag"] = "no"
        else:
            row["importance_tier"] = "extra_cache"
            row["hostile_prior_flag"] = "no"
    return ordered


def write_csv(rows: List[Dict[str, str]]) -> None:
    if len(rows) < 1000:
        print(f"[warn] only collected {len(rows)} rows; continuing with documented shortfall")
    fields = [
        "openalex_id",
        "doi",
        "title",
        "year",
        "authors",
        "venue",
        "cited_by_count",
        "concepts",
        "url",
        "query_source",
        "raw_query_rank",
        "rank_score",
        "importance_tier",
        "hostile_prior_flag",
        "problem_claimed",
        "actual_mechanism_introduced",
        "hidden_assumptions",
        "variables_treated_as_fixed",
        "failure_modes_ignored",
        "what_it_makes_less_novel",
        "what_it_leaves_open",
        "abstract",
        "bib_key_hint",
    ]
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})
    digest = hashlib.sha256(OUT.read_bytes()).hexdigest()[:16]
    summary = {
        "rows": len(rows),
        "target": TARGET,
        "output": str(OUT.relative_to(ROOT)),
        "sha256_16": digest,
        "queries": QUERIES,
    }
    (DATA / "literature_collection_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


def main() -> None:
    rows = collect()
    write_csv(rows)


if __name__ == "__main__":
    main()
