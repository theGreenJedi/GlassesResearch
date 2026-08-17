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


def norm_text(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def norm_url(value: str) -> str:
    p = urllib.parse.urlsplit(value.strip())
    host = p.netloc.lower().removeprefix("www.")
    path = p.path.rstrip("/")
    return urllib.parse.urlunsplit((p.scheme.lower(), host, path, "", ""))


def host_path(value: str) -> str:
    p = urllib.parse.urlsplit(norm_url(value))
    return f"{p.netloc}{p.path}".lower()


def host_of(value: str) -> str:
    return urllib.parse.urlsplit(norm_url(value)).netloc


def canonical_records(path: Path) -> tuple[dict[str, str], list[dict]]:
    text = path.read_text(encoding="utf-8")
    sources: dict[str, str] = {}
    records: list[dict] = []
    for line in text.splitlines():
        match = MODEL_ROW.match(line)
        if not match:
            continue
        model_id, maker, model = (part.strip() for part in match.groups())
        record = {"id": model_id, "maker": maker, "model": model}
        records.append(record)
        for raw in URL.findall(line):
            sources[norm_url(raw)] = model_id
    return sources, records


def candidate_records(path: Path) -> tuple[dict[str, list[dict]], list[dict]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("candidates", [])
    sources: dict[str, list[dict]] = {}
    for record in records:
        for source in record.get("sources", []):
            url = source.get("url")
            if url:
                sources.setdefault(norm_url(url), []).append(record)
    return sources, records


def identity_haystack(item: dict) -> str:
    return norm_text(" ".join([
        str(item.get("title", "")),
        str(item.get("summary", "")),
        urllib.parse.unquote(str(item.get("url", ""))),
    ]))


def phrase_present(phrase: str, hay: str) -> bool:
    phrase = norm_text(phrase)
    if not phrase:
        return False
    return re.search(rf"(?:^| )({re.escape(phrase)})(?: |$)", hay) is not None


def identity_match(maker: str, model: str, aliases: list[str], hay: str, page_host: str, source_hosts: set[str]) -> bool:
    model_n = norm_text(model)
    maker_n = norm_text(maker)
    alias_hits = [norm_text(a) for a in aliases if len(norm_text(a)) >= 3 and phrase_present(a, hay)]
    if alias_hits:
        return True
    if not model_n or not phrase_present(model_n, hay):
        return False
    # Short/generic model names such as Air, GO, One, Frame, or G2 need either
    # maker context or a page on a source domain already tied to that identity.
    distinctive = len(model_n) >= 5 or any(ch.isdigit() for ch in model_n) and len(model_n) >= 3
    return distinctive or phrase_present(maker_n, hay) or page_host in source_hosts


def registry_identity_matches(item: dict, records: list[dict]) -> list[dict]:
    hay = identity_haystack(item)
    page_host = host_of(str(item.get("url", "")))
    matches = []
    for record in records:
        source_hosts = {host_of(s.get("url", "")) for s in record.get("sources", []) if s.get("url")}
        if identity_match(record.get("maker", ""), record.get("model", ""), record.get("aliases", []), hay, page_host, source_hosts):
            matches.append(record)
    # Prefer the longest model phrase so "Maverick AI" does not accidentally
    # capture "Maverick AI Pro" and vice versa.
    if len(matches) > 1:
        lengths = [len(norm_text(r.get("model", ""))) for r in matches]
        longest = max(lengths)
        exact_long = [r for r in matches if len(norm_text(r.get("model", ""))) == longest and phrase_present(r.get("model", ""), hay)]
        if exact_long:
            matches = exact_long
    return matches


def canonical_identity_matches(item: dict, records: list[dict]) -> list[dict]:
    hay = identity_haystack(item)
    matches = []
    for record in records:
        if identity_match(record["maker"], record["model"], [], hay, "", set()):
            matches.append(record)
    if len(matches) > 1:
        longest = max(len(norm_text(r["model"])) for r in matches)
        matches = [r for r in matches if len(norm_text(r["model"])) == longest]
    return matches


def classify(
    item: dict,
    canonical_sources: dict[str, str],
    canonical: list[dict],
    registry_sources: dict[str, list[dict]],
    registry: list[dict],
) -> tuple[str, str | None, str]:
    url = norm_url(item.get("url", ""))
    title = str(item.get("title", ""))
    low = title.lower()
    hp = host_path(url)
    host = host_of(url)

    # First resolve explicit registry identities from the page text. This is
    # necessary for shared family pages and for current URLs that differ from
    # the historical source URL stored in the canonical ledger.
    reg_matches = registry_identity_matches(item, registry)
    if len(reg_matches) == 1:
        reg = reg_matches[0]
        status = reg.get("status")
        if reg.get("canonical_id"):
            return "duplicate-canonical", reg["canonical_id"], f"Identity matches resolved candidate {reg.get('candidate_id')}"
        if status == "duplicate-rebrand":
            return "alias-rebrand", reg.get("candidate_id"), "Registry already resolved this presentation as a rebrand/duplicate"
        if status == "in-scope":
            return "registry-sibling", reg.get("candidate_id"), "Distinct identity retained upstream of canonical admission"

    canonical_matches = canonical_identity_matches(item, canonical)
    if len(canonical_matches) == 1:
        record = canonical_matches[0]
        return "duplicate-canonical", record["id"], f"Maker/model identity matches canonical {record['maker']} {record['model']}"

    if url in canonical_sources:
        return "duplicate-canonical", canonical_sources[url], "URL is already evidence for a canonical GLS record"

    exact_registry = registry_sources.get(url, [])
    if len(exact_registry) == 1:
        reg = exact_registry[0]
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
        return "source-page-no-distinct-model", None, "Relevant manufacturer page, but this URL does not establish a distinct unresolved model identity"

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
    canonical_sources, canonical = canonical_records(ROOT / "models" / "THE_LIST.md")
    registry_sources, registry = candidate_records(ROOT / "data" / "model-candidates.json")

    resolved = []
    for item in payload.get("candidates", []):
        disposition, target, reason = classify(item, canonical_sources, canonical, registry_sources, registry)
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
