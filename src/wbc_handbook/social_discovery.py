"""Persistent, user-triggered discovery ledger and query-frontier evolution.

The ledger prevents an on-demand social update from blindly replaying the same
queries.  It records canonical URLs, per-query yield, blockers, and an
exponential no-new-result backoff.  The frontier turns recurring technical
entities found in post bodies and comments into evidence-linked search
proposals.  Nothing in this module schedules background work.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
import hashlib
import re
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


DISCOVERY_STATE_SCHEMA_VERSION = 1
FRONTIER_SCHEMA_VERSION = 2
MAX_LEDGER_RUNS = 100


class SocialDiscoveryError(ValueError):
    """Raised when a discovery state or frontier violates its contract."""


def _now(value: Optional[datetime] = None) -> datetime:
    current = value or datetime.now(timezone.utc).astimezone()
    if current.tzinfo is None:
        raise SocialDiscoveryError("timestamp must include a timezone")
    return current


def _iso(value: Optional[datetime] = None) -> str:
    return _now(value).isoformat(timespec="seconds")


def _parse_iso(value: Any, name: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise SocialDiscoveryError(f"{name} must be an ISO 8601 string")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise SocialDiscoveryError(f"{name} must be ISO 8601") from exc
    if parsed.tzinfo is None:
        raise SocialDiscoveryError(f"{name} must include a timezone")
    return parsed


def normalize_query_text(value: Any) -> str:
    """Return a stable comparison form without changing the executed query."""

    if not isinstance(value, str) or not value.strip():
        raise SocialDiscoveryError("query must be a non-empty string")
    return re.sub(r"\s+", " ", value.strip()).casefold()


def query_signature(platform: str, scope_id: str, query: str) -> str:
    payload = "\t".join((platform.strip().lower(), scope_id, normalize_query_text(query)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:24]


def empty_discovery_state(created_at: Optional[datetime] = None) -> Dict[str, Any]:
    created = _iso(created_at)
    return {
        "schema_version": DISCOVERY_STATE_SCHEMA_VERSION,
        "created_at": created,
        "updated_at": created,
        "queries": {},
        "known_urls": {},
        "runs": [],
    }


def _normalized_state(
    state: Optional[Mapping[str, Any]], *, now: Optional[datetime] = None
) -> Dict[str, Any]:
    if not state:
        return empty_discovery_state(now)
    if not isinstance(state, Mapping):
        raise SocialDiscoveryError("discovery state must be an object")
    if state.get("schema_version") != DISCOVERY_STATE_SCHEMA_VERSION:
        raise SocialDiscoveryError(
            f"discovery state schema_version must be {DISCOVERY_STATE_SCHEMA_VERSION}"
        )
    queries = state.get("queries", {})
    known_urls = state.get("known_urls", {})
    runs = state.get("runs", [])
    if not isinstance(queries, Mapping) or not isinstance(known_urls, Mapping):
        raise SocialDiscoveryError("discovery queries/known_urls must be objects")
    if not isinstance(runs, list):
        raise SocialDiscoveryError("discovery runs must be a list")
    normalized = dict(state)
    normalized["queries"] = {str(key): dict(value) for key, value in queries.items()}
    normalized["known_urls"] = {
        str(key): dict(value) for key, value in known_urls.items()
    }
    normalized["runs"] = [dict(value) for value in runs if isinstance(value, Mapping)]
    return normalized


def _query_platforms(item: Mapping[str, Any], default_platforms: Sequence[str]) -> List[str]:
    platforms = item.get("platforms", default_platforms)
    if not isinstance(platforms, Sequence) or isinstance(platforms, (str, bytes)):
        raise SocialDiscoveryError("query platforms must be a list")
    normalized = []
    for value in platforms:
        if not isinstance(value, str) or not value.strip():
            raise SocialDiscoveryError("query platform must be a non-empty string")
        platform = value.strip().lower()
        if platform not in normalized:
            normalized.append(platform)
    return normalized


def select_incremental_queries(
    queries: Sequence[Mapping[str, Any]],
    *,
    platforms: Sequence[str],
    state: Optional[Mapping[str, Any]] = None,
    max_queries_per_platform: int = 8,
    min_repeat_hours: int = 24,
    force: bool = False,
    selected_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Select a diverse, low-repeat query set for one on-demand run.

    Never-run queries are selected first.  A query that repeatedly produces no
    new canonical URLs receives an exponential backoff capped at 30 days.  The
    selector then round-robins scopes so one broad scope cannot consume the
    whole platform budget.
    """

    if not 1 <= max_queries_per_platform <= 100:
        raise SocialDiscoveryError("max_queries_per_platform must be in [1, 100]")
    if not 0 <= min_repeat_hours <= 24 * 30:
        raise SocialDiscoveryError("min_repeat_hours must be in [0, 720]")
    current = _now(selected_at)
    normalized_state = _normalized_state(state, now=current)
    query_state = normalized_state["queries"]
    platform_order = list(dict.fromkeys(value.lower() for value in platforms))
    candidates: Dict[str, List[Dict[str, Any]]] = {value: [] for value in platform_order}
    skipped: List[Dict[str, Any]] = []
    seen_signatures = set()

    for index, item in enumerate(queries):
        if not isinstance(item, Mapping):
            raise SocialDiscoveryError(f"queries[{index}] must be an object")
        scope_id = item.get("scope_id")
        query = item.get("query")
        if not isinstance(scope_id, str) or not re.fullmatch(
            r"[a-z0-9][a-z0-9_]{2,63}", scope_id
        ):
            raise SocialDiscoveryError(f"queries[{index}].scope_id is invalid")
        normalize_query_text(query)
        for platform in _query_platforms(item, platform_order):
            if platform not in candidates:
                continue
            signature = query_signature(platform, scope_id, query)
            if signature in seen_signatures:
                skipped.append({
                    "platform": platform,
                    "scope_id": scope_id,
                    "query": query,
                    "query_signature": signature,
                    "reason": "duplicate_query_signature",
                })
                continue
            seen_signatures.add(signature)
            history = query_state.get(signature, {})
            no_new_streak = int(history.get("no_new_streak", 0) or 0)
            run_count = int(history.get("run_count", 0) or 0)
            next_eligible = history.get("next_eligible_at")
            eligible = True
            if next_eligible and not force:
                eligible = _parse_iso(next_eligible, "next_eligible_at") <= current
            record = {
                **{key: value for key, value in item.items() if key != "platforms"},
                "platforms": [platform],
                "query_signature": signature,
                "selection_history": {
                    "run_count": run_count,
                    "no_new_streak": no_new_streak,
                    "last_new_urls": int(history.get("last_new_urls", 0) or 0),
                },
            }
            if not eligible:
                skipped.append({
                    "platform": platform,
                    "scope_id": scope_id,
                    "query": query,
                    "query_signature": signature,
                    "reason": "backoff_not_elapsed",
                    "next_eligible_at": next_eligible,
                })
                continue
            origin_priority = 0 if item.get("origin") == "frontier" else 1
            last_completed = history.get("last_completed_at") or ""
            last_new_urls = int(history.get("last_new_urls", 0) or 0)
            record["_priority"] = (
                0 if run_count == 0 else 1 if last_new_urls > 0 else 2,
                origin_priority,
                last_completed,
                run_count,
                signature,
            )
            candidates[platform].append(record)

    selected: List[Dict[str, Any]] = []
    per_platform_counts: Dict[str, int] = {}
    for platform in platform_order:
        ordered = sorted(candidates[platform], key=lambda value: value["_priority"])
        scope_buckets: Dict[str, List[Dict[str, Any]]] = {}
        scope_order: List[str] = []
        for record in ordered:
            scope = record["scope_id"]
            if scope not in scope_buckets:
                scope_buckets[scope] = []
                scope_order.append(scope)
            scope_buckets[scope].append(record)
        chosen: List[Dict[str, Any]] = []
        while len(chosen) < max_queries_per_platform and any(scope_buckets.values()):
            for scope in scope_order:
                if len(chosen) >= max_queries_per_platform:
                    break
                bucket = scope_buckets[scope]
                if bucket:
                    chosen.append(bucket.pop(0))
        chosen_signatures = {value["query_signature"] for value in chosen}
        for record in ordered:
            if record["query_signature"] not in chosen_signatures:
                skipped.append({
                    "platform": platform,
                    "scope_id": record["scope_id"],
                    "query": record["query"],
                    "query_signature": record["query_signature"],
                    "reason": "platform_budget",
                })
        for record in chosen:
            record.pop("_priority", None)
            selected.append(record)
        per_platform_counts[platform] = len(chosen)

    return {
        "schema_version": 1,
        "selected_at": _iso(current),
        "force": force,
        "min_repeat_hours": min_repeat_hours,
        "max_queries_per_platform": max_queries_per_platform,
        "selected": selected,
        "skipped": skipped,
        "counts": {
            "input_queries": len(queries),
            "selected": len(selected),
            "skipped": len(skipped),
            "per_platform": per_platform_counts,
        },
    }


