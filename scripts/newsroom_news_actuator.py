#!/usr/bin/env python3
"""Compile second-gate-approved news-only packages into canonical draft diffs.

This actuator is intentionally conservative. It acts only when the approved canonical
scope is exactly ``news.publish``. A package that also requires catalog, lineage,
report-card, Finder, release-tracker, or dossier work is preserved but blocked so the
repository never publishes only the easy half of a material change.

Generated edits still live on a draft pull request. Merge remains the final publication
act and retains the repository's normal validators as the authority.
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
SAFE_ROUTES = {"news.publish"}
GOOD_VERIFICATIONS = {"verified", "corroborated"}
VALID_CHANGE_TYPES = {
    "availability_change",
    "hardware_change",
    "software_release",
    "policy_change",
    "research_release",
}
VALID_TOPICS = {
    "hacks_development",
    "firmware_software",
    "hardware_teardown",
    "privacy_policy",
    "release_availability",
    "research_science",
    "standards_regulation",
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
    "applications": "firmware_software",
    "rumor": "research_science",
}


class ActuatorError(RuntimeError):
    pass


def text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ActuatorError(f"{field} must be a non-empty string")
    return value.strip()


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:90] or "newsroom-update"


def table_text(value: str) -> str:
    return " ".join(value.split()).replace("|", "\\|")


def display_day(day: date) -> str:
    month = day.strftime("%b")
    return f"{month}. {day.day}"


def heading_day(day: date) -> str:
    return f"{day.strftime('%B')} {day.day}, {day.year}"


def load_envelope(path: Path) -> tuple[str, dict[str, Any]]:
    try:
        envelope = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ActuatorError(f"{path}: invalid package JSON: {exc}") from exc
    if not isinstance(envelope, dict) or envelope.get("schema_version") != 1:
        raise ActuatorError(f"{path}: unsupported package envelope")
    package_id = text(envelope.get("package_id"), "package_id")
    if envelope.get("state") != "second_gate_approved":
        raise ActuatorError(f"{package_id}: package is not second-gate approved")
    package = envelope.get("package")
    if not isinstance(package, dict):
        raise ActuatorError(f"{package_id}: package body missing")
    return package_id, package


def destinations(package: dict[str, Any]) -> set[str]:
    raw = package.get("routes")
    if not isinstance(raw, list) or not raw:
        raise ActuatorError("package has no approved routes")
    result: set[str] = set()
    for route in raw:
        if not isinstance(route, dict):
            raise ActuatorError("package route must be an object")
        result.add(text(route.get("destination"), "route.destination"))
    return result


def source_urls(package: dict[str, Any]) -> list[str]:
    result: list[str] = []
    raw = package.get("sources")
    if not isinstance(raw, list):
        return result
    for source in raw:
        if not isinstance(source, dict):
            continue
        value = source.get("url")
        if isinstance(value, str) and value.startswith(("https://", "http://")) and value not in result:
            result.append(value)
    return result


def event_day(package: dict[str, Any]) -> date:
    days: list[date] = []
    raw = package.get("sources")
    if isinstance(raw, list):
        for source in raw:
            if not isinstance(source, dict):
                continue
            value = source.get("published_at")
            if not isinstance(value, str) or not value.strip():
                continue
            try:
                days.append(datetime.fromisoformat(value.strip().replace("Z", "+00:00")).date())
            except ValueError:
                try:
                    days.append(date.fromisoformat(value.strip()[:10]))
                except ValueError:
                    pass
    return max(days) if days else datetime.now(timezone.utc).date()


def publishable_claims(package: dict[str, Any]) -> list[dict[str, Any]]:
    raw = package.get("claims")
    if not isinstance(raw, list):
        raise ActuatorError("package claims must be a list")
    raw_sources = package.get("sources")
    has_primary = isinstance(raw_sources, list) and any(
        isinstance(source, dict) and source.get("source_class") == "primary"
        for source in raw_sources
    )
    result: list[dict[str, Any]] = []
    for claim in raw:
        if not isinstance(claim, dict):
            continue
        verification = claim.get("verification")
        confidence = claim.get("confidence")
        if verification in GOOD_VERIFICATIONS and confidence in {"medium", "high"}:
            result.append(claim)
        elif verification == "single_source" and confidence == "high" and has_primary:
            result.append(claim)
    return result


def existing_gls_ids(root: Path, package: dict[str, Any]) -> list[str]:
    candidates = sorted(set(re.findall(r"\bGLS-\d{4}\b", json.dumps(package, ensure_ascii=False))))
    ledger = (root / "models" / "THE_LIST.md").read_text(encoding="utf-8")
    return [model_id for model_id in candidates if model_id in ledger]


def derive_change_type(package: dict[str, Any], claims: list[dict[str, Any]]) -> str:
    beat = str(package.get("beat") or "")
    claim_types = {str(claim.get("claim_type") or "") for claim in claims}
    if "policy" in claim_types or beat == "privacy_policy":
        return "policy_change"
    if "research_result" in claim_types or beat == "research":
        return "research_release"
    if claim_types & {"release", "availability", "price"} or beat in {"products", "industry"}:
        return "availability_change"
    if beat in {"software_ai", "developer_open", "applications"}:
        return "software_release"
    if beat in {"displays_optics", "components"} or claim_types & {"spec", "feature"}:
        return "hardware_change"
    return "research_release"


def derive_topic(package: dict[str, Any]) -> str:
    topic = TOPIC_BY_BEAT.get(str(package.get("beat") or ""), "research_science")
    if topic not in VALID_TOPICS:
        raise ActuatorError(f"derived unknown alert topic: {topic}")
    return topic


def next_gre_id(ledger: str) -> str:
    numbers = [int(value) for value in re.findall(r'"id"\s*:\s*"GRE-(\d{6})"', ledger)]
    return f"GRE-{(max(numbers) if numbers else 0) + 1:06d}"


def append_gre(ledger: str, event: dict[str, Any]) -> str:
    closing = "\n  ]\n}"
    index = ledger.rfind(closing)
    if index < 0:
        raise ActuatorError("verified-changes ledger closing structure not recognized")
    prefix = ledger[:index].rstrip()
    if not prefix.endswith("}"):
        raise ActuatorError("verified-changes event list not recognized")
    rendered = json.dumps(event, ensure_ascii=False, indent=2)
    rendered = "\n".join("    " + line for line in rendered.splitlines())
    return prefix + ",\n" + rendered + closing + "\n"


def article_text(package_id: str, package: dict[str, Any], day: date, claims: list[dict[str, Any]], urls: list[str]) -> str:
    title = text(package.get("title"), "package.title")
    summary = text(package.get("summary"), "package.summary")
    reasons = [
        str(route.get("reason") or "").strip()
        for route in package.get("routes", [])
        if isinstance(route, dict) and str(route.get("reason") or "").strip()
    ]
    claims_md = "\n".join(f"- {str(claim.get('statement') or '').strip()}" for claim in claims)
    sources_md = "\n".join(f"- <{url}>" for url in urls)
    why = reasons[0] if reasons else "The second publication gate marked this as a material GlassesResearch development."
    return f"""# {title}

