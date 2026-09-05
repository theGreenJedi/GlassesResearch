# Manufacturer Completeness

A large model catalog can still be incomplete.

GlassesResearch therefore treats **whole-manufacturer completeness** as a separate research problem from model-level evidence depth. A manufacturer may have several well-sourced model pages, report cards, purchase records, or news articles and still contain unseen historical generations, regional products, enterprise variants, aliases, bundles, or adjacent wearables.

The Rokid historical audit on 2026-09-05 demonstrated this failure mode directly: an apparently well-covered major manufacturer still contained three missing canonical eyewear identities and one adjacent industrial wearable. The first two program waves then proved Rokid was not an isolated case.

## Coverage states

| State | Meaning |
|---|---|
| **Unreviewed** | No whole-manufacturer historical audit has been completed. |
| **Partial map** | Useful model or lineage work exists, but historical/product-family completeness has not been reconciled. |
| **Audit in progress** | The manufacturer is being checked across history, regions, aliases, bundles, SDK/support branches and acquisition evidence. |
| **Lineage reconciled** | A dated audit has assigned known products to canonical GLS rows, adjacent ADJ rows, registry/archive candidates, aliases/configurations, or documented non-products. |
| **Monitored** | Reconciled and retained in ongoing manufacturer/source monitoring. |

A lineage chapter is useful evidence organization, but **the existence of a lineage chapter does not certify completeness**.

## What the first audits found

| Audit | Families | Canonical result | Adjacent result | Important anti-inflation result |
|---|---|---:|---:|---|
| Rokid historical audit | Rokid | +3 | +1 | Style/Neo aliases, AR bundles and X-Craft form boundary resolved |
| Wave 01 | RayNeo/TCL, Epson, VITURE, INMO, Lucyd | +10 | +2 | Bundles, collector editions and licensed frame proliferation held back |
| Wave 02 | Vuzix, XREAL/Nreal, Meta, Snap, Solos | +23 | +4 | Meta Fury/Starfire and Snap Nico/Veronica resolved as styles/variants, not fake generations |

Wave 02 is especially important methodologically. Vuzix already had one of the site's stronger technical lineage chapters and eleven canonical models, yet the manufacturer-wide reconstruction exposed an entire older consumer display-eyewear era. Conversely, the equally deep Meta and Snap audits added **zero** models because the extra names resolved to styles. Completeness is therefore measured by **resolved history**, not by how many IDs an audit creates.

After Wave 02 synchronization, the canonical purchaser-history ledger advances from **193 to 216** records.

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

Reconciled families remain monitored because a completed audit is a dated evidence state, not a permanent claim that a manufacturer can never release or reveal another product.

## Current priority queue — after Wave 02

The five Wave 02 families—**Vuzix, XREAL/Nreal, Meta, Snap and Solos**—are now reconciled and monitored. Remaining debt is prioritized by population size, archival risk and naming complexity.

| Priority | Manufacturer family | Current state | Why |
|---:|---|---|---|
| 1 | RayNeo / TCL / Thunderbird | Audit in progress | Brand migration plus X, Air, V3, iO, GT and NXTWEAR branches; regional naming still needs full closure. |
| 2 | Epson Moverio | Audit in progress | Long consumer, enterprise and industrial history; regional/industrial archival checks remain. |
| 3 | VITURE | Audit in progress | Fast-moving One/Pro/Luma/Beast family; collector/co-brand and rapid-generation boundaries remain active. |
| 4 | INMO | Audit in progress | 2021-versus-2024 X relationship remains unresolved. |
| 5 | Innovative Eyewear / Lucyd | Audit in progress | Lyte 2025 and licensed-fashion electronics boundaries remain unresolved. |
| 6 | RealWear | Unreviewed | Five enterprise generations and high archival-risk procurement history. |
| 7 | Lenovo smart glasses | Partial map | ThinkReality and Legion branches span different architectures and naming systems. |
| 8 | Bose Frames | Partial map | Five canonical styles across two electronics generations; formal whole-company reconciliation still missing. |
| 9 | Amazon Echo Frames | Partial map | Three Echo Frames generations plus Carrera implementation require family/variant adjudication. |
| 10 | Huawei smart eyewear | Partial map | Gentle Monster audio collaborations, Huawei-branded audio eyewear and Vision Glass are materially different branches. |
| 11 | Iristick | Unreviewed | Four enterprise generations; procurement products are easy to lose from consumer-web history. |
| 12 | CORNMI NeoVista | Partial map | Four current display-glasses identities admitted from a focused audit but no whole-manufacturer history yet. |
| 13 | Xiaomi smart eyewear | Partial map | Audio, camera/display and AI-camera branches have regional Chinese-market history. |
| 14 | Dymesty | Partial map | Three named products plus possible upstream OEM relationships. |

The complete machine-readable queue, including already-reconciled families, is maintained in [`data/manufacturer-coverage.json`](../data/manufacturer-coverage.json).

## Admission discipline

Manufacturer audits follow the same stable-ID rules as the rest of GlassesResearch:

- Do not create a GLS row merely because a product was announced or demonstrated.
- Do not count a bundle twice when the eyewear hardware already has a canonical identity.
- Do not count a colorway, frame style, licensed co-brand, or collector finish as a new hardware generation unless evidence establishes a materially distinct device identity.
- Preserve aliases and real-world model numbers on the canonical record.
- Route helmets, headbands, clip-ons and other non-eyewear interfaces to the adjacent catalog when they qualify.
- Preserve uncertainty explicitly; unresolved history belongs in an investigation queue, not in invented certainty.
- Do not allow a generic audit-year placeholder to overwrite an evidence-backed first-sale era; reconciliation packets should carry explicit eras when known.

## Audit packets

- [Rokid historical audit](../research/investigations/ROKID_HISTORICAL_AUDIT_2026-09-05.md)
- [Manufacturer Completeness Wave 01](../research/investigations/MANUFACTURER_COMPLETENESS_WAVE_01_2026-09-05.md)
- [Manufacturer Completeness Wave 02](../research/investigations/MANUFACTURER_COMPLETENESS_WAVE_02_2026-09-05.md)

## Related research

- [Technology Lineages](../lineages/README.md)
- [The List](../models/THE_LIST.md)
- [Adjacent Wearable-HCI Catalog](../models/ADJACENT_WEARABLES.md)
- [Model Identifier Policy](../models/IDENTIFIER_POLICY.md)
