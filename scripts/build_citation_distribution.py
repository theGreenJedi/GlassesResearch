#!/usr/bin/env python3
"""Build citation/distribution assets from canonical model and Core Report Card data.

The outputs are intentionally static: external sites can embed a GlassesResearch
model card without cookies, tracking, API keys, or cross-origin data fetches.
Citation exports preserve stable GLS identifiers and canonical URLs.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ORIGIN = "https://glassesresearch.org"
MODEL_LINE = re.compile(r"^(Research paths:.*)$", re.MULTILINE)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def bib_escape(value: object) -> str:
    return str(value).replace("\\", "\\textbackslash{}") .replace("{", "\\{").replace("}", "\\}").replace("&", "\\&")


def citation_record(record: dict) -> dict:
    model_id = record["id"]
    title = f"{record['maker']} {record['model']} ({model_id}) — GlassesResearch"
    url = f"{ORIGIN}{record['public']['model_page']}"
    return {
        "id": model_id.lower(),
        "type": "webpage",
        "title": title,
        "author": [{"literal": "GlassesResearch"}],
        "publisher": "GlassesResearch",
        "URL": url,
        "note": f"Canonical smart-glasses record {model_id}",
    }


def bibtex(record: dict) -> str:
    model_id = record["id"]
    key = model_id.lower().replace("-", "")
    title = bib_escape(f"{record['maker']} {record['model']} ({model_id}) — GlassesResearch")
    url = f"{ORIGIN}{record['public']['model_page']}"
    return (
        f"@misc{{{key},\n"
        "  author = {{GlassesResearch}},\n"
        f"  title = {{{{{title}}}}},\n"
        f"  howpublished = {{\\url{{{url}}}}},\n"
        f"  note = {{Canonical smart-glasses record {model_id}}}\n"
        "}\n"
    )


def build_widget(devices: dict, scores: dict) -> str:
    score_map = {record["id"]: record for record in scores.get("records", [])}
    dimensions = scores.get("dimensions", [])
    models = {}
    for record in devices["records"]:
        score_record = score_map.get(record["id"], {})
        models[record["id"]] = {
            "id": record["id"],
            "maker": record["maker"],
            "model": record["model"],
            "state": record["state"],
            "type": record["type"],
            "url": f"{ORIGIN}{record['public']['model_page']}",
            "scores": score_record.get("scores", {}),
        }
    data = json.dumps(models, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    dims = json.dumps(dimensions, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'''/* GlassesResearch embeddable model card. Static, cookie-free, no tracking. */
(function () {{
  "use strict";
  const MODELS = {data};
  const DIMENSIONS = {dims};
  const VERSION = "1";

  function escapeHtml(value) {{
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");
  }}

  function scoreText(value) {{
    if (value === "unknown" || value === undefined || value === null) return "Unknown";
    if (value === "na") return "N/A";
    const number = Number(value);
    if (!Number.isFinite(number)) return "Unknown";
    return `${{Number.isInteger(number) ? number.toFixed(0) : number.toFixed(1)}}/10`;
  }}

  function render(element) {{
    if (!element) return;
    const id = String(element.getAttribute("data-glassesresearch-model") || "").trim().toUpperCase();
    const model = MODELS[id];
    const root = element.shadowRoot || element.attachShadow({{ mode: "open" }});
    if (!model) {{
      root.innerHTML = `<span style="font:14px system-ui,sans-serif">Unknown GlassesResearch model ID: ${{escapeHtml(id || "(empty)")}}</span>`;
      return;
    }}
    const rows = DIMENSIONS.map((dimension) => {{
      const value = model.scores ? model.scores[dimension.id] : "unknown";
      return `<div class="gr-row"><span>${{escapeHtml(dimension.label)}}</span><strong>${{escapeHtml(scoreText(value))}}</strong></div>`;
    }}).join("");
    root.innerHTML = `
      <style>
        :host {{ display:block; max-width:560px; color:#171717; }}
        .gr-card {{ box-sizing:border-box; border:1px solid #d6d6d6; border-radius:12px; padding:16px; background:#fff; font:14px/1.4 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
        .gr-top {{ display:flex; justify-content:space-between; gap:12px; align-items:flex-start; margin-bottom:12px; }}
        .gr-title {{ font-size:17px; font-weight:700; margin:0; }}
        .gr-title a {{ color:inherit; text-decoration:none; }}
        .gr-title a:hover {{ text-decoration:underline; }}
        .gr-id {{ white-space:nowrap; font:12px ui-monospace,SFMono-Regular,Menlo,monospace; color:#666; }}
        .gr-meta {{ color:#555; margin:4px 0 12px; }}
        .gr-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:0 18px; border-top:1px solid #ececec; }}
        .gr-row {{ display:flex; justify-content:space-between; gap:12px; padding:7px 0; border-bottom:1px solid #ececec; }}
        .gr-row strong {{ white-space:nowrap; }}
        .gr-foot {{ margin-top:12px; font-size:12px; color:#666; }}
        .gr-foot a {{ color:inherit; }}
        @media (max-width:480px) {{ .gr-grid {{ grid-template-columns:1fr; }} }}
      </style>
      <article class="gr-card" aria-label="GlassesResearch report card for ${{escapeHtml(model.maker)}} ${{escapeHtml(model.model)}}">
        <div class="gr-top">
          <h2 class="gr-title"><a href="${{escapeHtml(model.url)}}" target="_blank" rel="noopener noreferrer">${{escapeHtml(model.maker)}} ${{escapeHtml(model.model)}}</a></h2>
          <span class="gr-id">${{escapeHtml(model.id)}}</span>
        </div>
        <div class="gr-meta">${{escapeHtml(model.state)}} · ${{escapeHtml(model.type)}}</div>
        <div class="gr-grid">${{rows}}</div>
        <div class="gr-foot">Unknown remains unknown. <a href="${{escapeHtml(model.url)}}" target="_blank" rel="noopener noreferrer">Open evidence and sources at GlassesResearch</a>.</div>
      </article>`;
  }}

  function renderAll(scope) {{
    (scope || document).querySelectorAll("[data-glassesresearch-model]").forEach(render);
  }}

  window.GlassesResearchModelCard = {{ version: VERSION, render, renderAll }};
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", () => renderAll(document));
  else renderAll(document);
}})();
'''


def patch_model_pages(output_root: Path, records: list[dict]) -> None:
    for record in records:
        model_id = record["id"]
        path = output_root / "models" / "catalog" / f"{model_id.lower()}.md"
        if not path.exists():
            raise ValueError(f"generated model page missing for {model_id}: {path}")
        text = path.read_text(encoding="utf-8")
        if "data/citations/" in text:
            continue
        suffix = model_id.lower()
        reuse = (
            f"\nCite or reuse: [BibTeX](/data/citations/{suffix}.bib) · "
            f"[CSL-JSON](/data/citations/{suffix}.json) · "
            "[Embeddable model card](/docs/EMBED_GLASSESRESEARCH/)\n"
        )
        text, count = MODEL_LINE.subn(lambda match: match.group(1) + reuse, text, count=1)
        if count != 1:
            raise ValueError(f"could not add citation links to {model_id}")
        path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--devices", type=Path, required=True)
    parser.add_argument("--scores", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()

    devices = load(args.devices)
    scores = load(args.scores)
    records = devices.get("records", [])
    if devices.get("record_count") != len(records) or not records:
        raise ValueError("device database record_count does not match records")

    score_ids = {record.get("id") for record in scores.get("records", [])}
    device_ids = {record["id"] for record in records}
    if score_ids != device_ids:
        raise ValueError("Core Report Card IDs do not match canonical device IDs")

    citation_dir = args.output_root / "data" / "citations"
    citation_dir.mkdir(parents=True, exist_ok=True)
    index_records = []
    aggregate_bib = []
    for record in records:
        model_id = record["id"]
        suffix = model_id.lower()
        csl = citation_record(record)
        (citation_dir / f"{suffix}.json").write_text(json.dumps(csl, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        bib = bibtex(record)
        (citation_dir / f"{suffix}.bib").write_text(bib, encoding="utf-8")
        aggregate_bib.append(bib)
        index_records.append({
            "id": model_id,
            "canonical_url": csl["URL"],
            "bibtex": f"{ORIGIN}/data/citations/{suffix}.bib",
            "csl_json": f"{ORIGIN}/data/citations/{suffix}.json",
        })

    index = {"schema_version": 1, "record_count": len(index_records), "records": index_records}
    (citation_dir / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (citation_dir / "glassesresearch-models.bib").write_text("\n".join(aggregate_bib), encoding="utf-8")

    js_dir = args.output_root / "javascripts"
    js_dir.mkdir(parents=True, exist_ok=True)
    widget = build_widget(devices, scores)
    (js_dir / "glassesresearch-model-card.js").write_text(widget, encoding="utf-8")

    patch_model_pages(args.output_root, records)

    expected = len(records)
    if len(list(citation_dir.glob("gls-*.json"))) != expected or len(list(citation_dir.glob("gls-*.bib"))) != expected:
        raise ValueError("citation export count mismatch")
    if "cookie" not in widget.lower() or "tracking" not in widget.lower():
        raise ValueError("widget privacy contract marker missing")

    print(f"Built citation exports and embeddable cards for {expected} canonical models")


if __name__ == "__main__":
    main()