def update_discovery_state(
    plan: Mapping[str, Any],
    result: Mapping[str, Any],
    *,
    previous_state: Optional[Mapping[str, Any]] = None,
    updated_at: Optional[datetime] = None,
    min_repeat_hours: int = 24,
) -> Dict[str, Any]:
    """Update query yield and URL history from a normalized browser run."""

    current = _now(updated_at)
    state = _normalized_state(previous_state, now=current)
    tasks = plan.get("tasks", [])
    candidates = result.get("candidates", [])
    blockers = result.get("blockers", [])
    completed_searches = result.get("completed_searches", [])
    if not isinstance(tasks, list) or not isinstance(candidates, list):
        raise SocialDiscoveryError("plan.tasks and result.candidates must be lists")
    if not isinstance(completed_searches, list):
        raise SocialDiscoveryError("result.completed_searches must be a list")
    blocker_by_task = {
        value.get("task_id"): value
        for value in blockers
        if isinstance(value, Mapping) and value.get("task_id")
    }
    completed_search_task_ids = {
        str(value.get("task_id"))
        for value in completed_searches
        if isinstance(value, Mapping) and value.get("task_id")
    }
    urls_by_task: Dict[str, set] = {}
    candidate_by_url: Dict[str, Mapping[str, Any]] = {}
    for candidate in candidates:
        if not isinstance(candidate, Mapping):
            continue
        url = candidate.get("canonical_url")
        if not isinstance(url, str) or not url:
            continue
        candidate_by_url[url] = candidate
        for match in candidate.get("matches", []):
            if isinstance(match, Mapping) and match.get("task_id"):
                urls_by_task.setdefault(str(match["task_id"]), set()).add(url)

    known_before = set(state["known_urls"])
    query_updates = []
    for task in tasks:
        if not isinstance(task, Mapping) or task.get("task_type") != "search_and_enrich":
            continue
        task_id = task.get("task_id")
        observed = sorted(urls_by_task.get(str(task_id), set()))
        blocker = blocker_by_task.get(task_id)
        executed = bool(
            observed or blocker or str(task_id) in completed_search_task_ids
        )
        if not executed:
            continue
        signature = task.get("query_signature") or query_signature(
            str(task.get("platform")), str(task.get("scope_id")), str(task.get("query"))
        )
        history = dict(state["queries"].get(signature, {}))
        new_urls = [url for url in observed if url not in known_before]
        duplicate_urls = [url for url in observed if url in known_before]
        run_count = int(history.get("run_count", 0) or 0) + 1
        completed = blocker is None
        no_new_streak = int(history.get("no_new_streak", 0) or 0)
        if completed:
            no_new_streak = 0 if new_urls else no_new_streak + 1
        cooldown_hours = min(
            min_repeat_hours * (2 ** max(0, no_new_streak - 1)), 24 * 30
        )
        next_eligible = current if blocker else current + timedelta(hours=cooldown_hours)
        history.update({
            "platform": task.get("platform"),
            "scope_id": task.get("scope_id"),
            "query": task.get("query"),
            "run_count": run_count,
            "last_started_at": plan.get("created_at", _iso(current)),
            "last_completed_at": _iso(current) if completed else history.get("last_completed_at"),
            "last_blocker": blocker.get("state") if blocker else None,
            "last_observed_urls": len(observed),
            "last_new_urls": len(new_urls),
            "last_duplicate_urls": len(duplicate_urls),
            "total_new_urls": int(history.get("total_new_urls", 0) or 0) + len(new_urls),
            "total_duplicate_urls": int(history.get("total_duplicate_urls", 0) or 0)
            + len(duplicate_urls),
            "no_new_streak": no_new_streak,
            "next_eligible_at": _iso(next_eligible),
        })
        state["queries"][signature] = history
        query_updates.append({
            "query_signature": signature,
            "task_id": task_id,
            "new_urls": len(new_urls),
            "duplicate_urls": len(duplicate_urls),
            "blocker": history["last_blocker"],
        })

    for url, candidate in candidate_by_url.items():
        existing = dict(state["known_urls"].get(url, {}))
        matches = candidate.get("matches", [])
        signatures = list(existing.get("query_signatures", []))
        for match in matches:
            if not isinstance(match, Mapping):
                continue
            signature = query_signature(
                str(candidate.get("platform")),
                str(match.get("scope_id", candidate.get("scope_id"))),
                str(match.get("query", candidate.get("query"))),
            )
            if signature not in signatures:
                signatures.append(signature)
        existing.update({
            "platform": candidate.get("platform"),
            "first_seen_at": existing.get("first_seen_at", _iso(current)),
            "last_seen_at": _iso(current),
            "content_sha256": candidate.get("body_sha256"),
            "query_signatures": signatures[:50],
        })
        state["known_urls"][url] = existing

    run_summary = {
        "run_id": result.get("run_id"),
        "plan_run_id": plan.get("run_id"),
        "completed_at": _iso(current),
        "query_updates": query_updates,
        "new_urls": len(set(candidate_by_url) - known_before),
        "duplicate_urls": len(set(candidate_by_url) & known_before),
        "blockers": len(blockers),
    }
    state["runs"].append(run_summary)
    state["runs"] = state["runs"][-MAX_LEDGER_RUNS:]
    state["updated_at"] = _iso(current)
    return state


