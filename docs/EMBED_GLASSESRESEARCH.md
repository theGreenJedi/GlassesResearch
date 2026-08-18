---
title: "Embed GlassesResearch Model Cards"
description: "Embed a compact, evidence-safe GlassesResearch Core Report Card for any canonical GLS model without cookies, tracking, API keys, or copied ratings."
---

# Embed a GlassesResearch model card

Any canonical `GLS-####` model can be embedded on another website with one HTML element and one static script. The card links back to the canonical GlassesResearch model page so readers can inspect the evidence and sources behind it.

The widget is static and contains no cookies, analytics, tracking calls, API keys, or cross-origin data fetches. `Unknown` and `N/A` remain distinct from numeric scores.

## Copy-paste example

```html
<div data-glassesresearch-model="GLS-0039">
  <a href="https://glassesresearch.org/models/catalog/gls-0039/">
    W610 research at GlassesResearch
  </a>
</div>
<script async src="https://glassesresearch.org/javascripts/glassesresearch-model-card.js"></script>
```

Replace `GLS-0039` with any canonical GLS identifier. Keep the fallback link inside the element: it gives readers a useful destination even when JavaScript is disabled and preserves the canonical research link in the host page's HTML.

## What the card contains

The embedded card shows the canonical model identity, lifecycle state, device type, and the six Core Report Card subjects:

- Discreetness
- Camera
- Visual AI
- Hackability
- Owner Control
- Android Compatibility

A numeric score is shown only when the underlying Core Report Card contains one. Unresolved values render as `Unknown`; not-applicable values render as `N/A`.

## Stable identifiers

Use the GLS identifier rather than a retail alias or rebrand name in the embed attribute. Verified aliases resolve on GlassesResearch itself, while the stable GLS identifier prevents an external embed from becoming ambiguous when market names change.

## Citation exports

Every model also has machine-ready citation files:

- `https://glassesresearch.org/data/citations/gls-####.bib` — BibTeX
- `https://glassesresearch.org/data/citations/gls-####.json` — CSL-JSON
- `https://glassesresearch.org/data/citations/index.json` — citation endpoint index
- `https://glassesresearch.org/data/citations/glassesresearch-models.bib` — aggregate BibTeX for the canonical catalog

For claim-level attribution, cite the canonical GlassesResearch page and the underlying primary source when practical. See [How to Cite GlassesResearch](CITING_GLASSESRESEARCH.md).
