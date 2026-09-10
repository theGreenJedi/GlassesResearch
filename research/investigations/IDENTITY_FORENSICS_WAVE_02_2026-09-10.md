# Identity Forensics — Wave 02

**Date:** 2026-09-10  
**Scope:** continue catalog completeness work from the 2026-09-07 identity-forensics and competitor-completeness passes. This note records evidence and dispositions only; it does **not** mint or retire canonical `GLS-####` identities by itself.

## Baseline

The current canonical ledger contains **236 active smart-glasses records**. Earlier references to 216 are historical snapshots unless they are presented as a current count. The purpose of this wave is to find identities that the internally consistent ledger still misses, while preserving the purchaser-history admission boundary and avoiding style/variant inflation.

## Finding 1 — RealWear Arc 3 is a clean catalog omission

**Disposition: admission candidate — high confidence.**

The current GlassesResearch RealWear population stops at HMT-1, HMT-1Z1, Navigator 500, Navigator 520, and Navigator Z1. RealWear now directly sells a sixth named headset, **RealWear Arc 3**, and the current canonical list does not contain it.

Primary evidence:

- RealWear's current hardware page names Arc 3 as an industrial smart-glasses product and routes users to `SHOP NOW`: https://www.realwear.com/devices/hardware
- RealWear's first-party shop lists Arc 3 alongside Navigator 520 and Navigator Z1, starting at USD $2,950: https://shop.realwear.com/
- The direct Arc 3 product page exposes a live `Add to cart` purchase route. The currently indexed configuration is USD $3,550 with three years of Service & Support: https://shop.realwear.com/products/realwear-arc-3
- RealWear's launch post says Arc 3 was launched on 2025-10-28 and was available to purchase immediately under a yearly subscription model: https://www.realwear.com/blog/realwear-arc-3
- RealWear support identifies the hardware model as **A31G** and documents the production firmware line: https://support.realwear.com/knowledge/arc3/specifications and https://support.realwear.com/knowledge/realwear-arc-3-firmware-release-1.0-release-notes

### Identity boundary

Arc 3 is not a Navigator 520 cosmetic variant. RealWear describes a separate hardware architecture: see-through full-color micro-OLED display, Snapdragon 662 platform, dual fixed cameras, distinct 175–179 g headband-style chassis, Ari OS launch platform, and model name A31G. RealWear also says Arc 3 **extends rather than replaces** its existing devices.

### Admission-ruler result

The purchaser-history threshold is crossed directly and unambiguously: first-party launch + immediate paid acquisition + current first-party cart. No marketplace inference is required.

**Recommended next action:** admit RealWear Arc 3 as a new canonical model after the normal profile / comparison / lineage propagation checks. Do not treat Arc Base, thermal modules, support plans, or other accessories as separate eyewear identities.

## Finding 2 — Iristick G1 / G1 PRO are missing historical identities, but the rename boundary needs one more archival pass

**Disposition: strong historical candidates; hold canonical admission until the Z1 → G1 / G1 PRO rename and acquisition evidence are packaged cleanly.**

The current GlassesResearch Iristick population begins with G2 / G2 PRO and then H1 / G3. Iristick's own surviving primary documentation establishes an earlier **Iristick.G1** generation and a **G1 PRO** configuration that are absent from the canonical ledger.

Primary evidence:

- Iristick still hosts a March 2021 product specification explicitly covering **IRISTICK.G1** and **IRISTICK.G1 PRO**: https://iristick.com/uploads/files/IRI-spec-sheet-Iristick.G1-32021-EU-final.pdf
- The specification distinguishes the PRO configuration from base G1: PRO receives multilingual/offline voice-command capability and the advanced barcode-scanning tier while both share the documented G1 chassis/platform characteristics.
- Iristick's current regulatory/warranty material continues to identify `Iristick.G1 (PRO)` alongside G2 (PRO) and H1: https://docs.iristick.com/assets/RWS-Iristick.G2-H1.pdf
- Current Iristick software documentation still names G1 PRO as a supported voice-command device: https://play.google.com/store/apps/details?id=app.wizzeye.app

Independent acquisition/deployment evidence:

