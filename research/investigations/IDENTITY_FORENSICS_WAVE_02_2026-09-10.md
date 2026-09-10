# Identity Forensics — Wave 02

**Date:** 2026-09-10  
**Scope:** continue catalog completeness work from the 2026-09-07 identity-forensics and competitor-completeness passes. This note records the forensic evidence and final Wave 02 dispositions; canonical propagation is controlled by the accompanying reconciliation packet.

## Baseline

The current canonical ledger contains **236 active smart-glasses records**. Earlier references to 216 are historical snapshots unless they are presented as a current count. The purpose of this wave is to find identities that the internally consistent ledger still misses, while preserving the purchaser-history admission boundary and avoiding style/variant inflation.

## Finding 1 — RealWear Arc 3 is a clean catalog omission

**Final disposition: admit.**

The current GlassesResearch RealWear population stops at HMT-1, HMT-1Z1, Navigator 500, Navigator 520, and Navigator Z1. RealWear now directly sells a sixth named headset, **RealWear Arc 3**, and the current canonical list does not contain it.

Primary evidence:

- RealWear's current hardware page names Arc 3 and routes users to `SHOP NOW`: https://www.realwear.com/devices/hardware
- RealWear's first-party shop lists Arc 3 alongside Navigator 520 and Navigator Z1, starting at USD $2,950: https://shop.realwear.com/
- The direct Arc 3 product page exposes a live `Add to cart` purchase route: https://shop.realwear.com/products/realwear-arc-3
- RealWear support identifies the hardware model as **A31G**: https://support.realwear.com/knowledge/arc3/specifications
- RealWear firmware documentation independently repeats **RealWear Arc 3 (A31G)**: https://support.realwear.com/knowledge/realwear-arc-3-firmware-release-1.0-release-notes

### Identity boundary

Arc 3 is not a Navigator 520 cosmetic variant. RealWear documents a separate see-through full-color micro-OLED architecture, Snapdragon 662 platform, dual-camera system, different chassis and the model identifier A31G. The purchaser-history threshold is crossed directly by the current first-party cart.

**Canonical action:** admit as `GLS-0238`. Arc Base, thermal modules, support plans and other accessories remain non-eyewear accessories rather than separate smart-glasses identities.

## Finding 2 — Iristick Z1 → G1 chronology is now resolved

**Final disposition: Z1 is the former market name of G1; do not mint a separate Z1 row.**

The earlier ambiguity came from secondary snippets that alternately described Z1 as becoming G1 or G1 Pro. A contemporaneous Iristick press release resolves the boundary more cleanly. It states that **Iristick.G1 was formerly on the market as Iristick.Z1**, while separately listing **Iristick.G1PRO** as an available product from May 2021. The same release treats G1 and G1 PRO as members of the product portfolio rather than saying Z1 became G1 PRO.

Contemporaneous evidence:

- Iristick April 27, 2021 press release, preserved by the EU Innovation Fund: https://innovationfund.eu/wp-content/uploads/2021/04/2021-04-27-IRI-PRESS-RELEASE-Iristick.H1-launch-april2021_final.pdf
- Display Daily's May 2021 reproduction likewise carries the heading `Iristick.Z1 becomes Iristick.G1` and describes G1 PRO as the additional feature tier: https://displaydaily.com/introducing-iristick-g1-iristick-h1-visor-ex01/
- Iristick's surviving March 2021 G1 specification: https://iristick.com/uploads/files/IRI-spec-sheet-Iristick.G1-32021-EU-final.pdf
- Iristick's regulatory booklet continues to identify G1 (PRO) and preserves the shared G-series hardware/serial format: https://docs.iristick.com/assets/RWS-Iristick.G2-H1.pdf

Independent archival confirmation that Z1 was a real acquired/deployed product also survives in Médecins Sans Frontières' Unicat catalog, which preserves the Iristick Z1 as an outdated field-procurement item and links the later Iristick G1 article: https://www.unicat.msf.org/cat/product/76445

### Alias result

`Iristick.Z1` should be preserved as a historical alias / former market name for the base **Iristick.G1** identity. It should not consume a third canonical ID.

