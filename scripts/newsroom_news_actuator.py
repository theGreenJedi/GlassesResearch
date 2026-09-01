#!/usr/bin/env python3
"""Compile approved news-only newsroom packages into a complete canonical draft diff.

The actuator is deliberately narrow. It will produce canonical edits only when every
approved route in a package is `news.publish`. Mixed packages are blocked rather than
partially published, because GlassesResearch policy requires every materially affected
canonical layer to be updated together.

The output is still a draft repository change. Publication occurs only when the normal
pull request is reviewed and merged.
"""
from __future__ import annotations

import argparse
import json
import re
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DIR = ROOT / "research" / "newsroom-packages"
NEWS_PATH = ROOT / "docs" / "RESEARCH_NEWS.md"
ARTICLE_DIR = ROOT / "docs" / "news" / "articles"
REVIEW_DIR = ROOT / "research" / "news-reviews"
GRE_PATH = ROOT / "data" / "verified-changes.json"
THE_LIST = ROOT / "models" / "THE_LIST.md"

SAFE_ROUTES = {"news.publish"}
VALID_VERIFICATIONS = {"verified", "corroborated"}
VALID_CHANGE_TYPES = {
    "catalog_admission",
    "catalog_removal",
    "availability_change",
    "hardware_change",
    "software_release",
    "policy_change",
    "research_release",
    "relationship_change",
}
TOPIC_BY_BEAT = {
    "products": "release_availability",
    "industry": "release_availability",
    "software_ai": "firmware_software",
    "developer_open": "hacks_development",
    "privacy_policy": "privacy_policy",
    "research": "research_science",
    "displays_optics": "hardware_teardown",
    "components": "hardware_teardown",
    "applications": "apps_services",
    "rumor": "research_science",
}


class ActuatorError(RuntimeError):
    pass


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:90] or "newsroom-update"


def _text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ActuatorError(f"{field} must be a non-empty string")
    return value.strip()


def _package_envelope(path: Path) -> tuple[str, dict[str, Any]]:
    try:
        envelope = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ActuatorError(f"{path}: invalid package JSON: {exc}") from exc
    if not isinstance(envelope, dict) or envelope.get("schema_version") != 1:
        raise ActuatorError(f"{path}: unsupported package envelope")
    package_id = _text(envelope.get("package_id"), "package_id")
    if envelope.get("state") != "second_gate_approved":
        raise ActuatorError(f"{package_id}: package is not second-gate approved")
    package = envelope.get("package")
    if not isinstance(package, dict):
        raise ActuatorError(f"{package_id}: package body missing")
    return package_id, package


def _route_destinations(package: dict[str, Any]) -> set[str]:
    routes = package.get("routes")
    if not isinstance(routes, list) or not routes:
        raise ActuatorError("package has no approved routes")
    destinations: set[str] = set()
    for route in routes:
        if not isinstance(route, dict):
            raise ActuatorError("package route must be an object")
        destinations.add(_text(route.get("destination"), "route.destination"))
    return destinations


def _published_day(package: dict[str, Any]) -> date:
    days: list[date] = []
    sources = package.get("sources")
    if isinstance(sources, list):
        for source in sources:
            if not isinstance(source, dict):
                continue
            raw = source.get("published_at")
            if not isinstance(raw, str) or not raw.strip():
                continue
            try:
                days.append(datetime.fromisoformat(raw.strip().replace("Z", "+00:00")).date())
            except ValueError:
                try:
                    days.append(date.fromisoformat(raw.strip()[:10]))
                except ValueError:
                    continue
    return max(days) if days else datetime.now(timezone.utc).date()


def _eligible_claims(package: dict[str, Any]) -> list[dict[str, Any]]:
    claims = package.get("claims")
    if not isinstance(claims, list):
        raise ActuatorError("package claims must be a list")
    sources = package.get("sources")
    has_primary = isinstance(sources, list) and any(
        isinstance(source, dict) and source.get("source_class") == "primary" for source in sources
    )
    eligible: list[dict[str, Any]] = []
    for claim in claims:
        if not isinstance(claim, dict):
            continue
        verification = claim.get("verification")
        confidence = claim.get("confidence")
        if verification in VALID_VERIFICATIONS and confidence in {"medium", "high"}:
            eligible.append(claim)
        elif verification == "single_source" and confidence == "high" and has_primary:
            eligible.append(claim)
    return eligible


