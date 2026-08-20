#!/usr/bin/env python3
"""Build the canonical public GlassesResearch Open Smart-Glasses Dataset.

The export joins already validated catalog, comparison, Finder, Report Card,
evidence, ecosystem, and lineage products. It never strengthens a claim:
unknown stays unknown, and lineage never transfers specifications or scores.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MODEL_NODE_RE = re.compile(r"^model:(gls-\d{4})$")
CORE_RELEASE_FILES = (
    "models.json",
    "models.csv",
    "lineages.json",
    "relationships.json",
    "schema.json",
    "evidence-resources.json",
    "ecosystem-relations.json",
)


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def by_id(payload: dict[str, Any], key: str = "records") -> dict[str, dict[str, Any]]:
    return {str(item.get("id")): item for item in payload.get(key, []) if item.get("id")}


def compact_claim(field_id: str, entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "field": field_id,
        "value": entry.get("value"),
        "evidence_state": entry.get("evidence", "unknown"),
        "sources": entry.get("sources", []),
        "confidence": None,
        "verified_at": None,
    }


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def latest_source_date(paths: list[Path]) -> str | None:
    relatives: list[str] = []
    for path in paths:
        try:
            relatives.append(str(path.resolve().relative_to(ROOT)))
        except ValueError:
            continue
    if not relatives:
        return None
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", *relatives],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    value = result.stdout.strip()
    return value or None


def lineage_exports(lineage: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    models = lineage.get("models", {})
    families: dict[str, dict[str, Any]] = {}
    for model_id, context in models.items():
        family_id = str(context.get("family_id") or "")
        if not family_id:
            continue
        family = families.setdefault(
            family_id,
            {
                "id": family_id,
                "label": context.get("family_label") or family_id,
                "model_ids": [],
            },
        )
        family["model_ids"].append(model_id)
    ordered_families = []
    for family in sorted(families.values(), key=lambda item: (str(item["label"]).casefold(), item["id"])):
        family["model_ids"] = sorted(family["model_ids"])
        ordered_families.append(family)

    lineages = {
        "schema_version": 1,
        "semantics": lineage.get("semantics"),
        "family_count": len(ordered_families),
        "model_count": len(models),
        "families": ordered_families,
        "models": models,
    }
    relationships = {
        "schema_version": 1,
        "semantics": lineage.get("semantics"),
        "relationship_count": int(lineage.get("relationship_count", 0)),
        "relationships": lineage.get("relationships", []),
    }
    return lineages, relationships


def checksum_inventory(out: Path) -> dict[str, str]:
    checksums: dict[str, str] = {}
    for path in sorted(out.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(out).as_posix()
        if relative in {"manifest.json", "SHA256SUMS.txt"} or relative.startswith("releases/"):
            continue
        checksums[relative] = sha256(path)
    return checksums


def dataset_version(checksums: dict[str, str]) -> str:
    payload = "\n".join(f"{checksums[path]}  {path}" for path in sorted(checksums)) + "\n"
    return "GRD-" + hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16].upper()


def write_release_snapshot(out: Path, version: str, manifest: dict[str, Any], sums: str) -> None:
    release = out / "releases" / version.lower()
    if release.exists():
        shutil.rmtree(release)
    release.mkdir(parents=True)
    for name in CORE_RELEASE_FILES:
        shutil.copy2(out / name, release / name)
    write_json(release / "manifest.json", manifest)
    (release / "SHA256SUMS.txt").write_text(sums, encoding="utf-8")


def write_landing_page(path: Path, *, manifest: dict[str, Any], site_url: str) -> None:
    version = manifest["version"]
    record_count = manifest["record_count"]
    lineage_count = manifest["lineage_model_count"]
    family_count = manifest["family_count"]
    relationship_count = manifest["relationship_count"]
    release_date = manifest.get("date_modified") or "unknown"
    base = site_url.rstrip("/")
    page = f'''---
description: "Download and cite the GlassesResearch Open Smart-Glasses Dataset: canonical model identities, evidence-tracked claims, lineage context, and stable relationship IDs."
dataset_schema: true
dataset_name: "GlassesResearch Open Smart-Glasses Dataset"
dataset_version: "{version}"
dataset_record_count: {record_count}
dataset_date_modified: "{release_date}"
---
# GlassesResearch Open Smart-Glasses Dataset

**{record_count} canonical models · {lineage_count} lineage-mapped models · {family_count} established families · {relationship_count} stable lineage relationships**

This is the reusable data surface behind GlassesResearch. It is generated from the same validated catalog and research layers used to build the human-readable site; it is **not** a stronger or separate source of claims.

## Download

- [Canonical models — JSON]({base}/data/public/models.json)
- [Canonical models — CSV]({base}/data/public/models.csv)
- [Lineage index — JSON]({base}/data/public/lineages.json)
- [Stable lineage relationships — JSON]({base}/data/public/relationships.json)
- [Dataset manifest]({base}/data/public/manifest.json)
- [SHA-256 checksums]({base}/data/public/SHA256SUMS.txt)
- [Current content-addressed release]({base}/data/public/releases/{version.lower()}/manifest.json)

Each canonical `GLS-####` model also has a dedicated JSON bundle under `/data/public/models/`.

## Current release

- **Version:** `{version}`
- **Source-modified date:** `{release_date}`
- **License:** MIT
- **Identity contract:** permanent `GLS-####` identifiers; retired IDs are not reused.
- **Relationship contract:** stable `GLR-*` identifiers describe lineage relationships themselves.

The version is derived from SHA-256 checksums of the complete public export. If exported content does not change, the dataset version does not change.

## Evidence semantics

`Unknown`, `N/A`, and a verified negative are different states. Missing confidence or verification dates remain null rather than being inferred. Family membership, predecessor/successor position, aliases, and rebrands **never copy specifications, firmware behavior, community observations, verification status, or Report Card scores between models**.

## Cite

For the dataset as a whole:

> GlassesResearch. *GlassesResearch Open Smart-Glasses Dataset*. Version {version}. {base}/dataset/ (accessed as needed).

For a factual claim, cite the canonical GlassesResearch model or relationship record **and the underlying primary source when available**. Model-specific BibTeX and CSL-JSON exports remain available through each canonical model page and the [citation guide]({base}/docs/CITING_GLASSESRESEARCH/).

## Reuse

The JSON exports are intended for software, notebooks, journalism, archival work, independent research, and AI/retrieval systems. The CSV is deliberately flatter for spreadsheet analysis. The manifest and checksum file allow consumers to prove exactly which release they used.
'''
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(page, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--devices", type=Path, required=True)
    ap.add_argument("--comparisons", type=Path, required=True)
    ap.add_argument("--capabilities", type=Path, required=True)
    ap.add_argument("--report-cards", type=Path, required=True)
    ap.add_argument("--ecosystem", type=Path, required=True)
    ap.add_argument("--evidence", type=Path, required=True)
    ap.add_argument("--lineage-index", type=Path, required=True)
    ap.add_argument("--schema", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--page-output", type=Path, required=True)
    ap.add_argument("--site-url", default="https://glassesresearch.org")
    args = ap.parse_args()

    devices = load(args.devices)
    comparisons = by_id(load(args.comparisons))
    capabilities = by_id(load(args.capabilities))
    report_cards = by_id(load(args.report_cards))
    ecosystem = load(args.ecosystem)
    evidence = load(args.evidence)
    lineage = load(args.lineage_index)
    valid_model_ids = {str(record.get("id")) for record in devices.get("records", [])}
    unknown_lineage_ids = set(lineage.get("models", {})) - valid_model_ids
    if unknown_lineage_ids:
        raise RuntimeError(f"lineage index contains non-canonical models: {sorted(unknown_lineage_ids)}")

    nodes = {str(n.get("id")): n for n in ecosystem.get("nodes", []) if n.get("id")}
    relations_by_model: dict[str, list[dict[str, Any]]] = {}
    for rel in ecosystem.get("relations", []):
        endpoints = (str(rel.get("from", "")), str(rel.get("to", "")))
        for endpoint in endpoints:
            node = nodes.get(endpoint, {})
            if node.get("type") != "model":
                continue
            match = MODEL_NODE_RE.fullmatch(str(node.get("id", "")))
            if not match:
                continue
            model_id = match.group(1).upper()
            if model_id in valid_model_ids:
                relations_by_model.setdefault(model_id, []).append(rel)

    records: list[dict[str, Any]] = []
    for device in devices.get("records", []):
        model_id = str(device["id"])
        comparison = comparisons.get(model_id, {})
        cap = capabilities.get(model_id, {})
        claims = [compact_claim(fid, entry) for fid, entry in comparison.get("fields", {}).items()]
        records.append({
            "schema_version": 1,
            "id": model_id,
            "identity": {
                "maker": device.get("maker"),
                "model": device.get("model"),
                "era": device.get("era"),
                "state": device.get("state"),
                "type": device.get("type"),
                "access": device.get("access"),
            },
            "public": device.get("public", {}),
            "catalog_evidence": device.get("evidence"),
            "catalog_links": device.get("links", []),
            "claims": claims,
            "finder_capabilities": cap.get("capabilities", {}),
            "report_card": report_cards.get(model_id),
            "lineage": lineage.get("models", {}).get(model_id),
            "ecosystem_relations": relations_by_model.get(model_id, []),
        })

    out = args.output_dir
    model_dir = out / "models"
    if out.exists():
        shutil.rmtree(out)
    model_dir.mkdir(parents=True)
    (out / "schema.json").write_text(args.schema.read_text(encoding="utf-8"), encoding="utf-8")
    write_json(out / "evidence-resources.json", {"schema_version": evidence.get("schema_version"), "resources": evidence.get("resources", [])})
    write_json(out / "ecosystem-relations.json", ecosystem)

    aggregate = {"schema_version": 1, "record_count": len(records), "records": records}
    write_json(out / "models.json", aggregate)
    for record in records:
        write_json(model_dir / f"{record['id'].lower()}.json", record)

    with (out / "models.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "maker", "model", "era", "state", "type", "access", "model_page", "profile", "report_card", "lineage"])
        writer.writeheader()
        for record in records:
            public = record.get("public", {})
            identity = record["identity"]
            writer.writerow({
                "id": record["id"],
                "maker": identity.get("maker"),
                "model": identity.get("model"),
                "era": identity.get("era"),
                "state": identity.get("state"),
                "type": identity.get("type"),
                "access": identity.get("access"),
                "model_page": public.get("model_page", ""),
                "profile": public.get("profile", ""),
                "report_card": public.get("report_card", ""),
                "lineage": public.get("lineage", ""),
            })

    lineages, relationships = lineage_exports(lineage)
    write_json(out / "lineages.json", lineages)
    write_json(out / "relationships.json", relationships)

    checksums = checksum_inventory(out)
    version = dataset_version(checksums)
    date_modified = latest_source_date([
        args.devices,
        args.comparisons,
        args.capabilities,
        args.report_cards,
        args.ecosystem,
        args.evidence,
        args.lineage_index,
        args.schema,
    ])
    manifest = {
        "schema_version": 1,
        "dataset": "GlassesResearch Open Smart-Glasses Dataset",
        "version": version,
        "date_modified": date_modified,
        "license": "MIT",
        "canonical_url": args.site_url.rstrip("/") + "/dataset/",
        "record_count": len(records),
        "lineage_model_count": int(lineages["model_count"]),
        "family_count": int(lineages["family_count"]),
        "relationship_count": int(relationships["relationship_count"]),
        "semantics": "Generated convenience exports preserve source evidence states. Lineage never inherits specifications, ratings, verification status, or community observations.",
        "checksums": checksums,
    }
    write_json(out / "manifest.json", manifest)
    sums = "".join(f"{digest}  {path}\n" for path, digest in sorted(checksums.items()))
    (out / "SHA256SUMS.txt").write_text(sums, encoding="utf-8")
    write_release_snapshot(out, version, manifest, sums)
    write_landing_page(args.page_output, manifest=manifest, site_url=args.site_url)

    print(
        f"Wrote {version}: {len(records)} canonical models, {lineages['model_count']} lineage-mapped, "
        f"{lineages['family_count']} families, {relationships['relationship_count']} relationships"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
