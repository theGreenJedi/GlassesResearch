"""Shared GlassesResearch knowledge-flow classification and routing.

Discovery stays deliberately broad. This module decides what a candidate is,
how it relates to smart glasses, and where it should go next. Classification is
descriptive; it never authorizes publication.
"""
from __future__ import annotations

import re
from collections.abc import Iterable

RELATIONSHIPS = ("direct", "enabling", "adjacent", "speculative", "irrelevant")
CONTENT_TYPES = (
    "model", "review", "video", "news", "research", "tool", "sdk", "hack",
    "optics", "policy", "retail", "teardown", "community", "rumor",
)

DEFAULT_DIRECT_TERMS = (
    "smart glasses", "smartglasses", "ai glasses", "ar glasses",
    "augmented reality glasses", "mixed reality glasses", "smart eyewear",
    "ai eyewear", "ar eyewear", "camera glasses", "audio glasses",
    "display glasses", "hud glasses", "heads-up display glasses",
    "spectacles",
)

TYPE_TERMS = {
    "model": (
        "launch", "launched", "released", "release", "announced", "announcement",
        "preorder", "pre-order", "shipping", "available", "availability",
        "discontinued", "recall", "new model", "new glasses",
    ),
    "review": ("review", "hands-on", "hands on", "tested", "long-term", "long term"),
    "video": ("youtube", "video", "watch", "demo video"),
    "research": ("research", "study", "paper", "journal", "arxiv", "conference", "prototype"),
    "tool": ("tool", "app", "platform", "framework", "library", "repository", "github", "open source"),
    "sdk": ("sdk", "api", "developer", "developers", "devkit", "dev kit"),
    "hack": (
        "hack", "hacking", "reverse engineer", "reverse engineering", "firmware",
        "ble", "bluetooth low energy", "root", "jailbreak",
    ),
    "optics": (
        "waveguide", "microled", "micro-oled", "micro oled", "lens", "lenses",
        "optics", "optical", "prescription", "retinal", "holographic",
    ),
    "policy": (
        "privacy", "lawsuit", "complaint", "regulation", "regulator", "ban",
        "banned", "policy", "legal", "court", "surveillance",
    ),
    "retail": (
        "amazon", "walmart", "best buy", "retail", "retailer", "listing",
        "sale", "price", "aliexpress", "alibaba",
    ),
    "teardown": ("teardown", "tear down", "disassembly", "inside", "repair", "ifixit"),
    "community": ("reddit", "discord", "forum", "community", "owner report", "user report"),
    "rumor": (
        "rumor", "rumour", "leak", "leaked", "reportedly", "expected to",
        "may launch", "could launch", "patent", "concept",
    ),
}

SPECULATIVE_TERMS = TYPE_TERMS["rumor"]
ENABLING_TERMS = (
    "waveguide", "microled", "micro-oled", "micro oled", "optics", "optical",
    "prescription", "lens", "lenses", "retinal", "holographic", "camera module",
    "snapdragon ar1", "display engine", "eye tracking", "gaze tracking",
    "near-eye display", "near eye display",
)
ADJACENT_TERMS = (
    "wearable hci", "wearable human computer interface", "human-computer interface",
    "human computer interface", "brain-computer", "brain computer", "bci", "neural",
    "emg", "semg", "gesture control", "wearable interface", "hearable", "haptic",
    "biosensor", "spatial computing", "ambient computing", "android xr", "openxr",
)


def term_match(text: str, term: str) -> bool:
    """Match a token/phrase, never an arbitrary substring.

    Short signals such as AI, BLE, API and SDK must stand alone. In particular,
    `ble` must never match `eligible`.
    """
    text = text.lower()
    term = term.lower().strip()
    if not term:
        return False
    pattern = r"(?<![a-z0-9])" + re.escape(term).replace(r"\ ", r"\s+") + r"(?![a-z0-9])"
    return re.search(pattern, text) is not None


def term_hits(text: str, terms: Iterable[str]) -> list[str]:
    return sorted({term for term in terms if term_match(text, term)}, key=str.lower)


