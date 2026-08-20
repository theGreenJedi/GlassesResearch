#!/usr/bin/env python3
"""Verify the generated GlassesResearch Open Smart-Glasses Dataset contract."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

VERSION_RE = re.compile(r"^GRD-[0-9A-F]{16}$")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> None:
    raise RuntimeError(message)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site-root", type=Path, default=Path(".site-src"))
    args = ap.parse_args()
    root = args.site_root
    public = root / "data" / "public"

    devices = load(root / "data" / "devices.json")
    lineage = load(root / "data" / "lineage-index.json")
    models = load(public / "models.json")
    lineages = load(public / "lineages.json")
    relationships = load(public / "relationships.json")
    manifest = load(public / "manifest.json")

    record_count = int(devices.get("record_count", -1))
    if models.get("record_count") != record_count or len(models.get("records", [])) != record_count:
        fail("public model count drifted from canonical devices")
    if lineages.get("model_count") != lineage.get("model_count"):
        fail("public lineage model count drifted from lineage index")
    if relationships.get("relationship_count") != lineage.get("relationship_count"):
        fail("public relationship count drifted from lineage index")
    family_ids = {context.get("family_id") for context in lineage.get("models", {}).values() if context.get("family_id")}
    if lineages.get("family_count") != len(family_ids):
        fail("public family count drifted from lineage index")

    version = str(manifest.get("version") or "")
    if not VERSION_RE.fullmatch(version):
        fail(f"invalid dataset version {version!r}")
    expected_counts = {
        "record_count": record_count,
        "lineage_model_count": lineage.get("model_count"),
        "family_count": len(family_ids),
        "relationship_count": lineage.get("relationship_count"),
    }
    for key, expected in expected_counts.items():
        if manifest.get(key) != expected:
            fail(f"manifest {key}={manifest.get(key)!r}; expected {expected!r}")

    checksums = manifest.get("checksums")
    if not isinstance(checksums, dict) or not checksums:
        fail("dataset manifest has no checksum inventory")
    for relative, expected in checksums.items():
        path = public / relative
        if not path.is_file():
            fail(f"checksum target missing: {relative}")
        actual = sha256(path)
        if actual != expected:
            fail(f"checksum mismatch for {relative}: expected {expected}, got {actual}")

    sums_lines = (public / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines()
    parsed_sums = {}
    for line in sums_lines:
        digest, sep, relative = line.partition("  ")
        if not sep:
            fail(f"malformed SHA256SUMS line: {line!r}")
        parsed_sums[relative] = digest
    if parsed_sums != checksums:
        fail("SHA256SUMS inventory drifted from manifest")

    release = public / "releases" / version.lower()
    for name in ("models.json", "models.csv", "lineages.json", "relationships.json", "schema.json", "evidence-resources.json", "ecosystem-relations.json", "manifest.json", "SHA256SUMS.txt"):
        if not (release / name).is_file():
            fail(f"content-addressed release is missing {name}")
    for name in ("models.json", "models.csv", "lineages.json", "relationships.json", "schema.json", "evidence-resources.json", "ecosystem-relations.json"):
        if (release / name).read_bytes() != (public / name).read_bytes():
            fail(f"release snapshot drifted from current export: {name}")

    model_files = list((public / "models").glob("gls-*.json"))
    if len(model_files) != record_count:
        fail(f"expected {record_count} per-model JSON files, found {len(model_files)}")
    mapped_records = sum(1 for record in models.get("records", []) if record.get("lineage"))
    if mapped_records != lineage.get("model_count"):
        fail("per-model lineage context coverage drifted from lineage index")

    page = root / "dataset" / "index.md"
    if not page.is_file():
        fail("dataset landing page was not generated")
    text = page.read_text(encoding="utf-8")
    for required in (version, f"{record_count} canonical models", "SHA-256 checksums", "dataset_schema: true"):
        if required not in text:
            fail(f"dataset landing page missing {required!r}")

    print(
        f"Open dataset verified: {version}, {record_count} models, "
        f"{lineage.get('model_count')} lineage-mapped, {len(family_ids)} families, "
        f"{lineage.get('relationship_count')} relationships"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
