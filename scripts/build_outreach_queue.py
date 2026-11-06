#!/usr/bin/env python3
"""Produce a HUMAN-REVIEW-ONLY outreach queue from already published answers.

No platform authentication, network requests, messages, or posting actions.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ORIGIN = "https://glassesresearch.org"
SOURCES = {
    "reddit_rss": ("Reddit", {"reddit.com", "www.reddit.com"}),
    "github_issues": ("GitHub", {"github.com"}),
    "stackexchange": ("Stack Exchange", {"stackoverflow.com", "superuser.com", "electronics.stackexchange.com", "stackexchange.com"}),
}
ORDER = {"Reddit": 0, "GitHub": 1, "Stack Exchange": 2}


def build_candidates(registry: dict, outcomes: dict | None = None) -> list[dict]:
    """Match original community threads to published answer URLs; never auto-post."""
    decided = {item.get("source_url") for item in (outcomes or {}).get("entries", [])
               if item.get("status") in {"posted", "skipped"}}
    grouped: dict[str, dict] = {}
    for question in registry.get("questions", []):
        if question.get("status") != "answered" or question.get("evidence_state") != "published":
            continue
        path = question.get("answer_url")
        if not isinstance(path, str) or not path.startswith("/") or path.startswith("//"):
            continue
        for observation in question.get("observations", []):
            kind = observation.get("source")
            if kind not in SOURCES:
                continue
            source_url = observation.get("source_url", "")
            if not isinstance(source_url, str):
                continue
            parsed = urlparse(source_url)
            platform, hosts = SOURCES[kind]
            if parsed.scheme != "https" or parsed.hostname not in hosts or not parsed.path:
                continue
            if source_url in decided:
                continue
            entry = grouped.setdefault(source_url, {
                "source_url": source_url, "platform": platform,
                "questions": [], "last_observed": question.get("last_observed", ""),
            })
            item = {
                "id": question.get("id", ""),
                "question": question.get("canonical_question", ""),
                "answer_url": ORIGIN + path,
            }
            if item not in entry["questions"]:
                entry["questions"].append(item)
            entry["last_observed"] = max(entry["last_observed"], question.get("last_observed", ""))
    return sorted(grouped.values(), key=lambda item: (
        ORDER[item["platform"]], item["last_observed"], item["source_url"]
    ), reverse=False)


def sample_for_review(items: list[dict], limit: int) -> list[dict]:
    """Round-robin by platform for architecture testing, most recently observed first."""
    platforms = ("Reddit", "GitHub", "Stack Exchange")
    buckets = {
        p: sorted((c for c in items if c["platform"] == p),
                  key=lambda c: (c["last_observed"], c["source_url"]), reverse=True)
        for p in platforms
    }
    chosen = []
    while len(chosen) < limit and any(buckets.values()):
        for platform in platforms:
            if buckets[platform] and len(chosen) < limit:
                chosen.append(buckets[platform].pop(0))
    return chosen


def render_markdown(items: list[dict], limit: int) -> str:
    listed = sample_for_review(items, limit)
    lines = [
        "# Community outreach — review queue",
        "",
        "> **DRAFT CANDIDATES ONLY. Nothing here has been posted or approved.**",
        "> Original discussions may be locked, outdated, removed, or unsuitable for outreach.",
        "> Source discovery and our published-answer registry do **not** establish thread activity,",
        "> answer accuracy today, forum permission to link, or eligibility to reply.",
        "",
        f"- Matched community threads in registry: **{len(items)}**",
        f"- Displayed for human review: **{len(listed)}**",
        "- Posted replies confirmed by this queue: **0** (posting is not a feature of this tool)",
        "",
        "| Community | Original discussion | Related published answer | Last observed | Review |",
        "|---|---|---|---|---|",
    ]
    for item in listed:
        q = item["questions"][0]
        label = str(q["question"]).replace("|", "/").replace("[", "").replace("]", "")
        label = label[:105] + ("…" if len(label) > 105 else "")
        answer = q["answer_url"]
        lines.append(f'| {item["platform"]} | [Original thread]({item["source_url"]}) — {label} | [Answer]({answer})' +
                     (f' (+{len(item["questions"])-1} related)' if len(item["questions"]) > 1 else '') +
                     f' | {item["last_observed"]} | Context, recency, and community rules **unchecked** |')
    lines += [
        "",
        "## What a reviewer must establish before any reply",
        "",
        "1. Open the original discussion and confirm the question, date, context, and whether replies are allowed.",
        "2. Check subreddit/forum rules and any conflict-of-interest disclosure requirements.",
        "3. Re-read the linked answer and primary evidence; fix outdated or unsupported claims first.",
        "4. Write a genuinely helpful, tailored answer directly in the discussion. Link only if relevant and permitted.",
        "5. Have a human approve and post it. Log the original thread URL, action, date, and any observed outcome separately.",
        "6. No mass-posting, unsolicited DMs, vote manipulation, or automated social-platform posting.",
        "",
        "Regenerate from repository data: `python scripts/build_outreach_queue.py`.",
        "Human decisions persist in `operations/outreach/outcomes.json` and are never inferred from this queue.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=Path("research/questions/registry.json"))
    parser.add_argument("--outcomes", type=Path, default=Path("operations/outreach/outcomes.json"))
    parser.add_argument("--output", type=Path, default=Path("operations/outreach/queue.md"))
    parser.add_argument("--limit", type=int, default=15)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    registry = json.loads(args.registry.read_text(encoding="utf-8"))
    outcomes = json.loads(args.outcomes.read_text(encoding="utf-8")) if args.outcomes.exists() else {"entries": []}
    content = render_markdown(build_candidates(registry, outcomes), args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(content, encoding="utf-8")
    print(f"Prepared review-only outreach queue: {args.output}")


if __name__ == "__main__":
    main()
