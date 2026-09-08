# External Catalog Benchmarks

A large internal catalog can be internally consistent and still miss products that another researcher, retailer, database, or comparison site has found. GlassesResearch therefore uses external catalogs as **discovery benchmarks**, never as automatic admission authorities.

The machine-readable ledger is [`data/external-catalog-benchmarks.json`](../data/external-catalog-benchmarks.json). Every retained discrepancy must receive one of five dispositions: canonical match, alias/variant, adjacent wearable, non-product, or unresolved. A competing catalog name is not enough evidence to mint a new `GLS-####` identity.

## Initial benchmark set — 2026-09-08

The first pass records two independently maintained external catalogs:

- **AR Compare** — reported 81 models across 35 brands in September 2026. Its broad comparison scope is useful because it also exposes category-boundary problems: headsets, compute hosts, announced products, and frame/style names can appear beside eyeglass-frame smart glasses.
- **AI Glasses Open Database** — reported eight shipping/discontinued products in its July 2026 dataset. Its narrower, cited, machine-readable scope supplies a second independent discovery signal without pretending to cover historical procurement comprehensively.

The benchmark is intentionally **not a count contest**. GlassesResearch currently maintains a historical purchasing ledger, while external sources may count only current products, include announced devices, include accessories, or split styles that GlassesResearch treats as one electronics generation.

## What the first reconciliation already catches

The initial ledger preserves several instructive disagreements instead of silently forcing name matches:

| External identity | Disposition | GlassesResearch result |
|---|---|---|
| Meta Fury | Alias / variant | Resolves to the Meta Glasses platform anchored at `GLS-0165`; no duplicate electronics generation. |
| Magic Leap 2 | Adjacent | `ADJ-0007`; spatial-computing headset plus compute puck, outside the eyewear-only GLS count. |
| Microsoft HoloLens 2 | Adjacent | `ADJ-0005`; mixed-reality headset, not eyeglass-frame smart glasses. |
| Rokid Station 2 | Non-product | Compute host/accessory; no GLS identity. |
| Samsung Smart Glasses | Unresolved | Announcement alone does not satisfy the acquisition threshold for `THE_LIST.md`. |
| OPPO Air Glass 3 | Unresolved | Prototype/announcement boundary still requires acquisition evidence. |
| Warby Parker Intelligent Eyewear | Unresolved | Discovery lead retained without premature canonical admission. |
| GOOVIS G3 Max | Unresolved | Form-factor boundary requires explicit adjudication, likely in adjacent wearable HCI. |

These are exactly the cases a simple normalized-name join would mishandle.

## Machine guardrail

`scripts/check_external_catalog_benchmarks.py` runs in Catalog consistency CI. It verifies that:

- every source has a stable ID, observation date, URL, and reported model count;
- every reconciliation uses a declared disposition;
- duplicate source/name records are rejected;
- `canonical_match` and `alias_or_variant` records point to an existing `GLS-####`;
- `adjacent` records point to an existing `ADJ-####`;
- non-product and unresolved rows do not carry fake canonical IDs;
- every disposition points to an existing internal evidence/research path;
- every retained discrepancy includes a human-readable explanation.

This deliberately validates **our reconciliation evidence**, not the external site's truthfulness.

## Operating rule

When a benchmark source changes, update its observation date/count and add only the names that create a meaningful reconciliation question. Products that obviously map one-to-one to an existing canonical row do not need to bloat the discrepancy ledger unless a full source snapshot is being preserved for a specific audit.

When a discrepancy is resolved, change its state rather than deleting its history. If a new canonical model is justified, follow the stable-ID policy and normal manufacturer-completeness process first, then point the benchmark row at the resulting identity.

## Relationship to manufacturer completeness

External benchmarking and manufacturer completeness solve different failure modes:

- **Manufacturer completeness** asks whether GlassesResearch reconstructed a maker's full history across generations, regions, aliases, support branches, and procurement evidence.
- **External benchmarking** asks whether another catalog has surfaced a name or form factor that our taxonomy must explicitly account for.

A strong catalog needs both. External catalogs are tripwires; first-party/archival evidence remains the basis for admission.

## Related research

- [Manufacturer Completeness](MANUFACTURER_COMPLETENESS.md)
- [The List](../models/THE_LIST.md)
- [Adjacent Wearable-HCI Catalog](../models/ADJACENT_WEARABLES.md)
- [Model Identifier Policy](../models/IDENTIFIER_POLICY.md)
