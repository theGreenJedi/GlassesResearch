#!/usr/bin/env python3
"""Verify generated Frictionless Data Package and W3C DCAT 3 metadata."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ORIGIN = "https://glassesresearch.org"
DATASET_URL = f"{ORIGIN}/dataset/"
PUBLIC_URL = f"{ORIGIN}/data/public"
EXPECTED_RESOURCES = {
    "models-csv": ("models.csv", "text/csv"),
    "models-json": ("models.json", "application/json"),
    "lineages": ("lineages.json", "application/json"),
    "relationships": ("relationships.json", "application/json"),
    "evidence-resources": ("evidence-resources.json", "application/json"),
    "ecosystem-relations": ("ecosystem-relations.json", "application/json"),
    "model-schema": ("schema.json", "application/json"),
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def fail(message: str) -> None:
    raise RuntimeError(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    args = parser.parse_args()
    root = args.site_root
    public = root / "data" / "public"
    dataset = root / "dataset"
    manifest = load(public / "manifest.json")
    checksums = manifest.get("checksums", {})

    datapackage = load(dataset / "datapackage.json")
    if datapackage.get("profile") != "data-package":
        fail("Data Package does not explicitly declare the data-package profile")
    if datapackage.get("name") != "glassesresearch-open-smart-glasses-dataset":
        fail("Data Package has the wrong stable name")
    if datapackage.get("id") != DATASET_URL or datapackage.get("homepage") != DATASET_URL:
        fail("Data Package identity/homepage drifted from the canonical dataset URL")
    if datapackage.get("glassesresearchVersion") != manifest.get("version"):
        fail("Data Package GRD version drifted from the canonical manifest")
    licenses = datapackage.get("licenses", [])
    if not any(item.get("name") == "MIT" for item in licenses if isinstance(item, dict)):
        fail("Data Package does not declare the MIT license")

    resources = datapackage.get("resources")
    if not isinstance(resources, list) or len(resources) != len(EXPECTED_RESOURCES):
        fail("Data Package resource count drifted")
    by_name = {item.get("name"): item for item in resources if isinstance(item, dict)}
    if set(by_name) != set(EXPECTED_RESOURCES):
        fail("Data Package resource names drifted")
    for name, (filename, media) in EXPECTED_RESOURCES.items():
        entry = by_name[name]
        expected_profile = "tabular-data-resource" if name == "models-csv" else "data-resource"
        if entry.get("profile") != expected_profile:
            fail(f"Data Package resource profile drifted for {name}")
        if entry.get("path") != f"{PUBLIC_URL}/{filename}":
            fail(f"Data Package path drifted for {name}")
        if entry.get("mediatype") != media:
            fail(f"Data Package media type drifted for {name}")
        expected_hash = checksums.get(filename)
        if entry.get("hash") != f"sha256:{expected_hash}":
            fail(f"Data Package checksum drifted for {name}")
        if entry.get("bytes") != (public / filename).stat().st_size:
            fail(f"Data Package byte count drifted for {name}")

    csv_resource = by_name["models-csv"]
    schema = csv_resource.get("schema", {})
    fields = schema.get("fields", [])
    expected_fields = [
        "id", "maker", "model", "era", "state", "type", "access",
        "model_page", "profile", "report_card", "lineage",
    ]
    if [field.get("name") for field in fields] != expected_fields or schema.get("primaryKey") != "id":
        fail("models.csv Table Schema drifted from the generated CSV contract")

    dcat = load(dataset / "dcat.jsonld")
    context = dcat.get("@context", {})
    if context.get("dcat") != "http://www.w3.org/ns/dcat#":
        fail("DCAT descriptor does not use the canonical DCAT namespace")
    graph = dcat.get("@graph")
    if not isinstance(graph, list):
        fail("DCAT descriptor has no JSON-LD graph")
    nodes = {node.get("@id"): node for node in graph if isinstance(node, dict) and node.get("@id")}
    dataset_node = nodes.get(DATASET_URL)
    if not dataset_node or dataset_node.get("@type") != "dcat:Dataset":
        fail("DCAT graph is missing the canonical dcat:Dataset node")
    if dataset_node.get("dcat:version") != manifest.get("version"):
        fail("DCAT version drifted from the canonical GRD manifest")
    if dataset_node.get("dct:license", {}).get("@id") != "https://opensource.org/license/mit":
        fail("DCAT dataset does not declare the MIT license")

    distribution_refs = dataset_node.get("dcat:distribution", [])
    ref_ids = {item.get("@id") for item in distribution_refs if isinstance(item, dict)}
    expected_ids = {f"{DATASET_URL}#distribution-{name}" for name in EXPECTED_RESOURCES}
    if ref_ids != expected_ids:
        fail("DCAT distribution references drifted from the public resource set")
    for name, (filename, media) in EXPECTED_RESOURCES.items():
        node_id = f"{DATASET_URL}#distribution-{name}"
        node = nodes.get(node_id)
        if not node or node.get("@type") != "dcat:Distribution":
            fail(f"DCAT distribution node missing for {name}")
        if node.get("dcat:downloadURL", {}).get("@id") != f"{PUBLIC_URL}/{filename}":
            fail(f"DCAT download URL drifted for {name}")
        expected_media = f"https://www.iana.org/assignments/media-types/{media}"
        if node.get("dcat:mediaType", {}).get("@id") != expected_media:
            fail(f"DCAT media type drifted for {name}")
        if node.get("dcat:byteSize", {}).get("@value") != (public / filename).stat().st_size:
            fail(f"DCAT byte count drifted for {name}")
        checksum = node.get("spdx:checksum", {})
        if checksum.get("@type") != "spdx:Checksum":
            fail(f"DCAT checksum node missing for {name}")
        if checksum.get("spdx:algorithm", {}).get("@id") != "http://spdx.org/rdf/terms#checksumAlgorithm_sha256":
            fail(f"DCAT checksum algorithm drifted for {name}")
        checksum_value = checksum.get("spdx:checksumValue", {})
        if checksum_value.get("@type") != "xsd:hexBinary":
            fail(f"DCAT checksum value is not typed as xsd:hexBinary for {name}")
        if checksum_value.get("@value") != checksums.get(filename):
            fail(f"DCAT checksum value drifted for {name}")

    page = (dataset / "index.md").read_text(encoding="utf-8")
    for marker in (
        "## Catalog interoperability",
        "/dataset/datapackage.json",
        "/dataset/dcat.jsonld",
    ):
        if marker not in page:
            fail(f"dataset landing page is missing interoperability marker {marker!r}")

    print(
        f"Dataset interoperability verified: {manifest['version']}, "
        f"{len(EXPECTED_RESOURCES)} Data Package/DCAT distributions"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