# Stable product/component names are activated from one source.  Unknown code
# identifiers and acronyms require two independent source URLs before they enter
# the next search plan, which prevents one noisy post from causing query drift.
_KNOWN_TECHNICAL_ENTITIES: Tuple[Tuple[str, str], ...] = (
    ("Isaac Lab", r"\bIsaac\s*Lab\b"),
    ("Isaac Sim", r"\bIsaac\s*Sim\b"),
    ("MuJoCo", r"\bMuJoCo\b"),
    ("RaiSim", r"\bRaiSim\b"),
    ("Gazebo", r"\bGazebo\b"),
    ("Pinocchio", r"\bPinocchio\b"),
    ("Crocoddyl", r"\bCrocoddyl\b"),
    ("TSID", r"\bTSID\b"),
    ("mc_rtc", r"\bmc_rtc\b"),
    ("OCS2", r"\bOCS2\b"),
    ("Drake", r"\bDrake\b"),
    ("qpOASES", r"\bqpOASES\b"),
    ("OSQP", r"\bOSQP\b"),
    ("ProxQP", r"\bProxQP\b"),
    ("HPIPM", r"\bHPIPM\b"),
    ("EtherCAT", r"\bEtherCAT\b"),
    ("CAN-FD", r"\bCAN[ -]?FD\b"),
    ("ros2_control", r"\bros2_control\b"),
    ("PVD", r"\bPVD\b"),
    ("URDF-to-USD", r"\bURDF\s*(?:to|[-→])\s*USD\b"),
    ("接触传感器（Contact Sensor）", r"\bcontact\s*sensor(?:s)?\b|接触传感器"),
    ("碰撞过滤（Collision Filtering）", r"\bcollision\s+filter(?:ing)?\b|碰撞过滤"),
    ("关节索引（Joint Indexing）", r"\bjoint\s+index(?:ing| discrepancy)?\b|关节索引"),
    ("固定关节惯量（Fixed-Joint Inertia）", r"\bfixed[- ]joint\s+inertia\b|固定关节惯量"),
    ("训练非确定性（Training Nondeterminism）", r"\bnon[- ]?determin(?:ism|istic)\b|训练不确定性|结果不可复现"),
    ("自定义地形网格（Custom Terrain Mesh）", r"\bcustom\s+(?:usd\s+)?terrain\s+mesh\b|自定义地形网格"),
)

