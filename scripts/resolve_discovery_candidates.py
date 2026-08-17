#!/usr/bin/env python3
"""Resolve noisy discovery URLs without inventing canonical models."""
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

ACCESSORY_TERMS = ("accessories", "charging cable", "eyeglass case", "power adapter", "replacement lenses", "rx adapter", "merchandise", "charger")
SOURCE_TERMS = ("compare smart glasses", "contact support", "continue shopping", "developers", "request sdk", "remote support", "sales", "teleprompt", "transcribe", "translate", "talk to our oem", "smart eyewear", "in development", "collection", "bundles", "support", "health safety", "fashion week")
OPEN_PROJECT_HOSTS = ("github.com/mentra-community/opensourcesmartglasses", "teamopensmartglasses.com", "github.com/basedhardware/openglass", "seeedstudio.com/blog/2024/05/23/openglass")
NOISE_HOSTS = {
    "softonic.com", "rapidtables.com", "support.microsoft.com", "deepl.com", "thefreedictionary.com", "wikipedia.org",
    "developer.mozilla.org", "merriam-webster.com", "dictionary.com", "displaysettings.org", "cambridge.org", "webcam.org",
    "translate.google.com", "bing.com", "play.google.com", "reverso.net", "translate.google.us", "webcammictest.com",
    "apps.microsoft.com", "dell.com", "apps.apple.com", "en.m.wikipedia.org", "deepai.org", "ai.google",
    "copilot.microsoft.com", "openai.com", "z.ai", "gemini.google.com", "smart.com", "indeed.com", "smarttech.com",
    "corporatefinanceinstitute.com", "mindtools.com", "snhu.edu", "arbookfind.com", "renaissance.com", "arhelp.renaissance.com",
    "guns.com", "nyc.gov", "microsoft.com", "projectplusgame.com", "comptia.org", "pmi.org", "projectmanager.com",
    "thoughtco.com", "youtube.com", "vimeo.com", "genius.com", "periodic-table.rsc.org", "britannica.com", "thomasnet.com",
}
NOISE_TITLE_TERMS = ("best smart glasses", "best ar glasses", "ranking the best", "smart goals", "smart goal", "smart definition", "smart fortwo", "accelerated reader", "arkansas", "what is ar", "what is augmented reality", "project definition", "titanium", "camera online", "webcam test", "display definition")
GENERIC_MAKER_TOKENS = {"shared", "ecosystem", "oem", "glasses", "innovation", "current", "smart"}


