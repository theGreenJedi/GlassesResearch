# Model Chapters

Each smart-glasses model has its own self-contained research chapter under `models/`.

A model chapter should keep device-specific evidence, notes, diagrams, software, diagnostics, manufacturing intelligence, and reverse-engineering work together. Cross-model material belongs in shared top-level areas only when it genuinely applies to multiple devices.

## Current chapters

- [W610](W610/README.md)

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

Not every chapter needs every directory immediately. Add sections when evidence exists, but preserve this naming convention for consistency.