def classify_relationship(
    *,
    title: str,
    summary: str = "",
    url: str = "",
    source_lane: str = "",
    extra_direct_terms: Iterable[str] = (),
    trusted_direct_source: bool = False,
) -> tuple[str, str]:
    hay = f"{title} {summary} {url}"
    direct_terms = tuple(dict.fromkeys((*DEFAULT_DIRECT_TERMS, *tuple(extra_direct_terms))))
    direct_hits = term_hits(hay, direct_terms)
    speculative_hits = term_hits(hay, SPECULATIVE_TERMS)
    enabling_hits = term_hits(hay, ENABLING_TERMS)
    adjacent_hits = term_hits(hay, ADJACENT_TERMS)

    if speculative_hits and (direct_hits or trusted_direct_source or source_lane == "core_glasses"):
        return "speculative", f"future/rumor signals: {', '.join(speculative_hits[:4])}"

    if trusted_direct_source:
        return "direct", "known smart-glasses source"

    if direct_hits:
        return "direct", f"explicit smart-glasses/eyewear signals: {', '.join(direct_hits[:4])}"

    if enabling_hits and source_lane in {"core_glasses", "research_radar", "research"}:
        return "enabling", f"enabling technology signals: {', '.join(enabling_hits[:4])}"

    if adjacent_hits or source_lane == "adjacent_hci":
        return "adjacent", "neighboring wearable/HCI development without a concrete glasses claim"

    return "irrelevant", "no concrete smart-glasses, enabling-technology, or adjacent-HCI relationship detected"


def classify_types(
    *,
    title: str,
    summary: str = "",
    url: str = "",
    relationship: str,
    channel_hint: str = "",
) -> list[str]:
    hay = f"{title} {summary} {url}"
    found = [kind for kind, terms in TYPE_TERMS.items() if term_hits(hay, terms)]

    hint_types = {
        "retail": ("retail",),
        "developer": ("tool", "sdk"),
        "research": ("research",),
        "community": ("community",),
        "manufacturer_catalog": ("model",),
    }
    for kind in hint_types.get(channel_hint, ()):
        if kind not in found:
            found.append(kind)

    if relationship == "speculative" and "rumor" not in found:
        found.append("rumor")
    if not found:
        found.append("news")
    return [kind for kind in CONTENT_TYPES if kind in found]


def route_candidate(relationship: str, content_types: list[str]) -> list[str]:
    if relationship == "irrelevant":
        return ["reject_noise"]

    routes: list[str] = ["research_news_review"]
    if relationship == "speculative" or "rumor" in content_types:
        routes.append("watching")
    if "model" in content_types:
        routes.append("model_catalog_review")
    if any(t in content_types for t in ("review", "video", "teardown")):
        routes.append("report_card_evidence")
    if any(t in content_types for t in ("tool", "sdk", "hack")):
        routes.append("development_hacking")
    if "optics" in content_types or relationship == "enabling":
        routes.append("research_optics")
    if "policy" in content_types:
        routes.append("policy_privacy")
    if "retail" in content_types:
        routes.append("retail_rebrand_review")
    if "research" in content_types:
        routes.append("deep_research")
    if "community" in content_types:
        routes.append("community_evidence_review")
    if relationship == "adjacent":
        routes.append("adjacent_radar")
    return list(dict.fromkeys(routes))


def triage_priority(materiality_score: int, relationship: str, content_types: list[str]) -> str:
    weight = materiality_score
    weight += {"direct": 4, "enabling": 2, "adjacent": 0, "speculative": 1, "irrelevant": -10}[relationship]
    if any(t in content_types for t in ("model", "sdk", "hack", "teardown", "policy")):
        weight += 1
    if weight >= 9:
        return "high"
    if weight >= 5:
        return "normal"
    return "low"


def enrich_candidate(
    candidate: dict,
    *,
    source_lane: str = "",
    extra_direct_terms: Iterable[str] = (),
    trusted_direct_source: bool = False,
    channel_hint: str = "",
) -> dict:
    relationship, reason = classify_relationship(
        title=candidate.get("title", ""),
        summary=candidate.get("summary", ""),
        url=candidate.get("url", ""),
        source_lane=source_lane,
        extra_direct_terms=extra_direct_terms,
        trusted_direct_source=trusted_direct_source,
    )
    content_types = classify_types(
        title=candidate.get("title", ""),
        summary=candidate.get("summary", ""),
        url=candidate.get("url", ""),
        relationship=relationship,
        channel_hint=channel_hint,
    )
    candidate.update(
        {
            "relationship": relationship,
            "content_types": content_types,
            "primary_type": content_types[0],
            "routing_targets": route_candidate(relationship, content_types),
            "triage_priority": triage_priority(
                int(candidate.get("materiality_score", 0) or 0), relationship, content_types
            ),
            "publication_eligible": relationship in {"direct", "enabling"},
            "publication_gate_reason": reason,
            "disposition": candidate.get("disposition", "collected"),
            "site_action": candidate.get("site_action", "none_pending_editorial_review"),
        }
    )
    return candidate
