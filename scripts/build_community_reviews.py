#!/usr/bin/env python3
"""Validate accepted community reviews and build public summaries/profiles.

Community scores remain a separate evidence layer. They never overwrite the
canonical GlassesResearch Report Card.
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

DIMENSIONS = (
    "discreetness",
    "camera",
    "visual_ai",
    "hackability",
    "owner_control",
    "android_compatibility",
)
DIMENSION_LABELS = {
    "discreetness": "Discreetness",
    "camera": "Camera",
    "visual_ai": "Visual AI",
    "hackability": "Hackability",
    "owner_control": "Owner Control",
    "android_compatibility": "Android Compatibility",
}
REVIEW_ID = re.compile(r"^GR-CR-\d{4,}$")
REVIEWER_ID = re.compile(r"^GR-C-\d{4,}$")
MODEL_ID = re.compile(r"^GLS-\d{4}$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def score_summary(values: list[int]) -> dict:
    if not values:
        return {"n": 0, "median": None, "min": None, "max": None, "distribution": {}}
    counts = Counter(values)
    median_value = statistics.median(values)
    if isinstance(median_value, float) and median_value.is_integer():
        median_value = int(median_value)
    return {
        "n": len(values),
        "median": median_value,
        "min": min(values),
        "max": max(values),
        "distribution": {str(score): counts.get(score, 0) for score in range(11) if counts.get(score, 0)},
    }


def reviewer_public_name(reviewer: dict) -> str:
    return str(reviewer.get("public_name") or reviewer["reviewer_id"])


def render_profile(reviewer: dict, reviews: list[dict], devices: dict[str, dict]) -> str:
    name = reviewer_public_name(reviewer)
    joined = reviewer.get("joined_at") or "Unknown"
    bio = str(reviewer.get("bio") or "").strip()
    model_ids = sorted({review["model_id"] for review in reviews})
    ownership_evidence = sum(review.get("ownership_evidence") in {"supplied_private", "supplied_public"} for review in reviews)
    rows = []
    for review in sorted(reviews, key=lambda item: (item.get("accepted_at") or "", item["review_id"]), reverse=True):
        device = devices[review["model_id"]]
        rows.append(
            f"- **{review['review_id']}** — "
            f"[{device.get('maker', '')} {device.get('model', review['model_id'])}]"
            f"(/models/catalog/{review['model_id'].lower()}/) — accepted {review.get('accepted_at', 'unknown date')}"
        )
    profile_link = reviewer.get("profile_url")
    link_line = f"\nPublic link: {profile_link}\n" if profile_link else ""
    bio_block = f"\n{bio}\n" if bio else ""
    return f'''---
title: "{name.replace('"', '\\"')} — community contributor"
description: "Accepted independent hands-on smart-glasses reviews contributed by {name.replace('"', '\\"')} to GlassesResearch."
---

# {name}

Independent community contributor since **{joined}**.{link_line}{bio_block}

| Contribution record | Count |
|---|---:|
| Accepted hands-on reviews | **{len(reviews)}** |
| Distinct canonical models | **{len(model_ids)}** |
| Reviews with ownership evidence supplied | **{ownership_evidence}** |

This page is a contribution history, not an authority or trust score. Every claim remains governed by its own evidence and corroboration.

## Accepted reviews

{chr(10).join(rows) if rows else '- No accepted reviews yet.'}

## Evidence rule

A long contributor history does not make a new claim automatically true. GlassesResearch evaluates each submission on its evidence, device context, reproducibility, and independent corroboration.
'''


def render_index(reviewers: list[dict], review_map: dict[str, list[dict]]) -> str:
    rows = []
    for reviewer in sorted(reviewers, key=lambda item: reviewer_public_name(item).casefold()):
        reviews = review_map.get(reviewer["reviewer_id"], [])
        if not reviews:
            continue
        name = reviewer_public_name(reviewer)
        rows.append(f"- [{name}](/contributors/{reviewer['slug']}/) — {len(reviews)} accepted independent review{'s' if len(reviews) != 1 else ''}")
    return f'''# Community contributors

These profiles preserve the public contribution history of reviewers who chose a persistent identity. Anonymous reviews remain valid evidence but do not create a public contributor profile.

{chr(10).join(rows) if rows else 'No persistent contributor profiles have accepted reviews yet.'}

Contributor history is provenance, not a popularity score. Individual claims still require evidence and corroboration.

[Submit an independent hands-on review](/docs/COMMUNITY_REVIEWS/)
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reviews", required=True, type=Path)
    parser.add_argument("--reviewers", required=True, type=Path)
    parser.add_argument("--devices", required=True, type=Path)
    parser.add_argument("--summary-output", required=True, type=Path)
    parser.add_argument("--profile-root", required=True, type=Path)
    parser.add_argument("--index-output", required=True, type=Path)
    args = parser.parse_args()

    review_doc = load(args.reviews)
    reviewer_doc = load(args.reviewers)
    device_doc = load(args.devices)

    require(review_doc.get("schema_version") == 1, "community reviews: unsupported schema_version")
    require(reviewer_doc.get("schema_version") == 1, "community reviewers: unsupported schema_version")
    require(tuple(review_doc.get("report_card_dimensions", [])) == DIMENSIONS, "community reviews: report-card dimensions drifted from canonical six")

    device_list = device_doc.get("records", [])
    devices = {str(item.get("id")): item for item in device_list}
    require(len(devices) == len(device_list), "community reviews: duplicate canonical model ID in device dataset")

    reviewers = reviewer_doc.get("reviewers", [])
    reviewer_by_id: dict[str, dict] = {}
    reviewer_slugs: set[str] = set()
    for reviewer in reviewers:
        reviewer_id = str(reviewer.get("reviewer_id", ""))
        slug = str(reviewer.get("slug", ""))
        require(REVIEWER_ID.fullmatch(reviewer_id) is not None, f"community reviewers: invalid reviewer_id {reviewer_id!r}")
        require(reviewer_id not in reviewer_by_id, f"community reviewers: duplicate reviewer_id {reviewer_id}")
        require(SLUG.fullmatch(slug) is not None, f"community reviewers: invalid slug {slug!r}")
        require(slug not in reviewer_slugs, f"community reviewers: duplicate slug {slug}")
        require(reviewer.get("attribution_mode") in {"pseudonym", "identified"}, f"community reviewers: persistent reviewer {reviewer_id} must be pseudonym or identified")
        require(bool(str(reviewer.get("public_name") or "").strip()), f"community reviewers: {reviewer_id} needs public_name")
        reviewer_by_id[reviewer_id] = reviewer
        reviewer_slugs.add(slug)

    reviews = review_doc.get("reviews", [])
    seen_reviews: set[str] = set()
    accepted: list[dict] = []
    reviewer_reviews: dict[str, list[dict]] = defaultdict(list)
    model_reviews: dict[str, list[dict]] = defaultdict(list)

    for review in reviews:
        review_id = str(review.get("review_id", ""))
        model_id = str(review.get("model_id", ""))
        status = review.get("status")
        reviewer_id = review.get("reviewer_id")
        attribution = review.get("public_attribution") or {}
        ratings = review.get("ratings") or {}

        require(REVIEW_ID.fullmatch(review_id) is not None, f"community reviews: invalid review_id {review_id!r}")
        require(review_id not in seen_reviews, f"community reviews: duplicate review_id {review_id}")
        seen_reviews.add(review_id)
        require(MODEL_ID.fullmatch(model_id) is not None and model_id in devices, f"community reviews: {review_id} references unknown model {model_id}")
        require(status in {"accepted", "withdrawn", "superseded"}, f"community reviews: {review_id} has invalid status")
        require(set(ratings) == set(DIMENSIONS), f"community reviews: {review_id} must carry exactly the canonical six rating fields")
        for dimension, value in ratings.items():
            require(value is None or (isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 10), f"community reviews: {review_id} {dimension} must be null or integer 0-10")

        if reviewer_id is not None:
            require(reviewer_id in reviewer_by_id, f"community reviews: {review_id} references unknown reviewer {reviewer_id}")
            require(attribution.get("mode") in {"pseudonym", "identified"}, f"community reviews: {review_id} persistent contributor cannot be anonymous")
        else:
            require(attribution.get("mode") == "anonymous", f"community reviews: {review_id} without reviewer_id must be anonymous")

        if status != "accepted":
            continue
        accepted.append(review)
        model_reviews[model_id].append(review)
        if reviewer_id is not None:
            reviewer_reviews[str(reviewer_id)].append(review)

    model_summary: dict[str, dict] = {}
    for model_id, items in sorted(model_reviews.items()):
        rating_values = {dimension: [] for dimension in DIMENSIONS}
        for review in items:
            for dimension in DIMENSIONS:
                value = review["ratings"].get(dimension)
                if isinstance(value, int) and not isinstance(value, bool):
                    rating_values[dimension].append(value)
        model_summary[model_id] = {
            "accepted_review_count": len(items),
            "persistent_reviewer_count": sum(review.get("reviewer_id") is not None for review in items),
            "anonymous_review_count": sum(review.get("reviewer_id") is None for review in items),
            "ownership_evidence_count": sum(review.get("ownership_evidence") in {"supplied_private", "supplied_public"} for review in items),
            "ratings": {dimension: score_summary(values) for dimension, values in rating_values.items()},
            "reviews": [
                {
                    "review_id": review["review_id"],
                    "reviewer_id": review.get("reviewer_id"),
                    "display_name": (
                        reviewer_public_name(reviewer_by_id[str(review["reviewer_id"])])
                        if review.get("reviewer_id") is not None
                        else "Anonymous contributor"
                    ),
                    "contributor_url": (
                        f"/contributors/{reviewer_by_id[str(review['reviewer_id'])]['slug']}/"
                        if review.get("reviewer_id") is not None
                        else None
                    ),
                    "accepted_at": review.get("accepted_at"),
                    "ownership_basis": review.get("ownership_basis"),
                    "ownership_evidence": review.get("ownership_evidence"),
                    "ratings": review.get("ratings"),
                    "source_issue": review.get("source_issue"),
                }
                for review in sorted(items, key=lambda item: (item.get("accepted_at") or "", item["review_id"]), reverse=True)
            ],
        }

    summary = {
        "schema_version": 1,
        "evidence_class": "independent_hands_on",
        "accepted_review_count": len(accepted),
        "persistent_reviewer_count": len([reviewer_id for reviewer_id, items in reviewer_reviews.items() if items]),
        "model_count": len(model_summary),
        "report_card_dimensions": list(DIMENSIONS),
        "models": model_summary,
    }
    args.summary_output.parent.mkdir(parents=True, exist_ok=True)
    args.summary_output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    args.profile_root.mkdir(parents=True, exist_ok=True)
    for reviewer in reviewers:
        items = reviewer_reviews.get(reviewer["reviewer_id"], [])
        if not items:
            continue
        path = args.profile_root / reviewer["slug"] / "index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_profile(reviewer, items, devices), encoding="utf-8")

    args.index_output.parent.mkdir(parents=True, exist_ok=True)
    args.index_output.write_text(render_index(reviewers, reviewer_reviews), encoding="utf-8")
    print(f"Community review evidence verified: {len(accepted)} accepted reviews, {len(model_summary)} models")


if __name__ == "__main__":
    main()
