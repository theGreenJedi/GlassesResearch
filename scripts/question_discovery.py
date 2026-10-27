#!/usr/bin/env python3
"""Find real smart-glasses questions across independent sources, then maintain the registry.

Discovery is not publication. Questions require an evidence-backed answer before
they may move to "answered". Search Console is a *supplementary* performance
signal, never a prerequisite for question discovery.
"""
from __future__ import annotations

import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from html import unescape
from pathlib import Path
from urllib.parse import quote

import requests

REGISTRY = Path("research/questions/registry.json")
FAQ_ROOT = Path("docs/faq")
SOURCES = Path("research/question-sources.json")
REPORT_JSON = Path("analytics/question-discovery.json")
REPORT_MD = Path("analytics/question-discovery.md")
MINIMUM_PUBLISHED_ANSWERS = 1000
QUESTION_WORDS = (
    "who ", "what ", "when ", "where ", "why ", "how ", "can ", "could ",
    "do ", "does ", "did ", "is ", "are ", "will ", "would ", "should ",
    "which ", "whereas ", "anyone know ", "has anyone ", "is there ",
)
SMART_TERMS = (
    "smart glass", "ai glass", "ar glass", "xr glass", "wearable display",
    "ray-ban meta", "ray ban meta", "spectacles", "inmo", "rokid",
    "vuzix", "realwear", "solos airgo", "brilliant labs", "even realities",
    "myvu", "heycyan", "waveguide", "mentra", "halliday", "xreal",
    "caption glass", "camera glass", "google glass", "optical see-through",
    "open source glass", "recon jet", "north focals", "micro-led waveguide",
)
GITHUB_REPO_TERMS = ("mentra", "rokid", "vuzix", "rayneo", "xreal", "smartglass",
                     "smart-glass", "evenrealities", "brilliant-labs", "inmo", "myvu")
HEADERS = {"User-Agent": "GlassesResearch-question-discovery/1.0 (+https://glassesresearch.org/)"}
SOURCE_WARNINGS = {}



