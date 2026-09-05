# Manufacturer Completeness

A large model catalog can still be incomplete.

GlassesResearch therefore treats **whole-manufacturer completeness** as a separate research problem from model-level evidence depth. A manufacturer may have several well-sourced model pages, report cards, purchase records, or news articles and still contain unseen historical generations, regional products, enterprise variants, aliases, bundles, or adjacent wearables.

The Rokid historical audit on 2026-09-05 demonstrated this failure mode directly: an apparently well-covered major manufacturer still contained three missing canonical eyewear identities and one adjacent industrial wearable.

## Coverage states

| State | Meaning |
|---|---|
| **Unreviewed** | No whole-manufacturer historical audit has been completed. |
| **Partial map** | Useful model or lineage work exists, but historical/product-family completeness has not been reconciled. |
| **Audit in progress** | The manufacturer is being checked across history, regions, aliases, bundles, SDK/support branches and acquisition evidence. |
| **Lineage reconciled** | A dated audit has assigned known products to canonical GLS rows, adjacent ADJ rows, registry/archive candidates, aliases/configurations, or documented non-products. |
| **Monitored** | Reconciled and retained in ongoing manufacturer/source monitoring. |

A lineage chapter is useful evidence organization, but **the existence of a lineage chapter does not certify completeness**.

## Mandatory audit dimensions

A whole-manufacturer audit should check:

1. corporate and brand chronology;
2. all known eyewear generations;
3. regional product names and aliases;
4. manufacturer model numbers, regulatory identifiers and internal nomenclature;
5. retail, preorder, crowdfunding, developer or enterprise acquisition evidence;
6. bundles/configurations versus genuinely distinct eyewear hardware;
7. adjacent head-worn products that belong outside the smart-glasses count;
8. SDK, firmware, support and application branches;
9. the current manufacturer storefront/catalog;
10. historical product, support, press and developer material;
11. unresolved candidates, contradictory first-party claims and archival gaps.

The output is not required to increase the model count. A successful audit may instead collapse aliases, correct dates, retire unsupported identities, or route products to the adjacent catalog.

## Machine guardrail

`data/manufacturer-coverage.json` is the canonical coverage ledger.

`scripts/check_manufacturer_coverage.py` parses the Maker column in `models/THE_LIST.md`. When any exact Maker value reaches **three canonical GLS rows**, it must be assigned to a manufacturer family in the coverage ledger. Missing assignment fails catalog CI.

Families in `unreviewed`, `partial_map`, or `audit_in_progress` state emit coverage-debt warnings when their combined canonical population reaches the threshold. This keeps existing debt visible without pretending that a model count or lineage file proves historical completeness.

## Current priority queue — 2026-09-05

| Priority | Manufacturer family | Current state | Why |
|---:|---|---|---|
| 1 | RayNeo / TCL / Thunderbird | Audit in progress | Brand migration plus X, Air, V3, iO, GT and NXTWEAR branches. Current store changed after earlier catalog work. |
| 2 | Epson Moverio | Audit in progress | Long consumer, enterprise and industrial history; SDK documentation exposes omitted historical hardware identities. |
| 3 | VITURE | Audit in progress | Fast-moving One/Pro/Luma/Beast family; current store already exposes a newer generation not present in the canonical ledger. |
| 4 | INMO | Audit in progress | Air, GO and photography-focused X branches; first-party history exposes an unresolved INMO X product. |
| 5 | Innovative Eyewear / Lucyd | Audit in progress | Loud, Lyte, Armor and multiple licensed-fashion collections require hardware-generation versus frame-style reconciliation. |
| 6 | Meta eyewear | Partial map | Strong current coverage; formal manufacturer-completeness certification still absent. |
| 7 | XREAL / Nreal | Partial map | Dedicated lineage exists, but it must still pass a historical completeness audit. |
| 8 | Vuzix | Partial map | Strong architecture mapping; long historical catalog merits explicit completeness certification. |
| 9 | Snap Spectacles | Partial map | Generation map exists; formal whole-manufacturer certification pending. |
| 10 | Solos | Partial map | AirGo family is represented but not yet certified as historically complete. |

The complete machine-readable queue, including lower-priority and already-reconciled families, is maintained in [`data/manufacturer-coverage.json`](../data/manufacturer-coverage.json).

## Admission discipline

Manufacturer audits follow the same stable-ID rules as the rest of GlassesResearch:

- Do not create a GLS row merely because a product was announced or demonstrated.
- Do not count a bundle twice when the eyewear hardware already has a canonical identity.
- Do not count a colorway, frame style, licensed co-brand, or collector finish as a new hardware generation unless evidence establishes a materially distinct device identity.
- Preserve aliases and real-world model numbers on the canonical record.
- Route helmets, headbands, clip-ons and other non-eyewear interfaces to the adjacent catalog when they qualify.
- Preserve uncertainty explicitly; unresolved history belongs in an investigation queue, not in invented certainty.

## Related research

- [Technology Lineages](../lineages/README.md)
- [The List](../models/THE_LIST.md)
- [Adjacent Wearable-HCI Catalog](../models/ADJACENT_WEARABLES.md)
- [Model Identifier Policy](../models/IDENTIFIER_POLICY.md)
- [Rokid historical audit](../research/investigations/ROKID_HISTORICAL_AUDIT_2026-09-05.md)
