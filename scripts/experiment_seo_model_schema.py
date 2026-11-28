#!/usr/bin/env python3
"""Non-deploying experiment: compare three builds from the same staged source."""
from __future__ import annotations

import json
import re
import subprocess
import tempfile
from pathlib import Path
import xml.etree.ElementTree as ET

import verify_discoverability as audit

ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / "scripts/seo_hook.py"
SCRIPT = re.compile(r'<script\s+type="application/ld\+json"\s*>(.*?)</script>', re.S)
PRODUCT_TYPE = '"@type": "Product",'
MODEL_GATE = 'if not meta.get("model_id"):'


def split_html(text):
    """Remove only the generator's product node; preserve every other byte."""
    models = []

    def replace(match):
        payload = json.loads(match.group(1))
        if (isinstance(payload, dict)
                and payload.get("@type") in ("Product", "ProductModel")
                and str(payload.get("@id", "")).endswith("#product")):
            models.append(payload)
            return ""
        return match.group(0)

    return SCRIPT.sub(replace, text), models


def build(source, target):
    HOOK.write_bytes(source)
    subprocess.run(["mkdocs", "build", "--strict", "--site-dir", str(target)],
                   cwd=ROOT, check=True)
    audit.SITE = target
    audit.main()


def sitemap_urls(site):
    tree = ET.parse(site / "sitemap.xml")
    return sorted(n.text for n in tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"))


def compare(baseline, candidate, kind):
    paths = sorted(p.relative_to(baseline) for p in baseline.rglob("*.html"))
    assert paths == sorted(p.relative_to(candidate) for p in candidate.rglob("*.html")), "HTML paths differ"
    assert sitemap_urls(baseline) == sitemap_urls(candidate), "Sitemap URLs differ"
    for path in ("robots.txt", "CNAME", "search/search_index.json"):
        assert (baseline / path).read_bytes() == (candidate / path).read_bytes(), f"{path} differs"
    models = 0
    errors = []
    for path in paths:
        a, nodes_a = split_html((baseline / path).read_text(encoding="utf-8"))
        b, nodes_b = split_html((candidate / path).read_text(encoding="utf-8"))
        if a != b:
            errors.append(f"{path}: unexpected HTML changes")
        if len(nodes_a) > 1:
            errors.append(f"{path}: multiple generated product nodes")
        if not nodes_a:
            if nodes_b:
                errors.append(f"{path}: unexpected model node")
            continue
        models += 1
        node = nodes_a[0]
        if any(k in node for k in ("offers", "review", "aggregateRating")):
            errors.append(f"{path}: baseline assumption no longer holds")
        expected = [] if kind == "omitted" else [dict(node, **{"@type": "ProductModel"})]
        if nodes_b != expected:
            errors.append(f"{path}: unexpected model metadata delta")
    assert models > 0, "No baseline product nodes found"
    print(f"{kind}: compared {len(paths)} HTML files, {models} model nodes; "
          f"{len(errors)} unexpected differences", flush=True)
    if errors:
        raise AssertionError("\n".join(errors[:30]))
    return {"html_pages": len(paths), "model_nodes": models, "unexpected_differences": 0}


def main():
    original = HOOK.read_bytes()
    source = original.decode("utf-8")
    assert source.count(PRODUCT_TYPE) == 1, "Unexpected Product generator shape"
    assert source.count(MODEL_GATE) == 1, "Unexpected model gate shape"
    omitted = source.replace(MODEL_GATE, "if True:  # experiment only", 1)
    model_type = source.replace(PRODUCT_TYPE, '"@type": "ProductModel",', 1)
    result = {}
    try:
        with tempfile.TemporaryDirectory(prefix="gr-seo-experiment-") as temp:
            root = Path(temp)
            baseline = root / "baseline"
            build(original, baseline)
            for label, variant in (("omitted", omitted), ("productmodel", model_type)):
                candidate = root / label
                build(variant.encode("utf-8"), candidate)
                result[label] = compare(baseline, candidate, label)
    finally:
        HOOK.write_bytes(original)
    print(json.dumps(result, indent=2))
    print("Local build equivalence only; Google rich-result eligibility and ranking are not tested.")


if __name__ == "__main__":
    main()