<!-- newsroom-package: {package_id} -->

**Published:** {heading_day(day)}  
**Status:** Verified newsroom publication

{summary}

## What we verified

{claims_md}

## Why it matters

{why}

## Evidence boundary

This article is compiled only from claims that crossed the News Desk publication threshold and from evidence sources preserved in the second-gate-approved package. Conflicting, unverified, or lower-confidence claims are not promoted here. The repository pull-request review is the final publication gate.

## Sources

{sources_md}
"""


def review_text(package_id: str, package: dict[str, Any], article_rel: str, urls: list[str], model_ids: list[str]) -> str:
    title = text(package.get("title"), "package.title")
    summary = text(package.get("summary"), "package.summary")
    models = ", ".join(f"`{model_id}`" for model_id in model_ids) if model_ids else "none — no existing canonical GLS identifier was resolved from the approved package"
    canonical = ", ".join(
        f"`{value}`"
        for value in ("docs/RESEARCH_NEWS.md", article_rel, "data/verified-changes.json")
    )
    return f"""# Newsroom promotion review — {title}

<!-- news_promotion_schema: 1 -->
<!-- newsroom-package: {package_id} -->

**Reviewer:** Live Editorial Desk second human gate; repository PR is the final publication gate  
**Candidate files surveyed:** `research/newsroom-packages/{package_id}.json`  
**Total raw candidates considered:** 1  
**Underlying developments after deduplication:** 1