def _source_urls(package: dict[str, Any]) -> list[str]:
    result: list[str] = []
    sources = package.get("sources")
    if not isinstance(sources, list):
        return result
    for source in sources:
        if not isinstance(source, dict):
            continue
        value = source.get("url")
        if isinstance(value, str) and value.startswith(("https://", "http://")) and value not in result:
            result.append(value)
    return result


def _affected_models(root: Path, package: dict[str, Any]) -> list[str]:
    haystack = json.dumps(package, ensure_ascii=False)
    candidates = sorted(set(re.findall(r"\bGLS-\d{4}\b", haystack)))
    try:
        ledger = (root / "models" / "THE_LIST.md").read_text(encoding="utf-8")
    except OSError:
        return []
    return [model_id for model_id in candidates if model_id in ledger]


def _change_type(package: dict[str, Any], claims: list[dict[str, Any]]) -> str:
    beat = str(package.get("beat") or "")
    types = {str(claim.get("claim_type") or "") for claim in claims}
    if "policy" in types or beat == "privacy_policy":
        return "policy_change"
    if "research_result" in types or beat == "research":
        return "research_release"
    if "availability" in types or "price" in types or "release" in types or beat in {"products", "industry"}:
        return "availability_change"
    if beat in {"software_ai", "developer_open", "applications"}:
        return "software_release"
    if beat in {"displays_optics", "components"} or "spec" in types or "feature" in types:
        return "hardware_change"
    return "research_release"


def _next_gre_id(ledger_text: str) -> str:
    numbers = [int(value) for value in re.findall(r'"id"\s*:\s*"GRE-(\d{6})"', ledger_text)]
    return f"GRE-{(max(numbers) if numbers else 0) + 1:06d}"


def _indent_json(value: Any, spaces: int = 4) -> str:
    raw = json.dumps(value, ensure_ascii=False, indent=2)
    prefix = " " * spaces
    return "\n".join(prefix + line for line in raw.splitlines())


def _append_gre_event(ledger_text: str, event: dict[str, Any]) -> str:
    marker = "\n  ]\n}"
    index = ledger_text.rfind(marker)
    if index < 0:
        raise ActuatorError("verified-changes ledger closing structure not recognized")
    before = ledger_text[:index].rstrip()
    separator = "," if before.endswith("}") else ""
    return before + separator + "\n" + _indent_json(event) + marker + "\n"


def _display_day(day: date) -> str:
    return day.strftime("%b. %-d")


def _heading_day(day: date) -> str:
    return day.strftime("%B %-d, %Y")


def _topic(package: dict[str, Any]) -> str:
    return TOPIC_BY_BEAT.get(str(package.get("beat") or ""), "research_science")


def _article(package_id: str, package: dict[str, Any], day: date, claims: list[dict[str, Any]], sources: list[str]) -> str:
    title = _text(package.get("title"), "package.title")
    summary = _text(package.get("summary"), "package.summary")
    route_reasons = [
        str(route.get("reason") or "").strip()
        for route in package.get("routes", [])
        if isinstance(route, dict) and str(route.get("reason") or "").strip()
    ]
    claim_lines = "\n".join(f"- {str(claim.get('statement') or '').strip()}" for claim in claims)
    source_lines = "\n".join(f"- {url}" for url in sources)
    reason = route_reasons[0] if route_reasons else "The second-gate-approved News Desk package marked this as a material GlassesResearch development."
    return f"""# {title}

<!-- newsroom-package: {package_id} -->

**Published:** {_heading_day(day)}  
**Status:** Verified newsroom package; repository review required for publication

{summary}

## What we verified

{claim_lines}

## Why it matters

{reason}

## Evidence boundary

This article is compiled only from claims that crossed the News Desk's verification threshold and from the evidence sources preserved in the second-gate-approved package. Claims that remained conflicting, unverified, or below the actuator threshold are not promoted here. Repository review remains the final publication gate.

## Sources

{source_lines}
"""