def norm(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", " ", s.casefold()).strip()
    return re.sub(r"\s+", " ", s)


def clean(s: str) -> str:
    raw = unescape(s or "")
    raw = re.sub(r"https?://[^\s<>'\"]+", " ", raw)
    raw = re.sub(r"<[^>]*>", " ", raw)
    raw = re.sub(r"\b(?:www\.)?[^\s/]+\.(?:com|org|net|io|dev|ai)/[^\s]+", " ", raw)
    return re.sub(r"\s+", " ", raw).strip()


def looks_like_question(s: str, *, scoped: bool = False) -> bool:
    """Source context can establish relevance; GSC queries require topical words."""
    s = clean(s)
    n = norm(s)
    if len(s) < 15 or len(s) > 250:
        return False
    if not (s.endswith("?") or n.startswith(QUESTION_WORDS)):
        return False
    return scoped or any(t in n for t in SMART_TERMS)


def questions_from_text(title: str, body: str = "", *, scoped: bool = False) -> list[str]:
    """Preserve real question wording; never invent questions from keywords."""
    candidates = [clean(title)]
    # Forum body snippets may contain a literal question absent from the title.
    for raw in re.split(r"[\r\n]+|(?<=\?)\s+", body[:5000]):
        for match in re.finditer(r"[^.!?\n]{15,220}\?", clean(raw)):
            candidates.append(match.group(0).strip(" -:"))
    result, seen = [], set()
    for candidate in candidates:
        n = norm(candidate)
        if n not in seen and looks_like_question(candidate, scoped=scoped):
            result.append(candidate)
            seen.add(n)
    return result[:5]


def gsc_token():
    raw = os.getenv("GOOGLE_SEARCH_CONSOLE_CREDENTIALS", "").strip()
    site = os.getenv("GOOGLE_SEARCH_CONSOLE_SITE_URL", "").strip()
    if not raw or not site:
        raise RuntimeError("GSC credentials/property unavailable (optional discovery sensor)")
    from google.auth.transport.requests import Request
    from google.oauth2 import service_account
    creds = service_account.Credentials.from_service_account_info(
        json.loads(raw), scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
    )
    creds.refresh(Request())
    return creds.token, site


def gsc_questions() -> list[dict]:
    token, site = gsc_token()
    end = date.today() - timedelta(days=2)
    start = end - timedelta(days=27)
    endpoint = "https://searchconsole.googleapis.com/webmasters/v3/sites/" + quote(site, safe="") + "/searchAnalytics/query"
    r = requests.post(endpoint, headers={"Authorization": f"Bearer {token}"}, json={
        "startDate": start.isoformat(), "endDate": end.isoformat(),
        "type": "web", "dataState": "final", "dimensions": ["query"],
        "rowLimit": 25000,
    }, timeout=45)
    r.raise_for_status()
    out = []
    for row in r.json().get("rows", []):
        q = (row.get("keys") or [""])[0].strip()
        if looks_like_question(q):
            out.append({
                "question": q, "source": "google_search_console",
                "observed_at": end.isoformat(),
                "metrics": {key: float(row.get(key, 0)) for key in ("clicks", "impressions", "ctr", "position")},
            })
    return out


def github_questions(queries: list[str]) -> list[dict]:
    """Search third-party public issues; do not search only our own repository."""
    token = os.getenv("GITHUB_TOKEN", "").strip()
    headers = {**HEADERS, "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    out = []
    errors = []
    for query in queries:
        try:
            r = requests.get("https://api.github.com/search/issues", params={
                "q": f"{query} is:issue -repo:theGreenJedi/GlassesResearch",
                "per_page": 50, "sort": "updated", "order": "desc",
            }, headers=headers, timeout=35)
            r.raise_for_status()
            items = r.json().get("items", [])
        except Exception as exc:
            errors.append(f"{query}: {exc}")
            continue
        for item in items:
            title = clean(item.get("title") or "")
            url = item.get("html_url") or ""
            title_scoped = any(term in norm(title) for term in SMART_TERMS)
            repo_scoped = any(term in url.casefold().split("/issues/")[0] for term in GITHUB_REPO_TERMS)
            if not (title_scoped or repo_scoped):
                # Full-text GitHub search also returns spam/link dumps which merely
                # *mention* glasses. Do not harvest arbitrary questions from those.
                continue
            candidates = questions_from_text(title, "", scoped=True)
            # Additional questions in an issue body must individually mention a
            # scoped glasses/model concept; context cannot launder off-topic text.
            candidates += questions_from_text("", item.get("body") or "", scoped=False)
            for q in dict.fromkeys(candidates):
                out.append({
                    "question": q, "source": "github_issues",
                    "source_url": item.get("html_url"),
                    "observed_at": date.today().isoformat(),
                    "metrics": {"comments": item.get("comments", 0),
                                "reactions": (item.get("reactions") or {}).get("total_count", 0)},
                })
    if errors:
        SOURCE_WARNINGS["github_issues"] = errors[:5]
        if len(errors) == len(queries):
            raise RuntimeError(f"all GitHub search queries failed: {errors[0]}")
    return out


def stackexchange_questions(searches: list[dict]) -> list[dict]:
    out = []
    errors = []
    for spec in searches:
        try:
            r = requests.get("https://api.stackexchange.com/2.3/search/advanced", params={
                "site": spec["site"], "q": spec["q"], "sort": "activity",
                "order": "desc", "pagesize": 75,
            }, headers=HEADERS, timeout=35)
            r.raise_for_status()
            payload = r.json()
            if payload.get("error_id"):
                raise RuntimeError(payload.get("error_message", "Stack Exchange API error"))
            items = payload.get("items", [])
        except Exception as exc:
            errors.append(f"{spec}: {exc}")
            continue
        for item in items:
            # Stack Exchange posts are user questions, even without a trailing ?.
            q = clean(item.get("title") or "")
            context = norm(q + " " + " ".join(item.get("tags", [])))
            if not (15 <= len(q) <= 250 and any(t in context for t in SMART_TERMS)):
                continue
            out.append({
                "question": q, "source": "stackexchange",
                "source_url": item.get("link"),
                "observed_at": date.today().isoformat(),
                "metrics": {"score": item.get("score", 0), "answer_count": item.get("answer_count", 0)},
            })
    if errors:
        SOURCE_WARNINGS["stackexchange"] = errors[:5]
        if len(errors) == len(searches):
            raise RuntimeError(f"all Stack Exchange searches failed: {errors[0]}")
    return out


def reddit_rss_questions(feeds: list[str]) -> list[dict]:
    out = []
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    errors = []
    for feed in feeds:
        try:
            r = requests.get(feed, headers=HEADERS, timeout=35)
            r.raise_for_status()
            root = ET.fromstring(r.text)
        except Exception as exc:
            errors.append(f"{feed}: {exc}")
            continue
        for entry in root.findall("atom:entry", ns):
            title = entry.findtext("atom:title", default="", namespaces=ns)
            link = entry.find("atom:link", ns)
            url = link.get("href") if link is not None else None
            # Reddit post titles are the actual questions. Do not mine image alt
            # text, cross-posted links or unrelated comments from HTML bodies.
            for q in questions_from_text(title, "", scoped=True):
                out.append({
                    "question": q, "source": "reddit_rss", "source_url": url,
                    "observed_at": date.today().isoformat(),
                })
    if errors:
        SOURCE_WARNINGS["reddit_rss"] = errors[:5]
        if len(errors) == len(feeds):
            raise RuntimeError(f"all Reddit RSS feeds failed: {errors[0]}")
    return out


def external_questions() -> list[dict]:
    """Additional owner-approved JSON feeds remain supported."""
    out = []
    for url in [x.strip() for x in os.getenv("QUESTION_DISCOVERY_FEEDS", "").split(",") if x.strip()]:
        try:
            r = requests.get(url, headers=HEADERS, timeout=30)
            r.raise_for_status()
            payload = r.json()
            rows = payload if isinstance(payload, list) else payload.get("questions", [])
            for item in rows:
                q = item if isinstance(item, str) else item.get("question", "")
                if q and looks_like_question(q):
                    out.append({"question": clean(q), "source": "approved_feed",
                                "source_url": url, "observed_at": date.today().isoformat()})
        except Exception as exc:
            print(f"Approved question feed unavailable {url}: {exc}", file=sys.stderr)
    return out


def seed_published_answers(reg: dict) -> dict:
    """Reconcile existing visible FAQ questions without overwriting evidence."""
    by_norm = {q["normalized"]: q for q in reg["questions"]}
    pattern = re.compile(r"^#{2,3}\s+(?:\d+\.\s+)?(.+?\?)\s*$", re.M)
    for path in sorted(FAQ_ROOT.glob("*.md")):
        if path.name in {"README.md", "ASK_YOUR_OWN_QUESTION.md", "COMMUNITY_QUESTIONS.md"}:
            continue
        for match in pattern.finditer(path.read_text(encoding="utf-8")):
            question = match.group(1).strip()
            normalized = norm(question)
            slug = re.sub(r"[^a-z0-9 -]", "", match.group(0).lstrip("# ").casefold())
            slug = re.sub(r"\s+", "-", slug).strip("-")
            answer_url = f"/docs/faq/{path.stem}/#{slug}"
            if normalized in by_norm:
                item = by_norm[normalized]
                if item.get("answer_url") is None:
                    item["answer_url"] = answer_url
                    item["status"] = "answered"
                    item["evidence_state"] = "published"
                continue
            item = {
                "id": f"Q-{reg['next_id']:06d}", "canonical_question": question,
                "normalized": normalized, "variants": [question],
                "status": "answered", "first_observed": "published_corpus",
                "last_observed": "published_corpus",
                "observations": [{"question": question, "source": "published_practical_answers",
                                  "observed_at": "published_corpus"}],
                "answer_url": answer_url, "evidence_state": "published",
            }
            reg["next_id"] += 1
            reg["questions"].append(item)
            by_norm[normalized] = item
    return reg


def load_registry() -> dict:
    if REGISTRY.exists():
        # Once initialized, the registry is authoritative. Newly authored FAQ
        # headings are NOT publication proof: an explicit live-site gate must
        # credit the original observed question ID and canonical answer URL.
        # Automatic re-seeding would create duplicate IDs and inflate counts.
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    # The bootstrap scan only initializes a previously absent registry from
    # established published FAQ content; it never runs on an existing ledger.
    return seed_published_answers({
        "schema_version": 1,
        "principle": "1,000 published evidence-backed answers minimum; no maximum. Questions are discovered from real-world demand, independent of our site's search performance.",
        "next_id": 1, "questions": [],
    })


def observation_identity(obs: dict) -> tuple:
    # Repeated crawls of the same forum post are one observation, not artificial demand.
    if obs.get("source_url"):
        return (obs["source"], obs["source_url"], norm(obs["question"]))
    return (obs["source"], obs.get("observed_at"), norm(obs["question"]))


def reconcile(reg: dict, observations: list[dict]) -> list[dict]:
    by_norm = {q["normalized"]: q for q in reg["questions"]}
    new = []
    for obs in observations:
        n = norm(obs["question"])
        if not n:
            continue
        if n in by_norm:
            item = by_norm[n]
            seen = {observation_identity(old) for old in item.get("observations", [])}
            if observation_identity(obs) not in seen:
                item.setdefault("observations", []).append(obs)
                item["last_observed"] = obs["observed_at"]
            if obs["question"] not in item.setdefault("variants", []):
                item["variants"].append(obs["question"])
            continue
        item = {
            "id": f"Q-{reg['next_id']:06d}", "canonical_question": obs["question"],
            "normalized": n, "variants": [obs["question"]],
            "status": "observed", "first_observed": obs["observed_at"],
            "last_observed": obs["observed_at"], "observations": [obs],
            "answer_url": None, "evidence_state": "unresearched",
        }
        reg["next_id"] += 1
        reg["questions"].append(item)
        by_norm[n] = item
        new.append(item)
    return new


def priority(item: dict) -> tuple:
    """Order the research queue by independent observations, not site clicks."""
    obs = item.get("observations", [])
    independent = [o for o in obs if o.get("source") not in (
        "google_search_console", "published_practical_answers"
    )]
    distinct_posts = len({o.get("source_url", o.get("question")) for o in independent})
    return (distinct_posts, len({o.get("source") for o in independent}),
            sum(max(0, float(o.get("metrics", {}).get("score", 0) or 0)) for o in independent))


def main() -> int:
    SOURCE_WARNINGS.clear()
    reg = load_registry()
    reg["principle"] = (
        "At least 1,000 published, evidence-backed answers; no ceiling. "
        "Discover real questions across the internet regardless of GlassesResearch search visibility."
    )
    cfg = json.loads(SOURCES.read_text(encoding="utf-8"))
    observations, statuses = [], {}
    sensors = (
        ("github_issues", lambda: github_questions(cfg["github_queries"])),
        ("stackexchange", lambda: stackexchange_questions(cfg["stackexchange"])),
        ("reddit_rss", lambda: reddit_rss_questions(cfg["reddit_rss"])),
        ("google_search_console", gsc_questions),
        ("approved_feed", external_questions),
    )
    working_independent_sources = 0
    for name, collect in sensors:
        try:
            batch = collect()
            observations.extend(batch)
            statuses[name] = {"status": "partial" if name in SOURCE_WARNINGS else "ok", "observations": len(batch)}
            if name in SOURCE_WARNINGS:
                statuses[name]["warnings"] = SOURCE_WARNINGS[name]
            if name in {"github_issues", "stackexchange", "reddit_rss"} and (cfg.get({"github_issues":"github_queries", "stackexchange":"stackexchange", "reddit_rss":"reddit_rss"}[name]) or batch):
                working_independent_sources += 1
            if name == "approved_feed" and batch:
                working_independent_sources += 1
        except Exception as exc:
            statuses[name] = {"status": "unavailable", "error": str(exc)[:300]}
            print(f"{name} discovery unavailable: {exc}", file=sys.stderr)
    if not working_independent_sources:
        raise RuntimeError("No independent internet question sources worked; refusing a false successful refresh")
    newly_found = reconcile(reg, observations)
    answered = len({q["answer_url"] for q in reg["questions"] if q["status"] == "answered" and q.get("answer_url")})
    pending = [q for q in reg["questions"] if q["status"] in {"observed", "triaged", "researching"}]
    pending.sort(key=priority, reverse=True)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    reg["updated_at"] = now
    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY.write_text(json.dumps(reg, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    payload = {
        "generated_at": now, "observations": len(observations),
        "new_questions": len(newly_found), "registry_size": len(reg["questions"]),
        "published_answers": answered, "minimum_published_answers": MINIMUM_PUBLISHED_ANSWERS,
        "remaining_to_minimum": max(0, MINIMUM_PUBLISHED_ANSWERS - answered),
        "pending_research": len(pending), "sources": statuses,
        "questions": [{key: q[key] for key in ("id", "canonical_question", "observations")}
                      for q in newly_found],
        "research_queue": [{
            "id": q["id"], "question": q["canonical_question"], "priority": priority(q),
            "source_urls": sorted({o["source_url"] for o in q.get("observations", []) if o.get("source_url")}),
        } for q in pending[:100]],
    }
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Question Discovery — Latest", "", f"Generated: **{now}**", "",
        f"- Published evidence-backed answers: **{answered}** (minimum **{MINIMUM_PUBLISHED_ANSWERS}**, no ceiling)",
        f"- Remaining to minimum: **{max(0, MINIMUM_PUBLISHED_ANSWERS - answered)}**",
        f"- Canonical registry size: **{len(reg['questions'])}** (not the published count)",
        f"- Unanswered research candidates: **{len(pending)}**",
        f"- Observations this run: **{len(observations)}**",
        f"- New distinct questions: **{len(newly_found)}**",
        "", "## Source health", "",
    ]
    lines += [f"- {name}: {state['status']}" +
              (f" — {state['observations']} observations" if state["status"] in {"ok", "partial"}
               else f" — {state.get('error', '')}")
              for name, state in statuses.items()]
    lines += ["", "## New questions", ""]
    lines += [f"- **{q['id']}** — {q['canonical_question']}" for q in newly_found[:50]] or [
        "_No new materially distinct questions in this run._"
    ]
    lines += ["", "## Research queue (first 20)", ""]
    lines += [f"- **{q['id']}** — {q['canonical_question']}" for q in pending[:20]] or ["_None._"]
    lines += [
        "", "> A discovered question is not an answered question. Research, independently verify evidence, "
        "and publish only what the sources support. Search Console is optional performance feedback, "
        "never an eligibility requirement.", "",
    ]
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(REPORT_MD.read_text())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