- Wideum, an enterprise remote-assistance integrator, preserves an Iristick G1 unboxing and describes customer deployment of multiple Iristick units: https://wideum.com/en_us/iristick/
- Orange's IoT Journey catalog preserves an `Iristick.G1` product record in its XR-device catalog: https://iotjourney.orange.com/en/products/5192509b-1614075765
- Public trade-shipment data includes a `Complete Set G1 Pro For iOS Devices` shipment from Iristick NV to Bayer Turk and separate Iristick.G1 shipments: https://www.volza.com/company-profile/iristick-nv-42644538/export/

### Rename conflict that must not be guessed through

Surviving sources disagree on the exact historical naming transition:

- A 2021 report states **Iristick.Z1 becomes Iristick.G1**: https://displaydaily.com/introducing-iristick-g1-iristick-h1-visor-ex01/
- A preserved 2020 trade-publication entry says **Iristick Z1 smart glasses are now Iristick G1 Pro**: https://www.newequipment.com/home/company/55120160/72712

This may reflect a base/PRO renaming sequence rather than contradictory hardware, but the current evidence package is not sufficient to assert that. The old `Z1` identity should therefore be treated as an alias/lineage lead, not automatically as a third missing model.

### Identity boundary

The G1 and G1 PRO are manufacturer-documented names. Whether they deserve one or two canonical IDs depends on the site's existing generation/configuration rule. The present catalog already treats G2 and G2 PRO as separate canonical identities, so collapsing G1/G1 PRO without documenting why would be inconsistent. Conversely, the PRO differences currently visible could be software/feature-tier distinctions rather than a separate electronics generation. Preserve that uncertainty until historical sales literature or manuals establish the sold-SKU boundary.

**Recommended next action:** reconstruct the Z1/G1/G1 PRO commercial chronology from first-party or distributor archives, identify sold SKUs/model numbers if possible, then adjudicate base G1 and G1 PRO independently against the purchaser-history rule.

## Finding 3 — current Iristick coverage is otherwise aligned

Iristick's current first-party shop sells G2 PRO and G3, with H1 preserved as sold-out/legacy hardware. Current support pages likewise center G2 PRO, G3, and H1. Those identities already exist in GlassesResearch as GLS-0117, GLS-0119, and GLS-0118 respectively; no duplicate admission is warranted.

Primary current sources:

- https://shop.iristick.com/products
- https://docs.iristick.com/smart-glasses/
- https://iristick.com/pricing/

Iristick's pricing page also lists an **H3 COMING SOON** with no orderable purchase route. H3 is therefore a discovery/watch identity only at this stage, not a canonical purchaser-history admission.

## Count-hygiene observation

The repository's current canonical profile documentation says 236 active records. The manufacturer-completeness document contains a legitimate historical statement that Wave 02 advanced the count from 193 to 216; that historical sentence should **not** be globally replaced. Any public page still presenting 216 as the *current* count should instead be traced back to its generator/source and fixed there.

## Wave 02 disposition summary

| Identity | Result | Reason |
|---|---|---|
| RealWear Arc 3 / A31G | **Admission candidate** | Current first-party product, launch, support identity, price, and direct cart; distinct hardware branch. |
| Iristick G1 | **Strong hold / archival admission candidate** | Primary product specification + enterprise deployment evidence; sold-SKU/rename chronology needs closure. |
| Iristick G1 PRO | **Strong hold / archival admission candidate** | Manufacturer-documented PRO identity + shipment evidence; base-vs-PRO canonical boundary needs closure. |
| Iristick Z1 | **Alias/lineage investigation** | Sources disagree whether Z1 renamed to G1 or G1 Pro; do not mint a third identity without proof. |
| Iristick H3 | **Watch / pre-release** | First-party pricing page says coming soon and not yet orderable. |

## Next forensic targets

After Arc 3 propagation and Iristick archival closure, continue the manufacturer-completeness debt queue rather than re-auditing already monitored families. Highest-value next passes are Amazon Echo Frames, Bose Frames, Huawei smart eyewear, Xiaomi smart eyewear, Lenovo smart glasses, and the remaining RealWear/Iristick historical chronology. Special care is required where the current canonical catalog may be counting frame styles as separate electronics identities; completeness work can remove ambiguity as well as discover omissions.