_GENERIC_TOKEN = re.compile(
    r"`([A-Za-z][A-Za-z0-9_.:+-]{2,40})`|\b([A-Z][A-Z0-9_-]{2,12})\b|"
    r"\b([A-Z][a-z]+(?:[A-Z][A-Za-z0-9]+)+)\b"
)
_TOKEN_STOP = {
    "WBC", "RL", "GPU", "CPU", "API", "URL", "HTTP", "HTTPS", "JSON",
    "README", "DOCKER", "USD", "URDF", "ROS", "MPC", "QP", "IK", "PD",
    "PID", "COM", "DOF", "IMU", "LQR", "CUDA", "PYTHON", "LINUX",
    "NVIDIA", "RTX", "GEFORCE", "LTS", "LUID", "UUID", "LDA", "SE3",
    "ARGUMENTPARSER", "APPLAUNCHER", "ATTRIBUTEERROR", "VALUEERROR",
    "RUNTIMEERROR", "TYPEERROR", "KEYERROR", "INDEXERROR", "ASSERTIONERROR",
    "MODULENOTFOUNDERROR", "NONETYPE", "XML", "GUI", "RGB", "LOCAL", "WORLD",
    "INITIALSTATECFG", "ASSETBASECFG", "ARTICULATIONCFG", "SIMULATIONCFG",
    "SCENEENTITYCFG", "OFFSETCFG", "GROUNDPLANECFG", "DOMELIGHTCFG",
    "RIGIDBODYMATERIALCFG", "RIGIDBODYPROPERTIESCFG", "RIGIDOBJECTCFG",
    "COLLISIONPROPERTIESCFG", "USDFILECFG", "INTERACTIVESCENE",
}