> **Collection is not publication.** This package crossed the semantic gate and the explicit human publication gate. The canonical diff still requires normal repository review and merge.

## Summary

- Publish: 1
- Watch: 0
- Archive: 0
- Superseded: 0
- Reject: 0

### Development 1 — {title}

- **Candidate IDs:** `{package_id}`
- **Source URLs:** {' '.join(urls)}
- **Scope lane:** `core_glasses`
- **Event date:** derived from the newest dated evidence source in the approved package
- **Discovery date:** preserved in the live newsroom D1 audit trail
- **What happened:** {summary}
- **Why it may matter:** the approved semantic package routed this development to `news.publish`
- **Evidence quality:** only verified/corroborated claims, or high-confidence single-primary-source claims, cross this actuator
- **Affected models / lineages / technologies:** {models}
- **One-year institution test:** yes
- **Public-site eligible now:** yes, subject to repository PR review
- **Disposition:** `publish`
- **Reason for disposition:** second-gate-approved news-only promotion package
- **Affected models:** {models}
- **Affected lineages / platforms / resources:** none — this actuator refuses packages that request another canonical route rather than partially publishing them
- **Canonical destinations:** {canonical}
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

- [x] Duplicate/syndicated handling occurred upstream in the News Desk.
- [x] Public promotion passed the first editorial gate and second publication gate.
- [x] Raw package and evidence-source references remain preserved.
- [x] Publish decision identifies concrete canonical destinations.
- [x] Normal repository review and merge remain mandatory before this draft becomes public.
"""


def news_section(package_id: str, package: dict[str, Any], day: date, claims: list[dict[str, Any]], urls: list[str], article_rel: str) -> str:
    title = text(package.get("title"), "package.title")
    summary = text(package.get("summary"), "package.summary")
    claims_md = "\n".join(f"- {str(claim.get('statement') or '').strip()}" for claim in claims)
    sources_md = " · ".join(f"<{url}>" for url in urls)
    article_link = article_rel.removeprefix("docs/")
    return f"""### {heading_day(day)} — {title}

<!-- newsroom-package: {package_id} -->

{summary}

**Verified claims:**

{claims_md}

Continue: [verified article]({article_link})

Sources: {sources_md}

