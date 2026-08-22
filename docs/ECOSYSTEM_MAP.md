# Ecosystem relationship map

Smart glasses are rarely isolated products. This map connects hardware to the lineages, apps, platforms, SDKs, transports, services, and community projects that determine what the hardware can do—and what may survive when a vendor changes direction.

The machine-readable source is [`data/ecosystem-relations.json`](../data/ecosystem-relations.json). Every edge carries evidence, provenance, confidence, and status. An absent edge means “not mapped yet,” not “no relationship.”

Manufacturing and design provenance need an additional evidence layer because a seller, app operator, solution house, ODM, tooling owner, and final-assembly factory may all be different organizations. That work now lives in [Who Actually Makes These Glasses? Mapping the Shenzhen Smart-Glasses Platform Ecosystem](SHENZHEN_SMART_GLASSES_SUPPLY_CHAIN.md). Manufacturing relationships are not added to the machine graph until the evidence supports a specific durable edge.

## Seeded ecosystems

| Ecosystem | Hardware starting points | Connected layers | Research path |
|---|---|---|---|
| HeyCyan | Anko Camera Glasses; W610 | lineage, software platform, companion app, CyanBridge community project | [HeyCyan lineage](../lineages/HEYCYAN.md) |
| Shenzhen reference-platform / manufacturing provenance | W610 and recurring V821/V821L2 camera-glasses families | silicon, solution houses, ODM/factory leads, app operators, commercial suppliers, rebrands | [Supply-chain investigation](SHENZHEN_SMART_GLASSES_SUPPLY_CHAIN.md) |
| Solos | AirGo V2 | AirGo lineage, Solos SDK, BLE control | [Solos lineage](../lineages/SOLOS.md) |
| Even Realities | G2 | Even companion application, cloud AI and translation services | [G2 model research](../models/EvenG2/README.md) |
| Mentra | Mentra Live | MentraOS, SDK, BLE transport, Mentra Community | [Mentra Live in the canonical ledger](../models/THE_LIST.md) |

## How to read a relationship

- **Established** means the cited evidence directly supports the edge.
- **Inferred** means multiple clues support it but direct confirmation is incomplete.
- **Unresolved** records a material hypothesis without presenting it as fact.
- **Confidence** expresses the strength of the current support, independently of whether a source is primary, independent, community-produced, or hands-on.

The graph intentionally distinguishes a device that *uses a platform* from one that merely is *compatible with* a project, and a vendor SDK from a community project that supports the same ecosystem.

## Manufacturing-provenance boundary

A model should not receive a `manufactured_by` relationship merely because a company sells it, calls itself an OEM/ODM, operates its companion app, or appears on a marketplace listing. The supply-chain investigation first asks which entity actually owns or controls the relevant design, tooling, firmware, SMT, assembly, and test responsibilities.

Where the evidence supports only a lead, that lead remains prose research with a confidence label rather than a machine-readable manufacturing fact.

## Relationship vocabulary

`member_of`, `rebrand_of`, `manufactured_by`, `uses_platform`, `compatible_with`, `requires_app`, `exposes_sdk`, `uses_protocol`, `depends_on_service`, `community_supports`, and `supersedes`.

## Boundaries

This layer does not replace the canonical model ledger, comparison data, lineage research, manufacturing-provenance research, or evidence corpus. It indexes relationships among those sources. New nodes and edges must resolve to durable repository research or a direct external resource, and every edge must state its evidence and uncertainty.