def _review(package_id: str, package: dict[str, Any], article_path: str, sources: list[str], models: list[str]) -> str:
    title = _text(package.get("title"), "package.title")
    source_text = " ".join(sources)
    affected_models = ", ".join(f"`{model_id}`" for model_id in models) if models else "none — no existing canonical GLS identifier was resolved from the approved package"
    destinations = ", ".join(
        f"`{path}`"
        for path in ["docs/RESEARCH_NEWS.md", article_path, "data/verified-changes.json"]
    )
    return f"""# Newsroom promotion review — {title}

<!-- news_promotion_schema: 1 -->
<!-- newsroom-package: {package_id} -->

**Reviewer:** Live Editorial Desk second human gate; final repository review pending  
**Candidate files surveyed:** `research/newsroom-packages/{package_id}.json`  
**Total raw candidates considered:** 1  
**Underlying developments after deduplication:** 1

> **Collection is not publication.** This record represents an explicitly approved promotion package compiled into a draft repository diff. Merge remains the publication act.

## Summary

- Publish: 1
- Watch: 0
- Archive: 0
- Superseded: 0
- Reject: 0

### Development 1 — {title}

- **Candidate IDs:** `{package_id}`
- **Source URLs:** {source_text}
- **Scope lane:** `core_glasses`
- **Event date:** derived from the newest dated evidence source in the approved package
- **Discovery date:** preserved in the live newsroom/D1 audit trail
- **What happened:** {_text(package.get('summary'), 'package.summary')}
- **Why it may matter:** approved by the semantic News Desk and second human publication gate as material enough for `news.publish`
- **Evidence quality:** only verified/corroborated claims, or high-confidence single-primary-source claims, are promoted by this actuator
- **Affected models / lineages / technologies:** {affected_models}
- **One-year institution test:** yes
- **Public-site eligible now:** yes, subject to final repository review
- **Disposition:** `publish`
- **Reason for disposition:** second-gate-approved news-only promotion package
- **Affected models:** {affected_models}
- **Affected lineages / platforms / resources:** none — this news-only actuator refuses packages that request lineage, catalog, report-card, Finder, release-tracker, or research-dossier changes
- **Canonical destinations:** {destinations}
- **Canonical follow-up if published:**
  - [ ] Model page
  - [ ] The List
  - [ ] Lineage
  - [ ] Comparison data / report card
  - [ ] Timeline
  - [ ] Community / development resources
  - [ ] FAQ / glossary
  - [ ] Artifact / manual / SDK / firmware archive
  - [x] Public digest
  - [x] Verified-change ledger / alert surface

## Survey closeout

- [x] Duplicate/syndicated handling occurred in the News Desk before this package.
- [x] Public promotion passed both the first editorial gate and the second publication gate.
- [x] Raw package and evidence-source references remain preserved.
- [x] Publish decision identifies concrete canonical destinations.
- [ ] Final repository diff reviewed and merged.
"""


def _news_section(package_id: str, package: dict[str, Any], day: date, claims: list[dict[str, Any]], sources: list[str], article_rel: str) -> str:
    title = _text(package.get("title"), "package.title")
    summary = _text(package.get("summary"), "package.summary")
    claims_text = "\n".join(f"- {str(claim.get('statement') or '').strip()}" for claim in claims)
    sources_text = " · ".join(f"[{url}]({url})" for url in sources)
    article_link = article_rel.removeprefix("docs/")
    return f"""### {_heading_day(day)} — {title}

<!-- newsroom-package: {package_id} -->

{summary}

**Verified claims:**

{claims_text}

Continue: [verified article]({article_link})

Sources: {sources_text}

"""


def _insert_news(news_text: str, package_id: str, package: dict[str, Any], day: date, section: str, article_rel: str) -> str:
    if f"newsroom-package: {package_id}" in news_text:
        return news_text
    table_marker = "|---|---|---|"
    table_index = news_text.find(table_marker)
    if table_index < 0:
        raise ActuatorError("Research & News latest-verified table marker not found")
    line_end = news_text.find("\n", table_index)
    if line_end < 0:
        raise ActuatorError("Research & News table is malformed")
    title = _text(package.get("title"), "package.title")
    summary = _text(package.get("summary"), "package.summary")
    article_link = article_rel.removeprefix("docs/")
    row = f"| {_display_day(day)} | **{title}** — {summary} | [verified article]({article_link}) |\n"
    news_text = news_text[: line_end + 1] + row + news_text[line_end + 1 :]

    latest_index = news_text.find("## Latest verified")
    first_heading = news_text.find("\n### ", latest_index)
    if first_heading < 0:
        raise ActuatorError("Research & News first Latest verified story heading not found")
    insertion = first_heading + 1
    return news_text[:insertion] + section + news_text[insertion:]


