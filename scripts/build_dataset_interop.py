#!/usr/bin/env python3
"""Generate standards-based descriptors for the GlassesResearch open dataset."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ORIGIN = "https://glassesresearch.org"
DATASET_URL = f"{ORIGIN}/dataset/"
PUBLIC_URL = f"{ORIGIN}/data/public"

RESOURCE_SPECS = (
    ("models-csv", "models.csv", "Canonical smart-glasses models — CSV", "csv", "text/csv"),
    ("models-json", "models.json", "Canonical smart-glasses models — JSON", "json", "application/json"),
    ("lineages", "lineages.json", "Smart-glasses lineage families", "json", "application/json"),
    ("relationships", "relationships.json", "Stable lineage relationships", "json", "application/json"),
    ("evidence-resources", "evidence-resources.json", "Evidence-resource registry", "json", "application/json"),
    ("ecosystem-relations", "ecosystem-relations.json", "Ecosystem relationship graph", "json", "application/json"),
    ("model-schema", "schema.json", "Per-model JSON Schema", "json", "application/json"),
)

CSV_SCHEMA = {
    "fields": [
        {"name": "id", "type": "string", "constraints": {"required": True, "unique": True}},
        {"name": "maker", "type": "string"},
        {"name": "model", "type": "string"},
        {"name": "era", "type": "string"},
        {"name": "state", "type": "string"},
        {"name": "type", "type": "string"},
        {"name": "access", "type": "string"},
        {"name": "model_page", "type": "string"},
        {"name": "profile", "type": "string"},
        {"name": "report_card", "type": "string"},
        {"name": "lineage", "type": "string"},
    ],
    "primaryKey": "id",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def resource_descriptor(public: Path, manifest: dict, name: str, filename: str, title: str, fmt: str, media: str) -> dict:
    path = public / filename
    checksum = manifest["checksums"].get(filename)
    if not path.is_file() or not checksum:
        raise RuntimeError(f"dataset interoperability resource is missing or unhashed: {filename}")
    descriptor = {
        "name": name,
        "path": f"{PUBLIC_URL}/{filename}",
        "title": title,
        "format": fmt,
        "mediatype": media,
        "bytes": path.stat().st_size,
        "hash": f"sha256:{checksum}",
    }
    if filename == "models.csv":
        descriptor["profile"] = "tabular-data-resource"
        descriptor["encoding"] = "utf-8"
        descriptor["schema"] = CSV_SCHEMA
    return descriptor


def build_datapackage(public: Path, manifest: dict) -> dict:
    resources = [resource_descriptor(public, manifest, *spec) for spec in RESOURCE_SPECS]
    return {
        "name": "glassesresearch-open-smart-glasses-dataset",
        "id": DATASET_URL,
        "title": "GlassesResearch Open Smart-Glasses Dataset",
        "description": (
            "Canonical smart-glasses identities, evidence-tracked research claims, lineage context, "
            "stable relationship identifiers, and reusable public exports. Unknown, N/A, and verified "
            "negative states remain distinct; lineage does not inherit claims or scores."
        ),
        "homepage": DATASET_URL,
        "licenses": [
            {
                "name": "MIT",
                "path": "https://opensource.org/license/mit",
                "title": "MIT License",
            }
        ],
        "sources": [
            {
                "title": "GlassesResearch validated research corpus",
                "path": "https://github.com/theGreenJedi/GlassesResearch",
            }
        ],
        "contributors": [
            {
                "title": "GlassesResearch",
                "path": f"{ORIGIN}/",
                "role": "publisher",
            }
        ],
        "keywords": [
            "smart glasses",
            "AI glasses",
            "wearable computing",
            "augmented reality",
            "open data",
        ],
        "glassesresearchVersion": manifest["version"],
        "resources": resources,
    }


def checksum_node(digest: str) -> dict:
    return {
        "@type": "spdx:Checksum",
        "spdx:algorithm": {"@id": "http://spdx.org/rdf/terms#checksumAlgorithm_sha256"},
        "spdx:checksumValue": {"@value": digest, "@type": "xsd:hexBinary"},
    }


def build_dcat(public: Path, manifest: dict) -> dict:
    distributions = []
    distribution_ids = []
    for name, filename, title, _fmt, media in RESOURCE_SPECS:
        path = public / filename
        digest = manifest["checksums"].get(filename)
        if not path.is_file() or not digest:
            raise RuntimeError(f"DCAT resource is missing or unhashed: {filename}")
        node_id = f"{DATASET_URL}#distribution-{name}"
        distribution_ids.append({"@id": node_id})
        distributions.append(
            {
                "@id": node_id,
                "@type": "dcat:Distribution",
                "dct:title": title,
                "dcat:downloadURL": {"@id": f"{PUBLIC_URL}/{filename}"},
                "dcat:mediaType": {
                    "@id": f"https://www.iana.org/assignments/media-types/{media}"
                },
                "dcat:byteSize": {
                    "@value": path.stat().st_size,
                    "@type": "xsd:nonNegativeInteger",
                },
                "spdx:checksum": checksum_node(digest),
            }
        )

    dataset = {
        "@id": DATASET_URL,
        "@type": "dcat:Dataset",
        "dct:identifier": DATASET_URL,
        "dct:title": "GlassesResearch Open Smart-Glasses Dataset",
        "dct:description": (
            "Canonical smart-glasses identities and evidence-preserving research exports with "
            "lineage and stable relationship context."
        ),
        "dct:publisher": {"@id": f"{ORIGIN}/#organization"},
        "dct:license": {"@id": "https://opensource.org/license/mit"},
        "dcat:landingPage": {"@id": DATASET_URL},
        "dcat:version": manifest["version"],
        "dcat:distribution": distribution_ids,
    }
    if manifest.get("date_modified") and manifest["date_modified"] != "unknown":
        dataset["dct:modified"] = {
            "@value": manifest["date_modified"],
            "@type": "xsd:date",
        }

    return {
        "@context": {
            "dcat": "http://www.w3.org/ns/dcat#",
            "dct": "http://purl.org/dc/terms/",
            "foaf": "http://xmlns.com/foaf/0.1/",
            "spdx": "http://spdx.org/rdf/terms#",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
        },
        "@graph": [
            {
                "@id": f"{ORIGIN}/#organization",
                "@type": "foaf:Organization",
                "foaf:name": "GlassesResearch",
                "foaf:homepage": {"@id": f"{ORIGIN}/"},
            },
            dataset,
            *distributions,
        ],
    }


def patch_landing_page(page: Path) -> None:
    text = page.read_text(encoding="utf-8")
    if "## Catalog interoperability" in text:
        raise RuntimeError("dataset interoperability section already exists before generation")
    section = """

## Catalog interoperability

For data catalogs, notebooks, and research tooling:

- [Frictionless Data Package descriptor](/dataset/datapackage.json)
- [W3C DCAT 3 JSON-LD descriptor](/dataset/dcat.jsonld)

These descriptors point to the same canonical JSON/CSV exports above. They do not create a parallel dataset or strengthen any evidence state.
"""
    page.write_text(text.rstrip() + section + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    args = parser.parse_args()
    root = args.site_root
    public = root / "data" / "public"
    dataset_dir = root / "dataset"
    manifest = load(public / "manifest.json")

    write_json(dataset_dir / "datapackage.json", build_datapackage(public, manifest))
    write_json(dataset_dir / "dcat.jsonld", build_dcat(public, manifest))
    patch_landing_page(dataset_dir / "index.md")
    print(f"Built Data Package and DCAT 3 descriptors for {manifest['version']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