def norm_text(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def norm_url(value: str) -> str:
    p = urllib.parse.urlsplit(value.strip())
    host = p.netloc.lower().removeprefix("www.")
    return urllib.parse.urlunsplit((p.scheme.lower(), host, p.path.rstrip("/"), "", ""))


def host_of(value: str) -> str:
    return urllib.parse.urlsplit(norm_url(value)).netloc


def host_path(value: str) -> str:
    p = urllib.parse.urlsplit(norm_url(value))
    return f"{p.netloc}{p.path}".lower()


def phrase_present(phrase: str, hay: str) -> bool:
    phrase = norm_text(phrase)
    return bool(phrase and re.search(rf"(?:^| ){re.escape(phrase)}(?: |$)", hay))


def maker_present(maker: str, hay: str) -> bool:
    full = norm_text(maker)
    if phrase_present(full, hay):
        return True
    tokens = [t for t in full.split() if len(t) >= 3 and t not in GENERIC_MAKER_TOKENS]
    return any(phrase_present(token, hay) for token in tokens)


def identity_haystack(item: dict) -> str:
    return norm_text(" ".join((str(item.get("title", "")), str(item.get("summary", "")), urllib.parse.unquote(str(item.get("url", ""))))))


def load_canonical(path: Path) -> tuple[dict[str, str], list[dict]]:
    by_url: dict[str, str] = {}
    records: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = MODEL_ROW.match(line)
        if not match:
            continue
        model_id, maker, model = (x.strip() for x in match.groups())
        records.append({"id": model_id, "maker": maker, "model": model})
        for raw in URL.findall(line):
            by_url[norm_url(raw)] = model_id
    return by_url, records


def load_registry(path: Path) -> tuple[dict[str, list[dict]], list[dict]]:
    records = json.loads(path.read_text(encoding="utf-8")).get("candidates", [])
    by_url: dict[str, list[dict]] = {}
    for record in records:
        for source in record.get("sources", []):
            if source.get("url"):
                by_url.setdefault(norm_url(source["url"]), []).append(record)
    return by_url, records


def registry_matches(item: dict, records: list[dict]) -> list[dict]:
    hay = identity_haystack(item)
    page_host = host_of(str(item.get("url", "")))
    matches = []
    for record in records:
        model = norm_text(record.get("model"))
        aliases = [norm_text(a) for a in record.get("aliases", [])]
        source_hosts = {host_of(s["url"]) for s in record.get("sources", []) if s.get("url")}
        name_hit = phrase_present(model, hay) or any(len(a) >= 3 and phrase_present(a, hay) for a in aliases)
        if not name_hit:
            continue
        # Registry entries may be seller/OEM names, so source-domain context is
        # sufficient when maker text is absent from a product link title.
        if maker_present(record.get("maker", ""), hay) or page_host in source_hosts or len(model) >= 7:
            matches.append(record)
    if len(matches) > 1:
        longest = max(len(norm_text(r.get("model"))) for r in matches)
        matches = [r for r in matches if len(norm_text(r.get("model"))) == longest]
    return matches


def canonical_matches(item: dict, records: list[dict]) -> list[dict]:
    hay = identity_haystack(item)
    matches = []
    for record in records:
        # Canonical fuzzy matching is deliberately stricter than registry
        # matching: both maker and model must be present. This prevents generic
        # names such as DAQRI "Smart Glasses", Nreal "Light", or Brilliant
        # "Frame" from swallowing unrelated search results.
        if phrase_present(record["model"], hay) and maker_present(record["maker"], hay):
            matches.append(record)
    if len(matches) > 1:
        longest = max(len(norm_text(r["model"])) for r in matches)
        matches = [r for r in matches if len(norm_text(r["model"])) == longest]
    return matches


def registry_disposition(record: dict) -> tuple[str, str | None, str]:
    if record.get("canonical_id"):
        return "duplicate-canonical", record["canonical_id"], f"Identity matches resolved candidate {record.get('candidate_id')}"
    if record.get("status") == "duplicate-rebrand":
        return "alias-rebrand", record.get("candidate_id"), "Registry already resolved this presentation as a rebrand/duplicate"
    if record.get("status") == "in-scope":
        return "registry-sibling", record.get("candidate_id"), "Distinct identity retained upstream of canonical admission"
    return "source-page-no-distinct-model", record.get("candidate_id"), "Registry record does not establish a canonical admission"


def classify(item: dict, canonical_urls: dict[str, str], canonical: list[dict], registry_urls: dict[str, list[dict]], registry: list[dict]) -> tuple[str, str | None, str]:
    url = norm_url(str(item.get("url", "")))
    title = str(item.get("title", ""))
    low = title.lower()
    host = host_of(url)
    hp = host_path(url)

    if any(term in low for term in ACCESSORY_TERMS):
        return "non-product-accessory", None, "Accessory or merchandise, not a smart-glasses model"
    if any(fragment in hp for fragment in OPEN_PROJECT_HOSTS):
        return "non-canonical-open-project", None, "Open project/reference implementation without a distinct purchasable model identity"
    if host in NOISE_HOSTS or any(term in low for term in NOISE_TITLE_TERMS):
        return "non-product-noise", None, "Search-query collision, general reference, media result, or unrelated page"

    reg = registry_matches(item, registry)
    if len(reg) == 1:
        return registry_disposition(reg[0])

    can = canonical_matches(item, canonical)
    if len(can) == 1:
        record = can[0]
        return "duplicate-canonical", record["id"], f"Maker/model identity matches canonical {record['maker']} {record['model']}"

    if url in canonical_urls:
        return "duplicate-canonical", canonical_urls[url], "URL is already evidence for a canonical GLS record"

    exact_registry = registry_urls.get(url, [])
    if len(exact_registry) == 1:
        return registry_disposition(exact_registry[0])

    if item.get("scope_lane") != "core_glasses":
        return "research-radar-not-model", None, "Relevant research radar item, not a smart-glasses product identity"
    if "manufacturer_catalog" in str(item.get("discovery_channel", "")):
        return "source-page-no-distinct-model", None, "Relevant manufacturer page, but this URL does not establish a distinct unresolved model identity"
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
    canonical_urls, canonical = load_canonical(ROOT / "models" / "THE_LIST.md")
    registry_urls, registry = load_registry(ROOT / "data" / "model-candidates.json")

    resolved = []
    for item in payload.get("candidates", []):
        disposition, target, reason = classify(item, canonical_urls, canonical, registry_urls, registry)
        resolved.append({"id": item.get("id"), "title": item.get("title"), "url": item.get("url"), "discovery_channel": item.get("discovery_channel"), "scope_lane": item.get("scope_lane"), "disposition": disposition, "target": target, "reason": reason})

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
    (outdir / f"{stem}.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [f"# Discovery resolution — {stem}", "", f"Resolved **{len(resolved)}** retained discovery URLs.", "", "No discovery lead is promoted automatically. Canonical admission remains an evidence-backed separate action.", "", "## Dispositions", ""]
    lines += [f"- {name}: {count}" for name, count in sorted(counts.items())]
    lines += ["", "## Identity findings", "", "- **Halliday G2:** distinct pre-release sibling/successor to GLS-0049; registry-only and no inherited scores.", "- **Even R1:** adjacent smart ring for Even G2; not eyewear and not counted as a glasses model.", "", "## Per-lead resolution", "", "| Lead | Disposition | Target |", "|---|---|---|"]
    for row in resolved:
        safe = str(row["title"] or row["url"]).replace("|", "\\|")
        lines.append(f"| [{safe}]({row['url']}) | {row['disposition']} | {row['target'] or '—'} |")
    (outdir / f"{stem}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Resolved {len(resolved)} discovery URLs across {dict(sorted(counts.items()))}; canonical admissions=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