def _already_applied(root: Path, package_id: str) -> bool:
    review_dir = root / "research" / "news-reviews"
    if not review_dir.exists():
        return False
    marker = f"newsroom-package: {package_id}"
    return any(marker in path.read_text(encoding="utf-8", errors="ignore") for path in review_dir.glob("*.md"))


def apply_package(root: Path, path: Path) -> tuple[str, str]:
    package_id, package = _package_envelope(path)
    if _already_applied(root, package_id):
        return package_id, "already_applied"

    destinations = _route_destinations(package)
    if not destinations.issubset(SAFE_ROUTES):
        return package_id, "blocked:" + ",".join(sorted(destinations - SAFE_ROUTES))
    if destinations != {"news.publish"}:
        return package_id, "blocked:no_news_publish_route"
    if package.get("confidence") not in {"medium", "high"}:
        return package_id, "blocked:story_confidence"

    claims = _eligible_claims(package)
    if not claims:
        return package_id, "blocked:no_publishable_claims"
    sources = _source_urls(package)
    if not sources:
        return package_id, "blocked:no_sources"

    day = _published_day(package)
    slug = _slug(str(package.get("story_key") or package.get("title") or package_id))
    article_rel = f"docs/news/articles/{day.isoformat()}-{slug}.md"
    review_rel = f"research/news-reviews/{day.isoformat()}-newsroom-{slug}.md"
    article_path = root / article_rel
    review_path = root / review_rel
    if article_path.exists() and f"newsroom-package: {package_id}" not in article_path.read_text(encoding="utf-8", errors="ignore"):
        return package_id, "blocked:article_path_exists"
    if review_path.exists() and f"newsroom-package: {package_id}" not in review_path.read_text(encoding="utf-8", errors="ignore"):
        return package_id, "blocked:review_path_exists"

    ledger_path = root / "data" / "verified-changes.json"
    news_path = root / "docs" / "RESEARCH_NEWS.md"
    ledger_text = ledger_path.read_text(encoding="utf-8")
    news_text = news_path.read_text(encoding="utf-8")
    models = _affected_models(root, package)
    change_type = _change_type(package, claims)
    if change_type not in VALID_CHANGE_TYPES:
        raise ActuatorError(f"unsupported derived change type: {change_type}")

    gre_id = _next_gre_id(ledger_text)
    title = _text(package.get("title"), "package.title")
    summary = _text(package.get("summary"), "package.summary")
    heading = f"{_heading_day(day)} — {title}"
    publication_id = f"gr-{day.isoformat()}-{slug}"
    event = {
        "id": gre_id,
        "state": "verified",
        "change_type": change_type,
        "verified_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "previous_state": "This second-gate-approved development was not yet represented as a verified canonical GlassesResearch publication.",
        "new_state": summary,
        "affected": {"model_ids": models, "relationship_ids": []},
        "evidence_urls": sources,
        "publication": {
            "id": publication_id,
            "dispatch": True,
            "source_heading": heading,
            "title": title,
            "canonical_url": f"https://glassesresearch.org/docs/news/articles/{day.isoformat()}-{slug}/",
            "summary": summary,
            "published_at": day.isoformat(),
        },
        "alert_match": {
            "models": models,
            "brands_lineages": [],
            "topics": [_topic(package)],
        },
    }

    article_path.parent.mkdir(parents=True, exist_ok=True)
    review_path.parent.mkdir(parents=True, exist_ok=True)
    article_path.write_text(_article(package_id, package, day, claims, sources), encoding="utf-8")
    review_path.write_text(_review(package_id, package, article_rel, sources, models), encoding="utf-8")
    section = _news_section(package_id, package, day, claims, sources, article_rel)
    news_path.write_text(_insert_news(news_text, package_id, package, day, section, article_rel), encoding="utf-8")
    ledger_path.write_text(_append_gre_event(ledger_text, event), encoding="utf-8")
    return package_id, "applied_draft"


def apply_all(root: Path, package_dir: Path) -> list[tuple[str, str]]:
    results: list[tuple[str, str]] = []
    for path in sorted(package_dir.glob("GRNP-*.json")):
        results.append(apply_package(root, path))
    return results


