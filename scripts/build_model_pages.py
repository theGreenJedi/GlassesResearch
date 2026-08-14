#!/usr/bin/env python3
"""Generate canonical model pages and search-intent guides from verified data."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADING = re.compile(r"^##\s+(GLS-\d{4})\s+—\s+.+?\s*$", re.MULTILINE)
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

GUIDES = [
    ("prescription-smart-glasses", "Best prescription-compatible smart glasses", [("prescription_support", "yes")], "Models with verified prescription support", "Prescription compatibility is model- and frame-specific. Confirm the supported prescription range and fitting route before buying."),
    ("smart-glasses-without-cameras", "Best smart glasses without cameras", [("camera", "no")], "Camera-free glasses for audio or display use", "A verified camera-free design reduces one privacy concern; microphones, accounts, apps, and cloud processing still need separate review."),
    ("smart-glasses-with-displays", "Best smart glasses with displays and HUDs", [("display", "yes")], "Verified display-equipped smart glasses", "Display presence does not establish resolution, field of view, outdoor visibility, or binocular operation. Follow each model's evidence record."),
    ("audio-smart-glasses", "Best audio smart glasses", [("speakers", "yes"), ("no_display", "yes")], "Display-free glasses with verified speakers", "This shortlist favors verified capability, not sound quality. Fit, leakage, microphone quality, and battery endurance require model-specific testing."),
    ("visual-ai-smart-glasses", "Best visual AI smart glasses", [("visual_ai", "yes")], "Glasses with verified visual-AI capability", "Visual AI usually depends on a camera, companion software, an account, and cloud services. Check the model page for what is verified and what remains unknown."),
    ("smart-glasses-for-developers", "Best smart glasses for developers", [("sdk_api", "yes")], "Models with a verified SDK or API", "An SDK can be restricted, discontinued, enterprise-only, or cloud-bound. Availability and license terms should be rechecked before committing a project."),
    ("open-source-smart-glasses", "Best open-source smart glasses", [("open_source", "yes")], "Models with verified open-source support", "Open source may cover only part of the stack. Hardware files, firmware, application code, and model weights are separate layers."),
    ("offline-smart-glasses", "Best smart glasses that work offline", [("offline_operation", "yes")], "Models with verified offline operation", "Offline operation means at least one useful capability is documented without a vendor cloud; it does not imply every feature works offline."),
    ("self-hosted-ai-smart-glasses", "Best self-hosted AI smart glasses", [("self_hostable", "yes")], "Models with verified self-hosting support", "Self-hosting can cover only part of a product's intelligence stack. Companion apps, accounts, firmware services, and other features may remain vendor-dependent."),
    ("smart-glasses-for-calls-and-music", "Best smart glasses for calls and music", [("phone_calls", "yes"), ("music", "yes")], "Glasses with both capabilities verified", "This is a capability shortlist, not an audio-quality ranking. Wind rejection, leakage, comfort, and call clarity still need hands-on comparison."),
    ("smart-glasses-with-video-recording", "Best camera glasses for video recording", [("video_recording", "yes")], "Models with verified video recording", "Recording resolution, clip limits, stabilization, indicator behavior, storage, and export workflow vary by model."),
    ("bluetooth-smart-glasses", "Best Bluetooth smart glasses", [("bluetooth", "yes")], "Models with verified Bluetooth support", "Bluetooth support alone does not prove standard audio profiles, multipoint pairing, BLE access, or compatibility with every phone."),
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def profiles() -> dict[str, str]:
    found: dict[str, str] = {}
    for path in sorted((ROOT / "models").glob("PROFILES*.md")):
        text = path.read_text(encoding="utf-8")
        matches = list(HEADING.finditer(text))
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            body = text[match.end():end].strip()
            paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
            prose = next((p for p in paragraphs if not p.startswith(("Source:", "Sources:"))), "")
            # Profile prose is relocated from models/ into models/catalog/.
            # Keep external citations, but avoid carrying source-relative links
            # into a different directory where they would resolve incorrectly.
            prose = LINK.sub(lambda m: m.group(0) if re.match(r"https?://", m.group(2)) else m.group(1), prose)
            found.setdefault(match.group(1), prose)
    return found


def md_value(value: object) -> str:
    if value is True:
        return "Yes"
    if value is False:
        return "No"
    return str(value)


def score_average(record: dict | None) -> float:
    if not record:
        return -1
    values = [float(v) for v in record["scores"].values() if isinstance(v, (int, float))]
    return sum(values) / len(values) if values else -1


def source_links(record: dict) -> str:
    external = [item for item in record["links"] if item["kind"] == "external"]
    return "\n".join(f"- [{item['label']}]({item['url']})" for item in external) or "- No external source recorded."


def model_page(record: dict, profile: str, comparison: dict | None, capability: dict, score: dict | None, labels: dict[str, str], score_labels: dict[str, str], related: list[dict]) -> str:
    title = f"{record['maker']} {record['model']} ({record['id']})"
    description = f"Verified specifications, capabilities, status, sources, and research links for {record['maker']} {record['model']} smart glasses."
    confirmed = [(labels.get(k, k.replace("_", " ").title()), v["provenance"]) for k, v in capability["capabilities"].items() if v["value"] == "yes"]
    negatives = [labels.get(k, k.replace("_", " ").title()) for k, v in capability["capabilities"].items() if v["value"] == "no"]
    unknown_count = sum(v["value"] == "unknown" for v in capability["capabilities"].values())
    facts = []
    if comparison:
        for key, fact in comparison["fields"].items():
            if key in {"manufacturer", "release_year", "status", "category", "last_reviewed", "research_notes"} or fact.get("evidence") == "unknown" or str(fact.get("value", "")).lower() == "unknown":
                continue
            facts.append((labels.get(key, key.replace("_", " ").title()), md_value(fact["value"]), fact["evidence"]))
    facts = facts[:16]
    public = record["public"]
    paths = [f"[Editorial profile]({public['profile']})"]
    if public.get("report_card"):
        paths.append(f"[Report Card]({public['report_card']})")
    if public.get("lineage"):
        paths.append(f"[Lineage research]({public['lineage']})")
    related_rows = "\n".join(f"- [{r['maker']} {r['model']}]({r['public']['model_page']}) — {r['state']}, {r['type']}" for r in related[:5])
    fact_rows = "\n".join(f"| {a} | {b} | {c} |" for a, b, c in facts) or "| Research depth | No structured specification record yet | unknown |"
    cap_rows = "\n".join(f"| {name} | Yes | {prov} |" for name, prov in confirmed) or "| Confirmed capabilities | None yet | unresolved |"
    neg_text = ", ".join(negatives) if negatives else "No capability negatives are currently verified."
    scores = ""
    if score:
        rows = "\n".join(f"| {score_labels.get(k, k.replace('_', ' ').title())} | {md_value(v)} |" for k, v in score["scores"].items())
        scores = f"\n## GlassesResearch Report Card\n\nScores use a 0–10 scale; `unknown` means unscored and `na` means not applicable.\n\n| Dimension | Score |\n|---|---:|\n{rows}\n"
    return f'''---
title: "{title.replace('"', '\\"')}"
description: "{description.replace('"', '\\"')}"
model_id: "{record['id']}"
model_name: "{str(record['model']).replace('"', '\\"')}"
model_maker: "{str(record['maker']).replace('"', '\\"')}"
model_category: "{str(record['type']).replace('"', '\\"')}"
---

# {title}

{profile}

## At a glance

| Field | Verified catalog value |
|---|---|
| Canonical ID | **{record['id']}** |
| Manufacturer | {record['maker']} |
| Model | {record['model']} |
| Era / release year | {record['era']} |
| Lifecycle state | {record['state']} |
| Device type | {record['type']} |
| Access route | {record['access']} |
| Catalog evidence class | {record['evidence']} |

Research paths: {' · '.join(paths)} · [Compare in the Finder](/docs/COMPARISON_ENGINE/)

## Verified capabilities

Only confirmed facts are presented as positive. An unresolved field is not treated as a negative.

| Capability | State | Provenance |
|---|---|---|
{cap_rows}

**Verified absent:** {neg_text}

**Coverage note:** {unknown_count} capability fields remain unknown. That is a research status, not a product limitation.

## Structured specifications

| Field | Value | Evidence |
|---|---|---|
{fact_rows}
{scores}
## Sources

{source_links(record)}

The [canonical catalog row](/models/THE_LIST/) is the stable identity ledger. Source links document the catalog claim; deeper specifications may have their own citations in the comparison record.

## Related models

{related_rows or '- No closely related catalog entry is currently identified.'}

## Corrections and research gaps

Unknown fields are deliberately preserved as unknown. To supply primary documentation or challenge a claim, use the [research challenge process](/docs/RESEARCH_CHALLENGES/).
'''


def guide_page(spec: tuple, candidates: list[dict], score_map: dict, cap_map: dict) -> str:
    slug, title, criteria, heading, caveat = spec
    crit = " and ".join(f"**{field.replace('_', ' ')} = {value}**" for field, value in criteria)
    rows = []
    for r in candidates:
        avg = score_average(score_map.get(r["id"]))
        depth = "Report Card available" if avg >= 0 else "catalog + capability record"
        rows.append(f"| [{r['maker']} {r['model']}]({r['public']['model_page']}) | {r['state']} | {r['type']} | {depth} |")
    return f'''---
title: "{title}"
description: "A verified GlassesResearch shortlist built from canonical catalog records and explicit capability evidence, with unknowns left unknown."
---

# {title}

## {heading}

This guide answers a specific search question using the GlassesResearch verified database. Inclusion requires {crit}; unknown values never qualify. It is a research shortlist rather than an affiliate ranking, and it changes when stronger evidence enters the database.

!!! note "Read the evidence state"
    {caveat}

## Verified shortlist

| Model | Status | Category | Research depth |
|---|---|---|---|
{chr(10).join(rows) if rows else '| No model currently meets every verified criterion | — | — | The database keeps unresolved claims unknown |'}

## How to choose

1. Open each canonical model page and check lifecycle state, access route, and evidence class.
2. Compare confirmed capabilities and structured specifications; do not assume an unknown field means yes or no.
3. Follow the primary sources and check current availability, software support, account requirements, and service dependence.
4. Use the [Glasses Finder](/docs/COMPARISON_ENGINE/) for additional filters and side-by-side comparison.

## Method

The shortlist is generated from the same 144-record canonical catalog used by the Finder. A model is included only when every criterion above is explicitly `yes` in the capability matrix. Report Card availability is shown as research depth, not converted into a universal product ranking.

See [all buying and use-case guides](/guides/) or [browse all 144 canonical models](/models/catalog/).
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    devices = load(args.data_dir / "devices.json")
    comparisons = load(args.data_dir / "comparisons.json")
    capabilities = load(args.data_dir / "finder-capabilities.json")
    scores = load(args.data_dir / "report-card-scores.json")
    records = devices["records"]
    profile_map = profiles()
    comparison_map = {r["id"]: r for r in comparisons["records"]}
    cap_map = {r["id"]: r for r in capabilities["records"]}
    score_map = {r["id"]: r for r in scores["records"]}
    labels = {f["id"]: f["label"] for g in comparisons["groups"] for f in g["fields"]}
    labels.update({f: f.replace("_", " ").title() for f in capabilities["capability_fields"]})
    score_labels = {d["id"]: d["label"] for d in scores["dimensions"]}
    catalog = args.output_root / "models" / "catalog"
    catalog.mkdir(parents=True, exist_ok=True)
    makers: dict[str, list[dict]] = {}
    for r in records:
        makers.setdefault(r["maker"], []).append(r)
    for r in records:
        related = [x for x in makers[r["maker"]] if x["id"] != r["id"]]
        if len(related) < 3:
            related += [x for x in records if x["id"] != r["id"] and x["type"] == r["type"] and x not in related]
        page = model_page(r, profile_map[r["id"]], comparison_map.get(r["id"]), cap_map[r["id"]], score_map.get(r["id"]), labels, score_labels, related)
        (catalog / f"{r['id'].lower()}.md").write_text(page, encoding="utf-8")
    index_rows = "\n".join(f"| [{r['maker']} {r['model']}]({r['public']['model_page']}) | {r['id']} | {r['era']} | {r['state']} | {r['type']} |" for r in records)
    (catalog / "index.md").write_text(f"# Canonical smart-glasses model pages\n\nAll {len(records)} individually indexable model records. Each page preserves the stable GLS identity and separates verified facts from unknowns.\n\n[Use the Finder](/docs/COMPARISON_ENGINE/) · [Read the search-intent guides](/guides/) · [View the canonical ledger](/models/THE_LIST/)\n\n| Model | ID | Era | Status | Type |\n|---|---|---:|---|---|\n{index_rows}\n", encoding="utf-8")
    guide_dir = args.output_root / "guides"
    guide_dir.mkdir(parents=True, exist_ok=True)
    guide_links = []
    for spec in GUIDES:
        slug, title, criteria, _, _ = spec
        chosen = [r for r in records if all(cap_map[r["id"]]["capabilities"].get(field, {}).get("value") == value for field, value in criteria)]
        chosen.sort(key=lambda r: (r["state"] == "current", score_average(score_map.get(r["id"])), r["era"]), reverse=True)
        chosen = chosen[:18]
        (guide_dir / f"{slug}.md").write_text(guide_page(spec, chosen, score_map, cap_map), encoding="utf-8")
        guide_links.append(f"- [{title}](/guides/{slug}/) — {len(chosen)} models meet the verified criteria")
    (guide_dir / "index.md").write_text("# Smart-glasses buying and use-case guides\n\nThese guides translate the verified 144-model database into focused shortlists. Unknown facts never qualify a model, and Report Card coverage is shown separately from capability evidence.\n\n" + "\n".join(guide_links) + "\n\n[Browse all canonical model pages](/models/catalog/) · [Open the Glasses Finder](/docs/COMPARISON_ENGINE/)\n", encoding="utf-8")
    print(f"Generated {len(records)} canonical model pages and {len(GUIDES)} search-intent guides")


if __name__ == "__main__":
    main()