def _frontier_query(term: str, platform: str) -> str:
    if platform in {"xiaohongshu", "zhihu"}:
        return f"人形机器人 WBC {term} 调试"
    if platform == "github_issue":
        return f'"{term}" humanoid'
    return f'"{term}" humanoid WBC debugging'


def _contexts(candidate: Mapping[str, Any]) -> Iterable[Tuple[str, str, str]]:
    title = candidate.get("title")
    if isinstance(title, str) and title.strip():
        yield "标题", title, str(candidate.get("canonical_url", ""))
    body = candidate.get("body_text", candidate.get("summary", ""))
    if isinstance(body, str) and body.strip():
        yield "正文", body, str(candidate.get("canonical_url", ""))
    for index, comment in enumerate(candidate.get("selected_comments", [])):
        if not isinstance(comment, Mapping) or not isinstance(comment.get("text"), str):
            continue
        author = comment.get("author_display") or f"评论 {index + 1}"
        locator = f"评论 @{author}"
        yield locator, comment["text"], str(
            comment.get("source_url") or candidate.get("canonical_url", "")
        )


def _term_hits(text: str) -> List[Tuple[str, bool, int, int]]:
    hits: List[Tuple[str, bool, int, int]] = []
    occupied: List[Tuple[int, int]] = []
    for term, pattern in _KNOWN_TECHNICAL_ENTITIES:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            hits.append((term, True, match.start(), match.end()))
            occupied.append((match.start(), match.end()))
    for match in _GENERIC_TOKEN.finditer(text):
        token = next(value for value in match.groups() if value).strip("._:+-")
        if token.upper() in _TOKEN_STOP or len(token) > 40:
            continue
        if any(start <= match.start() < end for start, end in occupied):
            continue
        hits.append((token, False, match.start(), match.end()))
    return hits