## Finding 3 — Iristick G1 and G1 PRO qualify as two marketed product identities

**Final disposition: admit G1 and G1 PRO separately; preserve shared-hardware evidence.**

Iristick's March 2021 specification presents **IRISTICK.G1** and **IRISTICK.G1 PRO** side by side. Both share the same 77 g chassis, 428 × 240 display, cameras, 6× optical zoom, pocket unit and core hardware. The PRO tier adds multilingual voice commands and advanced barcode scanning. That means the evidence supports a common hardware platform with a separately marketed PRO configuration rather than two unrelated electronics generations.

The purchaser-history boundary is nevertheless satisfied for both marketed identities:

- Iristick's April 2021 press release explicitly states that **Iristick.G1, Iristick.G1PRO and Iristick.H1 are available from May 2021**.
- Iristick's product specification explicitly names and distinguishes G1 and G1 PRO.
- Iristick's current Wizzeye software still names **G1 PRO** as a supported voice-command product.
- Public trade records preserve a shipped `Complete Set G1 Pro For iOS Devices` and separate Iristick.G1 shipments from Iristick NV, corroborating real enterprise acquisition rather than a paper-only feature label: https://www.volza.com/company-profile/iristick-nv-42644538/export/

The current canonical catalog already treats the later **G2** and **G2 PRO** as separate marketed identities (`GLS-0116` / `GLS-0117`) even though they likewise occupy a shared product family. Applying the same ruler to the documented G1 pair avoids an arbitrary generation-specific inconsistency.

**Canonical action:**

- `GLS-0239` — Iristick G1, with **Iristick Z1** preserved as historical alias/former market name.
- `GLS-0240` — Iristick G1 PRO, explicitly described as the common G1 platform with PRO voice/barcode feature tier rather than an independently proven new electronics architecture.

## Finding 4 — current Iristick coverage is otherwise aligned

Iristick's current first-party shop sells G2 PRO and G3, with H1 preserved in the supported product family. Those identities already exist in GlassesResearch as GLS-0117, GLS-0119, and GLS-0118 respectively; no duplicate admission is warranted.

Current first-party documentation also continues to identify G2 PRO, G3 and H1 as the active comparison set: https://docs.iristick.com/smart-glasses/specifications/

Iristick's pricing material lists an **H3 COMING SOON** with no demonstrated paid purchase route. H3 therefore remains a discovery/watch identity only at this stage, not a canonical purchaser-history admission.

## Count-hygiene observation

The repository's current canonical profile documentation says 236 active records. The manufacturer-completeness document contains a legitimate historical statement that Wave 02 advanced the count from 193 to 216; that historical sentence should **not** be globally replaced. Any public page still presenting 216 as the *current* count should instead be traced back to its generator/source and fixed there.

## Wave 02 disposition summary

| Identity | Result | Reason |
|---|---|---|
| RealWear Arc 3 / A31G | **Admit — GLS-0238** | Current first-party product, model-number support evidence and direct cart; distinct RealWear architecture. |
| Iristick G1 | **Admit — GLS-0239** | First-party product specification plus contemporaneous availability statement; former Z1 market name resolved. |
| Iristick G1 PRO | **Admit — GLS-0240** | Separately marketed PRO product with documented feature differentiation and acquisition evidence. |
| Iristick Z1 | **Alias of G1** | Iristick's contemporaneous release explicitly says G1 was formerly marketed as Z1. |
| Iristick H3 | **Watch / pre-release** | Announced/coming-soon identity without a demonstrated paid acquisition route. |

## Evidence boundary

These decisions establish identity and purchaser history. They do **not** convert manufacturer technical specifications into independently verified performance, and the G1/G1 PRO split must not be described as proof of different core hardware. The evidence instead shows a common G1 platform with a separately marketed PRO feature tier.

## Wave closeout

The two blockers that opened Wave 02 are now adjudicated: Arc 3 has a clean current identity/acquisition path, and the Iristick Z1/G1/G1 PRO rename problem has been resolved without inventing a third Z1 identity. The accompanying reconciliation packet may now propagate three admissions through the normal mechanical catalog pipeline.
