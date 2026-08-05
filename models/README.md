# Model Chapters

[`The List`](THE_LIST.md) is the canonical purchaser-history ledger with stable IDs. The [`model registry`](CATALOG.md) tracks substantive starting points across the smart-glasses ecosystem. A model receives a self-contained chapter under `models/` when enough real evidence exists to make that chapter useful.

A model chapter should keep device-specific evidence, notes, diagrams, software, diagnostics, manufacturing intelligence, and reverse-engineering work together. Cross-model material belongs in shared top-level areas only when it genuinely applies to multiple devices.

## Ecosystem indexes

- [The List](THE_LIST.md) — 112 verified purchasable models and generations, past and present
- [Smart-glasses model registry](CATALOG.md) — broader discovery layer for platforms, prototypes, unnamed devices, and research leads

## Current substantive chapters

- [W610](W610/README.md) — current hands-on reference device

## Standard chapter layout

Each model may include:

- `hardware/` — physical construction, components, measurements, teardowns
- `ble/` — advertisements, services, characteristics, captures, protocol notes
- `firmware/` — versions, dumps, update paths, hashes, analysis
- `software/` — apps, SDKs, APIs, integrations, compatibility
- `manufacturing/` — OEM/ODM relationships, factories, suppliers, product-family evidence
- `diagnostics/` — test procedures, symptoms, logs, known failures
- `diagrams/` — block diagrams, signal flows, architecture drawings
- `schematics/` — traced or sourced circuit information, clearly labeled by confidence
- `evidence/` — photographs, manuals, listings, regulatory records, raw captures
- `resources/` — model-specific links, communities, repositories, vendors, references
- `research-log/` — chronological experiments and findings

Not every registered model needs a chapter immediately, and not every chapter needs every directory. Add sections only when evidence exists, while preserving these names when they fit. The W610 chapter is a reference implementation, not a mandatory empty template.