def evolve_query_frontier(
    candidates: Sequence[Mapping[str, Any]],
    *,
    existing_queries: Sequence[Mapping[str, Any]],
    previous_frontier: Optional[Mapping[str, Any]] = None,
    platforms: Sequence[str] = ("xiaohongshu", "zhihu", "x", "github_issue"),
    evolved_at: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Merge every evidence-linked technical term into the visible frontier.

    The frontier is deliberately unbounded: execution budgets belong to the
    per-run selector, not to the durable topic catalogue.
    """

    current = _now(evolved_at)
    if previous_frontier:
        if previous_frontier.get("schema_version") not in {1, FRONTIER_SCHEMA_VERSION}:
            raise SocialDiscoveryError("query frontier schema_version is unsupported")
        topics_value = previous_frontier.get("topics", [])
        if not isinstance(topics_value, list):
            raise SocialDiscoveryError("query frontier topics must be a list")
        topics = {
            str(value.get("topic_id")): dict(value)
            for value in topics_value
            if isinstance(value, Mapping) and value.get("topic_id")
        }
        created_at = previous_frontier.get("created_at", _iso(current))
    else:
        topics = {}
        created_at = _iso(current)

    existing_text = "\n".join(
        normalize_query_text(value.get("query"))
        for value in existing_queries
        if isinstance(value, Mapping) and isinstance(value.get("query"), str)
    )
    for candidate in candidates:
        if not isinstance(candidate, Mapping):
            continue
        canonical_url = candidate.get("canonical_url")
        if not isinstance(canonical_url, str) or not canonical_url:
            continue
        scope_id = str(candidate.get("scope_id", "open_ended_wbc_field_notes"))
        platform = str(candidate.get("platform", "unknown"))
        for locator, text, evidence_url in _contexts(candidate):
            for term, known, start, end in _term_hits(text):
                normalized_term = term.casefold()
                topic_id = hashlib.sha256(normalized_term.encode("utf-8")).hexdigest()[:16]
                topic = dict(topics.get(topic_id, {}))
                evidence = [
                    dict(value) for value in topic.get("evidence", [])
                    if isinstance(value, Mapping)
                ]
                evidence_key = (canonical_url, locator, term)
                existing_keys = {
                    (value.get("root_url"), value.get("locator"), value.get("term"))
                    for value in evidence
                }
                if evidence_key not in existing_keys:
                    left = max(0, start - 100)
                    right = min(len(text), end + 140)
                    evidence.append({
                        "root_url": canonical_url,
                        "source_url": evidence_url or canonical_url,
                        "platform": platform,
                        "locator": locator,
                        "term": term,
                        "context": re.sub(r"\s+", " ", text[left:right]).strip(),
                        "observed_at": _iso(current),
                    })
                source_count = len({value.get("root_url") for value in evidence})
                strong_evidence_count = len({
                    value.get("root_url") for value in evidence
                    if value.get("locator") == "标题"
                    or str(value.get("locator", "")).startswith("评论")
                })
                covered = normalized_term in existing_text
                qualifies = known or (source_count >= 2 and strong_evidence_count >= 1)
                status = (
                    "covered" if covered else
                    "ready" if qualifies else
                    "needs_more_evidence"
                )
                generated_queries = {
                    value: _frontier_query(term, value) for value in platforms
                }
                topic.update({
                    "topic_id": topic_id,
                    "term": term,
                    "scope_id": topic.get("scope_id", scope_id),
                    "known_entity": bool(topic.get("known_entity", False) or known),
                    "status": status,
                    "independent_source_count": source_count,
                    "strong_evidence_count": strong_evidence_count,
                    "evidence": evidence,
                    "generated_queries": generated_queries,
                    "first_seen_at": topic.get("first_seen_at", _iso(current)),
                    "last_seen_at": _iso(current),
                })
                topics[topic_id] = topic

    # Recompute legacy v1 active/proposed statuses even when no fresh evidence
    # mentioned the topic during this particular evolution pass.
    for topic in topics.values():
        source_count = len({
            value.get("root_url")
            for value in topic.get("evidence", [])
            if isinstance(value, Mapping) and value.get("root_url")
        })
        strong_evidence_count = len({
            value.get("root_url")
            for value in topic.get("evidence", [])
            if isinstance(value, Mapping)
            and (
                value.get("locator") == "标题"
                or str(value.get("locator", "")).startswith("评论")
            )
        })
        covered = normalize_query_text(str(topic.get("term", "unknown"))) in existing_text
        qualifies = bool(topic.get("known_entity")) or (
            source_count >= 2 and strong_evidence_count >= 1
        )
        topic["status"] = (
            "covered" if covered else
            "ready" if qualifies else
            "needs_more_evidence"
        )
        topic["independent_source_count"] = source_count
        topic["strong_evidence_count"] = strong_evidence_count
        topic.pop("deferred_reason", None)

    ranked = sorted(
        topics.values(),
        key=lambda value: (
            0 if value.get("known_entity") else 1,
            -int(value.get("strong_evidence_count", 0)),
            -int(value.get("independent_source_count", 0)),
            str(value.get("term", "")).casefold(),
        ),
    )
    ordered = sorted(
        ranked,
        key=lambda value: (
            {
                "ready": 0,
                "needs_more_evidence": 1,
                "covered": 2,
            }.get(value.get("status"), 3),
            0 if value.get("known_entity") else 1,
            -int(value.get("strong_evidence_count", 0)),
            -int(value.get("independent_source_count", 0)),
            str(value.get("term", "")).casefold(),
        ),
    )
    counts: Dict[str, int] = {}
    for topic in ordered:
        status = str(topic.get("status", "unknown"))
        counts[status] = counts.get(status, 0) + 1
    return {
        "schema_version": FRONTIER_SCHEMA_VERSION,
        "created_at": created_at,
        "updated_at": _iso(current),
        "activation_rule": (
            "known technical entity: one source; unknown identifier: two independent URLs"
        ),
        "topics": ordered,
        "counts": counts,
    }


def frontier_queries(
    frontier: Optional[Mapping[str, Any]],
    platforms: Sequence[str],
    *,
    topic_ids: Optional[Sequence[str]] = None,
) -> List[Dict[str, Any]]:
    if not frontier:
        return []
    if frontier.get("schema_version") not in {1, FRONTIER_SCHEMA_VERSION}:
        raise SocialDiscoveryError("query frontier schema_version is unsupported")
    requested = {value.strip() for value in topic_ids or [] if value.strip()}
    queries: List[Dict[str, Any]] = []
    for topic in frontier.get("topics", []):
        if not isinstance(topic, Mapping):
            continue
        topic_id = str(topic.get("topic_id", ""))
        status = str(topic.get("status", ""))
        if requested:
            if topic_id not in requested:
                continue
        elif status not in {"ready", "active"}:
            continue
        generated = topic.get("generated_queries", {})
        if not isinstance(generated, Mapping):
            continue
        for platform in platforms:
            query = generated.get(platform)
            if isinstance(query, str) and query.strip():
                queries.append({
                    "scope_id": topic.get("scope_id", "open_ended_wbc_field_notes"),
                    "domain_hints": [],
                    "query": query,
                    "platforms": [platform],
                    "origin": "frontier",
                    "frontier_topic_id": topic_id,
                    "frontier_term": topic.get("term"),
                })
    return queries


def frontier_topic_ids(frontier: Optional[Mapping[str, Any]]) -> set[str]:
    """Return every visible stable topic identifier from either frontier version."""

    if not frontier:
        return set()
    if frontier.get("schema_version") not in {1, FRONTIER_SCHEMA_VERSION}:
        raise SocialDiscoveryError("query frontier schema_version is unsupported")
    return {
        str(value.get("topic_id"))
        for value in frontier.get("topics", [])
        if isinstance(value, Mapping) and value.get("topic_id")
    }


def render_query_frontier_markdown(
    frontier: Mapping[str, Any],
    *,
    discovery_state: Optional[Mapping[str, Any]] = None,
) -> str:
    """Render the complete topic catalogue and its execution eligibility."""

    if frontier.get("schema_version") not in {1, FRONTIER_SCHEMA_VERSION}:
        raise SocialDiscoveryError("query frontier schema_version is unsupported")
    state = _normalized_state(discovery_state) if discovery_state else None
    query_state = state["queries"] if state else {}
    status_labels = {
        "ready": "ready（达到自动搜索门槛）",
        "needs_more_evidence": "needs_more_evidence（证据尚少）",
        "covered": "covered（固定查询已覆盖）",
        "active": "ready（由旧版 active 迁移）",
        "proposed": "needs_more_evidence（由旧版 proposed 迁移）",
    }
    topics = [
        value for value in frontier.get("topics", []) if isinstance(value, Mapping)
    ]
    counts: Dict[str, int] = {}
    for topic in topics:
        raw_status = str(topic.get("status", "needs_more_evidence"))
        status = {
            "active": "ready",
            "proposed": "needs_more_evidence",
        }.get(raw_status, raw_status)
        counts[status] = counts.get(status, 0) + 1

    lines = [
        "# WBC 社交查询全量前沿",
        "",
        "> 本页展示全部去重子话题；状态不控制可见性，只影响默认自动调度。",
        "> 每轮仍受平台查询和详情页预算约束，未执行主题会在后续按需运行中继续轮转。",
        "",
        f"- 主题总数：{len(topics)}",
        f"- ready：{counts.get('ready', 0)}",
        f"- needs_more_evidence：{counts.get('needs_more_evidence', 0)}",
        f"- covered：{counts.get('covered', 0)}",
        "- 默认次序：从未搜索 → 上轮新增证据 → 到期刷新 → scope 轮询",
        "- 定向执行：`social-browser-plan --topic <topic_id>` 或 "
        "`github-issue-plan --topic <topic_id>`",
        "",
    ]
    for index, topic in enumerate(topics, start=1):
        topic_id = str(topic.get("topic_id", "unknown"))
        term = str(topic.get("term", "未命名主题"))
        raw_status = str(topic.get("status", "needs_more_evidence"))
        lines.extend([
            f"## {index}. {term}",
            "",
            f"- `topic_id`：`{topic_id}`",
            f"- 状态：`{status_labels.get(raw_status, raw_status)}`",
            f"- scope：`{topic.get('scope_id', 'open_ended_wbc_field_notes')}`",
            f"- 独立根来源：{int(topic.get('independent_source_count', 0) or 0)}；"
            f"强触发来源：{int(topic.get('strong_evidence_count', 0) or 0)}",
            f"- 首次发现：{topic.get('first_seen_at', '未知')}；"
            f"最近发现：{topic.get('last_seen_at', '未知')}",
            "",
        ])
        generated = topic.get("generated_queries", {})
        if isinstance(generated, Mapping) and generated:
            schedules = []
            for platform, query in sorted(generated.items()):
                if not isinstance(query, str):
                    continue
                signature = query_signature(
                    str(platform),
                    str(topic.get("scope_id", "open_ended_wbc_field_notes")),
                    query,
                )
                history = query_state.get(signature, {})
                schedules.append(
                    f"`{platform}`：上次 {history.get('last_completed_at', '从未搜索')}；"
                    f"下次 {history.get('next_eligible_at', '现在')}；"
                    f"上轮新增 {int(history.get('last_new_urls', 0) or 0)}"
                )
            lines.append("- 平台与执行时间：" + "；".join(schedules))
        else:
            lines.append("- 平台与执行时间：暂无生成查询。")
        lines.append("- 触发来源：")
        evidence = [
            value for value in topic.get("evidence", []) if isinstance(value, Mapping)
        ]
        if not evidence:
            lines.append("- 暂无可定位来源（旧版迁移项，等待补采）。")
        else:
            for item in evidence:
                root_url = str(item.get("root_url", ""))
                source_url = str(item.get("source_url") or root_url)
                locator = str(item.get("locator", "未定位"))
                platform = str(item.get("platform", "unknown"))
                link = f"[{locator}]({source_url})" if source_url else locator
                lines.append(
                    f"  - `{platform}` · {link} · 根帖：{root_url or '未知'}"
                )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"
