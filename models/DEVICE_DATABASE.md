# Device Database

GlassesResearch already has the hard part of a device database: [The List](THE_LIST.md), a stable-ID purchasing-history ledger covering every currently known model that crossed into documented acquisition. This layer turns that ledger into a validated, machine-readable database without creating a second competing source of truth.

## Canonical record

Every device record is anchored by its `GLS-####` ID in [The List](THE_LIST.md). The required core fields are:

| Field | Purpose |
|---|---|
| `id` | Stable GlassesResearch identifier. Never recycled. |
| `maker` | Manufacturer, brand, project, or shared OEM ecosystem. |
| `model` | Publicly marketed model or generation name. |
| `era` | First documented acquisition year or approximate era. |
| `state` | Current, legacy, preorder, enterprise, developer, or other explicitly qualified status. |
| `type` | Functional device category. |
| `access` | How the device could be acquired. |
| `evidence` | Evidence class supporting inclusion/status. |
| `links` | Internal research links and/or external primary/commercial/secondary sources. |

The website build parses all records into `/data/devices.json`. That JSON is generated from The List during CI; it is not edited by hand.

## Enrichment model

The core ledger intentionally stays compact. Richer facts belong in model chapters, glossary records, evidence pages, preservation records, and source-specific research notes, then link back to the stable model ID. Enrichment can include:

- manufacturer, OEM/ODM, aliases, rebrands, and hardware lineage;
- chipset, display, cameras, microphones, speakers, sensors, radios, and battery;
- operating system, companion app, account dependency, offline behavior, SDK/API access, and firmware status;
- FCC or other regulatory identifiers;
- prescription and lens options, repairability, replaceable components, and teardown findings;
- community projects, reverse engineering, BLE/protocol work, recovery methods, and preserved artifacts;
- verification state for each claim.

Unknown fields stay unknown. A sparse verified record is preferable to a complete-looking record assembled from guesses or copied marketplace claims.

## Database invariants

`scripts/build_device_database.py` enforces these rules on every pull request:

1. The declared count in The List must equal the number of parsed model rows.
2. Stable IDs must be unique, sequential, and in canonical numeric order.
3. Every record must contain maker, model, and evidence classification.
4. Every record must contain at least one research or source link.
5. The machine-readable database is regenerated from the human ledger during every site build.

This means adding, deleting, duplicating, or accidentally renumbering a device can fail CI before it reaches the public site.

## Interfaces

- Human master index: [The List](THE_LIST.md)
- Broader research/prototype registry: [Model Registry](CATALOG.md)
- Machine-readable endpoint after deployment: `https://glassesresearch.org/data/devices.json`
- Rich model chapters: [Models](README.md)

The database is deliberately model-agnostic. W610 can be deeply documented because GlassesResearch has a hands-on specimen, while hundreds of other models can still have stable, evidence-backed canonical identities before equivalent hands-on research exists.