"""


def insert_news(news: str, package_id: str, package: dict[str, Any], day: date, section: str, article_rel: str) -> str:
    if f"newsroom-package: {package_id}" in news:
        return news
    marker = "|---|---|---|"
    marker_at = news.find(marker)
    if marker_at < 0:
        raise ActuatorError("Research & News latest-verified table marker not found")
    line_end = news.find("\n", marker_at)
    if line_end < 0:
        raise ActuatorError("Research & News latest-verified table is malformed")
    title = table_text(text(package.get("title"), "package.title"))
    summary = table_text(text(package.get("summary"), "package.summary"))
    article_link = article_rel.removeprefix("docs/")
    row = f"| {display_day(day)} | **{title}** — {summary} | [verified article]({article_link}) |\n"
    news = news[: line_end + 1] + row + news[line_end + 1 :]

    latest = news.find("## Latest verified")
    heading = news.find("\n### ", latest)
    if heading < 0:
        raise ActuatorError("Research & News first Latest verified story heading not found")
    insert_at = heading + 1
    return news[:insert_at] + section + news[insert_at:]


def already_applied(root: Path, package_id: str) -> bool:
    review_dir = root / "research" / "news-reviews"
    marker = f"newsroom-package: {package_id}"
    if not review_dir.exists():
        return False
    for path in review_dir.glob("*.md"):
        if marker in path.read_text(encoding="utf-8", errors="ignore"):
            return True
    return False


def apply_package(root: Path, package_path: Path) -> tuple[str, str]:
    package_id, package = load_envelope(package_path)
    if already_applied(root, package_id):
        return package_id, "already_applied"

    route_set = destinations(package)
    if route_set != SAFE_ROUTES:
        extra = route_set - SAFE_ROUTES
        return package_id, "blocked:" + (",".join(sorted(extra)) if extra else "no_news_publish_route")
    if package.get("confidence") not in {"medium", "high"}:
        return package_id, "blocked:story_confidence"

    claims = publishable_claims(package)
    if not claims:
        return package_id, "blocked:no_publishable_claims"
    urls = source_urls(package)
    if not urls:
        return package_id, "blocked:no_sources"

    day = event_day(package)
    story_key = str(package.get("story_key") or package.get("title") or package_id)
    slug = slugify(story_key)
    article_rel = f"docs/news/articles/{day.isoformat()}-{slug}.md"
    review_rel = f"research/news-reviews/{day.isoformat()}-newsroom-{slug}.md"
    article = root / article_rel
    review = root / review_rel
    marker = f"newsroom-package: {package_id}"
    if article.exists() and marker not in article.read_text(encoding="utf-8", errors="ignore"):
        return package_id, "blocked:article_path_exists"
    if review.exists() and marker not in review.read_text(encoding="utf-8", errors="ignore"):
        return package_id, "blocked:review_path_exists"

    news_path = root / "docs" / "RESEARCH_NEWS.md"
    gre_path = root / "data" / "verified-changes.json"
    news = news_path.read_text(encoding="utf-8")
    ledger = gre_path.read_text(encoding="utf-8")
    model_ids = existing_gls_ids(root, package)
    change_type = derive_change_type(package, claims)
    if change_type not in VALID_CHANGE_TYPES:
        raise ActuatorError(f"unsupported derived change type: {change_type}")
    topic = derive_topic(package)

    title = text(package.get("title"), "package.title")
    summary = text(package.get("summary"), "package.summary")
    source_heading = f"{heading_day(day)} — {title}"
    gre_event = {
        "id": next_gre_id(ledger),
        "state": "verified",
        "change_type": change_type,
        "verified_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "previous_state": "This second-gate-approved development was not yet represented as a verified canonical GlassesResearch publication.",
        "new_state": summary,
        "affected": {"model_ids": model_ids, "relationship_ids": []},
        "evidence_urls": urls,
        "publication": {
            "id": f"gr-{day.isoformat()}-{slug}",
            "dispatch": True,
            "source_heading": source_heading,
            "title": title,
            "canonical_url": f"https://glassesresearch.org/docs/news/articles/{day.isoformat()}-{slug}/",
            "summary": summary,
            "published_at": day.isoformat(),
        },
        "alert_match": {
            "models": model_ids,
            "brands_lineages": [],
            "topics": [topic],
        },
    }

    article.parent.mkdir(parents=True, exist_ok=True)
    review.parent.mkdir(parents=True, exist_ok=True)
    article.write_text(article_text(package_id, package, day, claims, urls), encoding="utf-8")
    review.write_text(review_text(package_id, package, article_rel, urls, model_ids), encoding="utf-8")
    section = news_section(package_id, package, day, claims, urls, article_rel)
    news_path.write_text(insert_news(news, package_id, package, day, section, article_rel), encoding="utf-8")
    gre_path.write_text(append_gre(ledger, gre_event), encoding="utf-8")
    return package_id, "applied_draft"


def apply_all(root: Path) -> list[tuple[str, str]]:
    package_dir = root / "research" / "newsroom-packages"
    return [apply_package(root, path) for path in sorted(package_dir.glob("GRNP-*.json"))]


def fixture(root: Path) -> Path:
    (root / "docs" / "news" / "articles").mkdir(parents=True)
    (root / "research" / "news-reviews").mkdir(parents=True)
    package_dir = root / "research" / "newsroom-packages"
    package_dir.mkdir(parents=True)
    (root / "data").mkdir(parents=True)
    (root / "models").mkdir(parents=True)
    (root / "docs" / "RESEARCH_NEWS.md").write_text(
        "# Research & News\n\n## Latest verified\n\n| Date | What changed | Go deeper |\n|---|---|---|\n| Aug. 28 | Old item | old |\n\n### August 28, 2026 — Old item\n\nOld.\n",
        encoding="utf-8",
    )
    (root / "data" / "verified-changes.json").write_text(
        '{\n  "schema_version": 1,\n  "events": [\n    {"id":"GRE-000001"}\n  ]\n}\n',
        encoding="utf-8",
    )
    (root / "models" / "THE_LIST.md").write_text("GLS-0001 Example Glasses\n", encoding="utf-8")
    envelope = {
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
            "claims": [{
                "claim_id": "claim-1",
                "normalized_key": "release",
                "statement": "GLS-0001 Example Glasses launched.",
                "claim_type": "release",
                "verification": "verified",
                "confidence": "high",
            }],
            "sources": [{
                "source_id": "source-1",
                "url": "https://example.com/glasses",
                "publisher": "Example",
                "source_class": "primary",
                "published_at": "2026-09-01",
            }],
            "routes": [{
                "route_id": "route-1",
                "destination": "news.publish",
                "reason": "Material launch",
                "payload": {},
                "created_at": "2026-09-01T00:00:00Z",
            }],
        },
    }
    path = package_dir / "GRNP-TEST00000001.json"
    path.write_text(json.dumps(envelope, indent=2) + "\n", encoding="utf-8")
    return path


def self_test() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        package = fixture(root)
        assert apply_package(root, package) == ("GRNP-TEST00000001", "applied_draft")
        news = (root / "docs" / "RESEARCH_NEWS.md").read_text(encoding="utf-8")
        ledger_text = (root / "data" / "verified-changes.json").read_text(encoding="utf-8")
        ledger = json.loads(ledger_text)
        assert "newsroom-package: GRNP-TEST00000001" in news
        assert ledger["events"][-1]["id"] == "GRE-000002"
        assert ledger["events"][-1]["affected"]["model_ids"] == ["GLS-0001"]
        assert ledger["events"][-1]["publication"]["dispatch"] is True
        assert ledger["events"][-1]["alert_match"]["topics"] == ["release_availability"]
        assert apply_package(root, package) == ("GRNP-TEST00000001", "already_applied")

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        package = fixture(root)
        envelope = json.loads(package.read_text(encoding="utf-8"))
        envelope["package"]["routes"].append({
            "route_id": "route-2",
            "destination": "catalog.update",
            "reason": "Catalog must change too",
            "payload": {},
            "created_at": "2026-09-01T00:00:00Z",
        })
        package.write_text(json.dumps(envelope, indent=2) + "\n", encoding="utf-8")
        before = (root / "docs" / "RESEARCH_NEWS.md").read_text(encoding="utf-8")
        assert apply_package(root, package) == ("GRNP-TEST00000001", "blocked:catalog.update")
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
        results = [apply_package(args.root, args.package)] if args.package else apply_all(args.root)
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
