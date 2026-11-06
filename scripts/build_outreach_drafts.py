#!/usr/bin/env python3
"""Create offline reply-review packets. Never contact a platform or publish messages."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from scripts.build_outreach_queue import build_candidates
except ModuleNotFoundError:
    from build_outreach_queue import build_candidates

REQUIRED_CHECKS = (
    "thread_context_reviewed", "thread_accepts_replies", "community_rules_reviewed",
    "added_value_confirmed", "published_answer_rechecked", "affiliation_policy_reviewed",
)


def validate_candidates(raw: dict, candidates: list[dict]) -> dict[str, dict]:
    if raw.get("schema_version") != 1 or not isinstance(raw.get("entries"), list):
        raise ValueError("invalid candidate-decisions schema")
    known = {c["source_url"] for c in candidates}
    seen = {}
    for item in raw["entries"]:
        if not isinstance(item, dict):
            raise ValueError("candidate decision must be an object")
        url, decision = item.get("source_url"), item.get("decision")
        if url not in known or url in seen:
            raise ValueError("unknown or duplicate original discussion")
        if decision not in {"hold", "skip", "approved_for_drafting"}:
            raise ValueError("invalid candidate review decision")
        if decision == "approved_for_drafting":
            if not item.get("reviewer") or not item.get("reviewed_at") or not str(item.get("notes", "")).strip():
                raise ValueError("human reviewer, date, and contextual notes required")
            if any(item.get(field) is not True for field in REQUIRED_CHECKS):
                raise ValueError("candidate approval needs all six manual checks")
        seen[url] = item
    return seen


def validate_drafts(raw: dict, approved: dict, candidates: list[dict]) -> dict[str, dict]:
    if raw.get("schema_version") != 1 or not isinstance(raw.get("entries"), list):
        raise ValueError("invalid draft submissions schema")
    known = {c["source_url"]: c for c in candidates}
    result = {}
    for item in raw["entries"]:
        if not isinstance(item, dict):
            raise ValueError("draft must be an object")
        url = item.get("source_url")
        if url in result or url not in approved:
            raise ValueError("draft requires one uniquely approved candidate")
        answers = {q["answer_url"] for q in known[url]["questions"]}
        if item.get("answer_url") not in answers:
            raise ValueError("draft must link its original approved answer")
        body = item.get("reply_body")
        if not isinstance(body, str) or not body.strip() or len(body) > 12000 or not item.get("author"):
            raise ValueError("draft requires nonempty reply text and author")
        result[url] = item
    return result


def validate_reply_reviews(raw: dict, drafts: dict) -> dict[str, dict]:
    if raw.get("schema_version") != 1 or not isinstance(raw.get("entries"), list):
        raise ValueError("invalid reply review schema")
    seen = {}
    for item in raw["entries"]:
        if not isinstance(item, dict):
            raise ValueError("reply review must be an object")
        url, status = item.get("source_url"), item.get("decision")
        if url not in drafts or url in seen:
            raise ValueError("review requires one existing draft")
        if status not in {"pending", "request_revision", "accepted_for_dry_run_only"}:
            raise ValueError("no posting or publication status is supported")
        if status != "pending" and (not item.get("reviewer") or not item.get("reviewed_at")):
            raise ValueError("reviewer and date required for reply decision")
        seen[url] = item
    return seen


def render_packets(candidates: list[dict], approvals: dict, drafts: dict, reviews: dict) -> str:
    eligible = [c for c in candidates if c["source_url"] in approvals]
    lines = [
        "# Reply review packets — OFFLINE DRY RUN", "",
        "> **NOT FOR POSTING.** This document is not sent to any person or platform.",
        "> Gate 1 permits drafting only. Gate 2 cannot publish.", "",
        f"- Human-approved candidate discussions: **{len(eligible)}**",
        f"- Human-authored replies prepared for review: **{len(drafts)}**",
        "- Platform replies sent: **0** (no sender exists in this pipeline)", "",
    ]
    if not eligible:
        lines += ["## Gate 1: awaiting candidate review", "",
                  "No candidates approved, so there are no proposed replies. Review queue.md first.", ""]
    for candidate in eligible:
        url = candidate["source_url"]
        decision = approvals[url]
        reply = drafts.get(url)
        review = reviews.get(url, {})
        q = candidate["questions"][0]
        lines += [f"## {candidate['platform']} — {q['id']}", "",
                  f"- Original discussion: {url}",
                  f"- Original question: {q['question']}",
                  f"- Evidence-linked research: {q['answer_url']}",
                  f"- Candidate reviewer: {decision['reviewer']} ({decision['reviewed_at']})",
                  f"- Review notes: {decision['notes']}",
                  f"- Reply-stage decision: **{review.get('decision', 'not_submitted')}**", ""]
        if reply:
            lines += ["### Proposed answer — review only", "",
                      f"Draft author: {reply['author']}", "",
                      "~~~text", reply["reply_body"].replace("~~~", "---"), "~~~", "",
                      "Check factual accuracy, provenance, local rules, affiliation, relevance,",
                      "whether a link is necessary, and usefulness without any click.", ""]
        else:
            lines += ["### Not yet authored", "",
                      "No answer text can be reviewed until an author prepares a complete reply.", ""]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    root = Path("operations/outreach")
    parser.add_argument("--registry", type=Path, default=Path("research/questions/registry.json"))
    parser.add_argument("--outcomes", type=Path, default=root / "outcomes.json")
    parser.add_argument("--decisions", type=Path, default=root / "candidate_decisions.json")
    parser.add_argument("--drafts", type=Path, default=root / "draft_submissions.json")
    parser.add_argument("--reviews", type=Path, default=root / "draft_decisions.json")
    parser.add_argument("--output", type=Path, default=root / "replies_for_review.md")
    args = parser.parse_args()
    def load(p): return json.loads(p.read_text(encoding="utf-8"))
    candidates = build_candidates(load(args.registry), load(args.outcomes))
    decisions = validate_candidates(load(args.decisions), candidates)
    approved = {u: x for u, x in decisions.items() if x["decision"] == "approved_for_drafting"}
    drafts = validate_drafts(load(args.drafts), approved, candidates)
    reviews = validate_reply_reviews(load(args.reviews), drafts)
    text = render_packets(candidates, approved, drafts, reviews)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"Offline review packets: {len(approved)} candidates, {len(drafts)} replies; posted: 0")


if __name__ == "__main__":
    main()
