#!/usr/bin/env python3
"""Resolve high-recall discovery URLs without promoting search noise into models.

The collector is intentionally noisy. This resolver turns every retained URL into
an explicit disposition by comparing it with the canonical ledger, the candidate
registry, and conservative non-product/source rules. It never creates a GLS ID.
Canonical admission remains a separate evidence-backed editorial action.
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.parse
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL_ROW = re.compile(r"^\|\s*(GLS-\d{4})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", re.M)
URL = re.compile(r"https?://[^)\s|]+")

ACCESSORY_TERMS = (
    "accessories", "charging cable", "eyeglass case", "power adapter",
    "replacement lenses", "rx adapter", "merchandise", "charger",
)
SOURCE_TERMS = (
    "compare smart glasses", "contact support", "continue shopping", "cookie",
    "developers", "request sdk", "remote support", "sales", "teleprompt",
    "transcribe", "translate", "talk to our oem", "smart eyewear", "in development",
    "collection", "bundles", "support", "health safety", "fashion week",
)
OPEN_PROJECT_HOSTS = {
    "github.com/mentra-community/opensourcesmartglasses",
    "teamopensmartglasses.com",
    "github.com/basedhardware/openglass",
    "seeedstudio.com/blog/2024/05/23/openglass",
}
NOISE_HOSTS = {
    "softonic.com", "rapidtables.com", "support.microsoft.com", "deepl.com",
    "thefreedictionary.com", "wikipedia.org", "developer.mozilla.org",
    "merriam-webster.com", "dictionary.com", "displaysettings.org",
    "cambridge.org", "webcam.org", "translate.google.com", "bing.com",
    "play.google.com", "reverso.net", "translate.google.us", "webcammictest.com",
    "apps.microsoft.com", "dell.com", "apps.apple.com", "en.m.wikipedia.org",
    "deepai.org", "ai.google", "copilot.microsoft.com", "openai.com", "z.ai",
    "gemini.google.com", "smart.com", "indeed.com", "smarttech.com",
    "corporatefinanceinstitute.com", "mindtools.com", "snhu.edu", "arbookfind.com",
    "renaissance.com", "arhelp.renaissance.com", "guns.com", "nyc.gov",
    "microsoft.com", "projectplusgame.com", "comptia.org", "pmi.org",
    "projectmanager.com", "thoughtco.com", "youtube.com", "vimeo.com",
    "genius.com", "periodic-table.rsc.org", "britannica.com", "thomasnet.com",
}
NOISE_TITLE_TERMS = (
    "best smart glasses", "best ar glasses", "ranking the best", "smart goals",
    "smart goal", "smart definition", "smart fortwo", "accelerated reader",
    "arkansas", "what is ar", "what is augmented reality", "project definition",
    "titanium", "camera online", "webcam test", "display definition",
)


def norm_url(value: str) -> str:
    p = urllib.parse.urlsplit(value.strip())
    host = p.netloc.lower().removeprefix("www.")
    path = p.path.rstrip("/")
    return urllib.parse.urlunsplit((p.scheme.lower(), host, path, "", ""))


def host_path(value: str) -> str:
    p = urllib.parse.urlsplit(norm_url(value))
    return f"{p.netloc}{p.path}".lower()


def canonical_sources(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    result: dict[str, str] = {}
    for line in text.splitlines():
        match = MODEL_ROW.match(line)
        if not match:
            continue
        model_id = match.group(1)
        for raw in URL.findall(line):
            result[norm_url(raw)] = model_id
    return result


def candidate_sources(path: Path) -> dict[str, dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    result: dict[str, dict] = {}
    for record in payload.get("candidates", []):
        for source in record.get("sources", []):
            url = source.get("url")
            if url:
                result[norm_url(url)] = record
    return result


def classify(item: dict, canonical: dict[str, str], registry: dict[str, dict]) -> tuple[str, str | None, str]:
    url = norm_url(item.get("url", ""))
    title = str(item.get("title", ""))
    low = title.lower()
    hp = host_path(url)
    host = urllib.parse.urlsplit(url).netloc

    if url in canonical:
        return "duplicate-canonical", canonical[url], "URL is already evidence for a canonical GLS record"

    reg = registry.get(url)
    if reg:
        status = reg.get("status")
        if reg.get("canonical_id"):
            return "duplicate-canonical", reg["canonical_id"], f"Already resolved by candidate registry {reg.get('candidate_id')}"
        if status == "duplicate-rebrand":
            return "alias-rebrand", reg.get("candidate_id"), "Registry already resolved this presentation as a rebrand/duplicate"
        if status == "in-scope":
            return "registry-sibling", reg.get("candidate_id"), "Distinct identity retained upstream of canonical admission"

    if any(term in low for term in ACCESSORY_TERMS):
        return "non-product-accessory", None, "Accessory or merchandise, not a smart-glasses model"

    if any(fragment in hp for fragment in OPEN_PROJECT_HOSTS):
        return "non-canonical-open-project", None, "Open project/reference implementation without a distinct purchasable model identity"

    if host in NOISE_HOSTS or any(term in low for term in NOISE_TITLE_TERMS):
        return "non-product-noise", None, "Search-query collision, general reference, media result, or unrelated page"

    channel = str(item.get("discovery_channel", ""))
    if "manufacturer_catalog" in channel:
        return "source-page-no-distinct-model", None, "Relevant manufacturer page, but this URL does not establish a new model identity"

    if item.get("scope_lane") != "core_glasses":
        return "research-radar-not-model", None, "Relevant research radar item, not a smart-glasses product identity"

    if any(term in low for term in SOURCE_TERMS):
        return "source-page-no-distinct-model", None, "Useful source or use-case page, not a separate model"

    return "source-page-no-distinct-model", None, "Potentially useful discovery source; no distinct new model identity established by this lead"


def latest_intake(directory: Path) -> Path:
    paths = sorted(p for p in directory.glob("*.json") if not p.name.endswith(".resolved.json"))
    if not paths:
        raise SystemExit("No discovery intake JSON found")
    return paths[-1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input")
    ap.add_argument("--output-dir", default=str(ROOT / "research" / "discovery-resolutions"))
    args = ap.parse_args()

    source = Path(args.input) if args.input else latest_intake(ROOT / "research" / "discovery-candidates")
    payload = json.loads(source.read_text(encoding="utf-8"))
    canonical = canonical_sources(ROOT / "models" / "THE_LIST.md")
    registry = candidate_sources(ROOT / "data" / "model-candidates.json")

    resolved = []
    for item in payload.get("candidates", []):
        disposition, target, reason = classify(item, canonical, registry)
        resolved.append({
            "id": item.get("id"),
            "title": item.get("title"),
            "url": item.get("url"),
            "discovery_channel": item.get("discovery_channel"),
            "scope_lane": item.get("scope_lane"),
            "disposition": disposition,
            "target": target,
            "reason": reason,
        })

    counts = Counter(row["disposition"] for row in resolved)
    outdir = Path(args.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    stem = source.stem
    result = {
        "schema_version": 1,
        "source": source.as_posix(),
        "candidate_count": len(resolved),
        "counts": dict(sorted(counts.items())),
        "canonical_admissions": [],
        "policy": "resolution never creates a GLS ID; canonical admission requires separate verified evidence",
        "observations": [
            "Halliday G2 is retained as HALLIDAY-G2, a distinct pre-release sibling/successor to GLS-0049; no score inheritance.",
            "Even R1 surfaced in Even Realities manufacturer text but is a smart ring that interacts with Even G2, not eyewear.",
        ],
        "resolutions": resolved,
    }
    json_path = outdir / f"{stem}.json"
    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        f"# Discovery resolution — {stem}", "",
        f"Resolved **{len(resolved)}** retained discovery URLs.", "",
        "No discovery lead is promoted automatically. Canonical admission remains an evidence-backed separate action.", "",
        "## Dispositions", "",
    ]
    lines += [f"- {name}: {count}" for name, count in sorted(counts.items())]
    lines += ["", "## Identity findings", "",
              "- **Halliday G2:** distinct pre-release sibling/successor to GLS-0049; registry-only and no inherited scores.",
              "- **Even R1:** adjacent smart ring for Even G2; not eyewear and not counted as a glasses model.",
              "", "## Per-lead resolution", "",
              "| Lead | Disposition | Target |", "|---|---|---|"]
    for row in resolved:
        safe = str(row["title"] or row["url"]).replace("|", "\\|")
        lines.append(f"| [{safe}]({row['url']}) | {row['disposition']} | {row['target'] or '—'} |")
    (outdir / f"{stem}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Resolved {len(resolved)} discovery URLs across {dict(sorted(counts.items()))}; canonical admissions=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