def _fixture_root(base: Path) -> tuple[Path, Path]:
    (base / "docs" / "news" / "articles").mkdir(parents=True)
    (base / "research" / "news-reviews").mkdir(parents=True)
    (base / "research" / "newsroom-packages").mkdir(parents=True)
    (base / "data").mkdir(parents=True)
    (base / "models").mkdir(parents=True)
    (base / "docs" / "RESEARCH_NEWS.md").write_text(
        "# Research & News\n\n## Latest verified\n\n| Date | What changed | Go deeper |\n|---|---|---|\n| Aug. 28 | Old item | old |\n\n### August 28, 2026 — Old item\n\nOld.\n",
        encoding="utf-8",
    )
    (base / "data" / "verified-changes.json").write_text(
        '{\n  "schema_version": 1,\n  "events": [\n    {"id":"GRE-000001"}\n  ]\n}\n',
        encoding="utf-8",
    )
    (base / "models" / "THE_LIST.md").write_text("GLS-0001 Example Glasses\n", encoding="utf-8")
    package = {
        "schema_version": 1,
        "package_id": "GRNP-TEST00000001",
        "state": "second_gate_approved",
        "source_queue": "https://example.com/queue",
        "ingested_at": "2026-09-01T00:00:00Z",
        "package": {
            "story_id": "story-1",
            "story_key": "example-glasses-launch",
            "title": "Example Glasses launch",
            "summary": "Example Glasses launched with a documented acquisition path.",
            "confidence": "high",
            "beat": "products",
            "claims": [
                {
                    "claim_id": "claim-1",
                    "normalized_key": "release",
                    "statement": "GLS-0001 Example Glasses launched.",
                    "claim_type": "release",
                    "verification": "verified",
                    "confidence": "high",
                }
            ],
            "sources": [
                {
                    "source_id": "source-1",
                    "url": "https://example.com/glasses",
                    "publisher": "Example",
                    "source_class": "primary",
                    "published_at": "2026-09-01",
                }
            ],
            "routes": [
                {
                    "route_id": "route-1",
                    "destination": "news.publish",
                    "reason": "Material launch",
                    "payload": {},
                    "created_at": "2026-09-01T00:00:00Z",
                }
            ],
        },
    }
    package_path = base / "research" / "newsroom-packages" / "GRNP-TEST00000001.json"
    package_path.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
    return base, package_path


def self_test() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root, package_path = _fixture_root(Path(directory))
        package_id, status = apply_package(root, package_path)
        assert package_id == "GRNP-TEST00000001" and status == "applied_draft"
        news = (root / "docs" / "RESEARCH_NEWS.md").read_text(encoding="utf-8")
        ledger = (root / "data" / "verified-changes.json").read_text(encoding="utf-8")
        assert "newsroom-package: GRNP-TEST00000001" in news
        assert "GRE-000002" in ledger
        assert "GLS-0001" in ledger
        assert json.loads(ledger)["events"][-1]["publication"]["dispatch"] is True
        assert apply_package(root, package_path)[1] == "already_applied"

    with tempfile.TemporaryDirectory() as directory:
        root, package_path = _fixture_root(Path(directory))
        envelope = json.loads(package_path.read_text(encoding="utf-8"))
        envelope["package"]["routes"].append(
            {
                "route_id": "route-2",
                "destination": "catalog.update",
                "reason": "Catalog must change too",
                "payload": {},
                "created_at": "2026-09-01T00:00:00Z",
            }
        )
        package_path.write_text(json.dumps(envelope, indent=2) + "\n", encoding="utf-8")
        before = (root / "docs" / "RESEARCH_NEWS.md").read_text(encoding="utf-8")
        assert apply_package(root, package_path)[1] == "blocked:catalog.update"
        assert (root / "docs" / "RESEARCH_NEWS.md").read_text(encoding="utf-8") == before
    print("Newsroom news actuator self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", type=Path)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0

    try:
        if args.package:
            results = [apply_package(args.root, args.package)]
        else:
            package_dir = args.root / "research" / "newsroom-packages"
            results = apply_all(args.root, package_dir)
    except (ActuatorError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1

    if not results:
        print("No newsroom packages to compile.")
        return 0
    for package_id, status in results:
        print(f"{package_id}: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
