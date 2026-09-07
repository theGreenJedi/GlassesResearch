# The List reconciliation — Captify — 2026-09-06

## Admission decisions

| ID | Maker | Model | State | Type | Access | Evidence |
|---|---|---|---|---|---|---|
| GLS-0167 association | Captify / DreamSmart / MYVU | Captify Myvu | current | binocular accessibility display / audio | direct retail | Captify first-party collaboration statement + matching MYVU/StarV Air hardware profile |
| GLS-0218 | Captify | Captify Pro (CAP001) | current | binocular accessibility display / audio | direct retail | Captify first-party retail/support + FCC ID 2BQMS-CAP001 |

## Identity decisions

### Captify Myvu

Do **not** mint a duplicate hardware-generation ID. Captify explicitly states that its standard/Myvu edition is built in collaboration with DreamSmart MYVU, and its 43 g / 640×480 / 30° / 1,500-nit / 180 mAh profile aligns with the MYVU Air / StarV Air platform already tracked as `GLS-0167`. Captify's software/service package is materially distinct and remains represented in the Captify lineage.

### Captify Pro

Admit as `GLS-0218`. Captify Pro is not merely a software package over the Myvu chassis: Captify publishes a materially different 37 g frame and geometry, while FCC evidence independently assigns model **CAP001**, FCC ID **2BQMS-CAP001**, to Captify Inc. Direct sales and current support documentation establish purchaser history.

## Evidence caveats

- Published hardware values remain manufacturer-stated pending GlassesResearch bench measurements.
- The prescription range conflicts across Captify's own pages and is preserved as unresolved.
- No public SDK/open protocol/firmware recovery path was established in this pass.
- Offline captioning is first-party claimed; cloud independence should not receive a bench-verified score until reproduced.

## Canonical destinations

- [Captify lineage](../lineages/CAPTIFY.md)
- [Captify Pro research hub](CaptifyPro/README.md)
- [Captify lineage investigation](../research/investigations/CAPTIFY_LINEAGE_2026-09-06.md)

This reconciliation reserves `GLS-0218` for Captify Pro. If a concurrent catalog merge consumes that identifier before canonical list regeneration, renumber this admission rather than duplicating a stable ID.
