# Epson Moverio lineage

Epson's Moverio history spans **standalone Android smart glasses, tethered display glasses, fleet/enterprise variants, and industrial head-worn systems**. GlassesResearch treats Moverio as a corporate lineage with multiple technical branches rather than copying one generation's properties across the family.

**Relationship type:** corporate lineage; branch-specific hardware/software continuity  
**Confidence:** Confirmed

## Smart-glasses population

- `GLS-0106` — Moverio BT-100
- `GLS-0107` — Moverio BT-200
- `GLS-0108` — Moverio BT-300
- `GLS-0189` — Moverio BT-350
- `GLS-0190` — Moverio BT-30E
- `GLS-0109` — Moverio BT-30C
- `GLS-0110` — Moverio BT-35E
- `GLS-0111` — Moverio BT-40 / BT-40S
- `GLS-0112` — Moverio BT-45C / BT-45CS

## Adjacent industrial systems

- `ADJ-0011` — Moverio Pro BT-2000
- `ADJ-0012` — Moverio Pro BT-2200

BT-2000 and BT-2200 are preserved because they are historically important Moverio systems, but Epson describes them as industrial **smart headsets** using headbands/forehead support and, for BT-2200, safety-helmet mounting. They therefore belong in the adjacent wearable catalog rather than inflating the smart-glasses count.

## Historical gap resolved

Epson's own Moverio SDK compatibility matrix names BT-350 and BT-30E as distinct supported products alongside the already-canonical generations. First-party product/launch material confirms that they were not documentation aliases:

- **BT-350** was a distinct enterprise/fleet smart-glasses product optimized for multi-user deployment.
- **BT-30E** was launched as a separate compact/light display-glasses product alongside the more rugged BT-35E branch.

Both therefore satisfy the same product-identity standard used for existing Moverio generations.

## Architecture boundaries

### Standalone Android generations

BT-100, BT-200, BT-300 and BT-350 contain substantially more onboard application/runtime responsibility than later display-peripheral products. App compatibility, Android version, camera/sensor access, storage and developer tooling must remain generation-specific.

### Tethered display generations

BT-30C, BT-30E, BT-35E, BT-40/40S and BT-45C/45CS shift varying amounts of compute to an attached controller or host. Similar display modules do not make their connector, camera, ruggedization, controller bundle, or field-service behavior interchangeable.

### Bundle naming

BT-40S and BT-45CS pair glasses with Epson controller hardware; GlassesResearch preserves the paired retail/system nomenclature without counting the controller bundle as a second glasses generation where the eyewear hardware is the same BT-40 or BT-45C family member.

## Completeness status

This audit resolves the most obvious omissions surfaced by Epson's surviving SDK/product documentation, but the manufacturer remains under historical review until regional/prototype naming and early Japan-market material are collision-checked against the complete ledger.

Priority work:

1. recover exact first-sale years and regional model numbers for BT-350 and BT-30E;
2. map controller variants and whether any `S` suffix ever implies different eyewear hardware;
3. preserve Moverio SDK/API support by generation rather than by brand;
4. recover archived retail and enterprise acquisition evidence for discontinued products;
5. check additional Japan-only Moverio variants and accessories for false model inflation or genuine generations.

## Primary sources

- [Moverio developer portal](https://tech.moverio.epson.com/)
- [Moverio software / SDK compatibility](https://tech.moverio.epson.com/en/software_updates/)
- [Epson Moverio BT-350 product/support family](https://epson.com/moverio)
- [Epson Moverio BT-35E](https://epson.com/en/For-Work/Wearables/Smart-Glasses/Moverio-BT-35E-Smart-Glasses/p/V11H935020)

## Related GlassesResearch resources

- [Manufacturer Completeness](../docs/MANUFACTURER_COMPLETENESS.md)
- [Adjacent Wearable-HCI Catalog](../models/ADJACENT_WEARABLES.md)
- [The List](../models/THE_LIST.md)
- [Wave 01 manufacturer audit](../research/investigations/MANUFACTURER_COMPLETENESS_WAVE_01_2026-09-05.md)
