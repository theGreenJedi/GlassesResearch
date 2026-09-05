# Rokid historical model audit — 2026-09-05

## Scope

This audit reconstructs Rokid's eyewear/product lineage from first-party corporate milestones, current product/security documentation, developer material, surviving regional product pages, and contemporaneous launch records. It collision-checks those identities against the canonical GlassesResearch ledger and preserves bundles, co-brands, and non-eyewear wearables separately.

The governing rule is unchanged: **a model is admitted only when a distinct marketed hardware identity and a documented paid acquisition/procurement path are established.** Bundles do not inflate the eyewear count, and manufacturer naming drift is preserved as aliases rather than silently normalized.

## Primary chronology

Rokid's current corporate milestone page documents the following sequence:

- 2018 — Rokid Glass 1, all-in-one AR glasses.
- 2020 — Rokid Glass 2, split-type monocular optical-waveguide AR glasses.
- 2020 — X-Craft, industrial 5G explosion-proof MR product.
- 2021 — Rokid Air, consumer AR glasses.
- 2021 — Rokid Air Pro, AR glasses for exhibition/cultural-tourism use.
- 2023 — Rokid Max.
- 2023/2024 — Rokid AR Studio system, whose eyewear component is Rokid Max Pro.
- 2024 — Rokid AR Lite system, Max 2 + Station 2.
- 2024/2025 — Rokid Glasses, integrated display-AI eyewear.
- 2025/2026 — display-free Rokid AI Glasses, currently marketed globally as Style and regionally as Neo.
- 2026 — Rokid Glass 3 enterprise eyewear.

Primary chronology source: https://www.rokid.com/en-US/about

## Canonical collision check

Already present before this audit:

| Product | Existing ID | Audit disposition |
|---|---|---|
| Rokid Glass / Glass 1 | GLS-0061 | keep; historical enterprise standalone-AR branch |
| Rokid Glass 2 | GLS-0062 | keep; correct era to 2020 |
| Rokid AI Glasses | GLS-0063 | keep; reconcile to display-free RV203 / Style / Neo naming rather than creating a duplicate |
| Rokid Glasses | GLS-0064 | keep; integrated display-AI product |
| Rokid Air | GLS-0092 | keep |
| Rokid Max | GLS-0093 | keep |
| Rokid Max 2 | GLS-0094 | keep |

## New canonical admissions

### GLS-0182 — Rokid Air Pro

**Disposition:** admit as a distinct smart-glasses model.

Evidence supporting separate identity:

- Rokid's own corporate history names Air Pro separately from Air and gives an October 2021 release.
- Rokid's developer forum states that the UXR SDK supports both Air and Air Pro and explicitly distinguishes them: Air Pro adds cameras, while Air has myopia adjustment that Air Pro lacks.
- Surviving commercial/enterprise channels offer Air Pro as a separately orderable model.

This is therefore not an accessory package or cosmetic SKU. Its camera and optical differences are material to capability, privacy, Visual AI, and report-card treatment.

Primary/technical source: https://forum.rokid.com/post/detail/365

### GLS-0183 — Rokid Max Pro

**Disposition:** admit as a distinct smart-glasses model.

Evidence supporting separate identity:

- Rokid AR Studio's developer site identifies **Rokid Max Pro** as the eyewear component of the AR Studio system.
- Max Pro has model-specific hardware/behavior, including 6DoF support and camera-assisted spatial interaction when paired with Station Pro.
- Contemporaneous launch reporting records Max Pro and Station Pro as separately priced components of AR Studio rather than an unchanged Max bundle.
- Rokid's current security-support table lists Max Pro separately with hardware model `RA202`.

AR Studio remains a system/bundle identity; **Max Pro is the eyewear model**.

Primary source: https://arstudio.rokid.com/

### GLS-0184 — Rokid Glass 3

**Disposition:** admit as a distinct current enterprise smart-glasses model.

Evidence supporting separate identity:

- Rokid's current developer documentation explicitly targets **Rokid Glass 3** hardware and publishes a dedicated glasses-side + phone-side SDK demo workflow.
- Rokid's current enterprise manual names Glass 3 and publishes generation-specific hardware/software behavior.
- Rokid's security center lists Glass 3 separately with model numbers `RG301` / `RG303`, release date 2026-06-29, and an active support horizon.
- Current regional enterprise channels document orderability.

Glass 3 is therefore neither an alias of Glass 2 nor merely the enterprise name for Rokid Glasses.

Primary sources:
- https://x-docs.rokid.com/docs/en/downloads/demo-guide.html
- https://global.rokid.com/pages/security-center

## Existing-ID correction — GLS-0063

The previous canonical description (`Rokid AI Glasses`, 2024, region-limited camera/audio) was under-resolved. Current first-party evidence now supports a cleaner identity:

- Rokid's security-support table identifies **Rokid Ai Glasses** model `RV203` as a display-free AI-glasses product.
- Current global product pages market the display-free hardware as **Rokid AI Glasses Style**.
- Current regional pages also use **Rokid AI Glasses Neo** / **Neo (Style)** for the same display-free architecture.
- The current product page preserves the same 38.5 g class, AR1/RT600 compute, 12 MP Sony IMX681 camera, 32 GB storage, Wi-Fi 6, Bluetooth 5.3, open-ear audio, and four-microphone array.

Disposition: keep stable ID `GLS-0063`; update real-world nomenclature and era/status rather than minting a duplicate canonical ID.

Primary sources:
- https://global.rokid.com/pages/security-center
- https://global.rokid.com/products/rokid-ai-glasses-style

## Non-GLS dispositions

### Rokid X-Craft — ADJ-0010

**Disposition:** adjacent wearable, not smart-glasses count.

Rokid markets X-Craft as an industrial explosion-proof MR device, while its own video/product language describes an AR **headband** intended to mount with industrial protective headgear. The current German B2B store retains separately orderable 5G/Wi-Fi and ATEX/standard variants. Because the physical interface is helmet/headband-mounted rather than fundamentally eyeglass-frame eyewear, X-Craft belongs in the Adjacent Wearable-HCI Catalog.

Primary/current source: https://de.rokid.com/de-de/products/rokid-x-craft-for-b2b

### Rokid AR Studio

System identity: **Max Pro + Station Pro**. Preserve as a system investigation and lineage node, but do not count it in addition to Max Pro.

### Rokid AR Lite / current Rokid AR Spatial

System identity: **Max 2 + Station 2**. Preserve as system/bundle identity; Max 2 is the eyewear model.

### Rokid AR Joy / Joy 2

Station-based entertainment bundle. Preserve bundle/system identity; do not create another eyewear row when the glasses are unchanged Max/Max 2 hardware.

### Rokid AI Glasses Style Pack

Retail/power configuration of GLS-0063. No new eyewear identity.

### Bolon AI Glasses — RV201 / RV202

Rokid's current security table distinguishes Bolon AI Glasses model numbers `RV201` / `RV202`, and 2025 launch reporting confirms a separately branded display-free Bolon/Rokid product family. Available evidence also shows a very close shared platform relationship with Rokid's display-free AI glasses: similar AR1 compute, 38.5 g class, camera/audio feature set, and shared software ecosystem.

Disposition for this pass: **registry/lineage variant, not a separate GLS row yet**. GlassesResearch's canonical rule does not count an unchanged co-brand/frame treatment as a new model. Promote only if further evidence establishes materially distinct hardware beyond frame/brand/configuration differences.

## Count effect

Canonical active smart-glasses count: **180 → 183**

New canonical IDs:

- `GLS-0182` Rokid Air Pro
- `GLS-0183` Rokid Max Pro
- `GLS-0184` Rokid Glass 3

Adjacent wearable count adds:

- `ADJ-0010` Rokid X-Craft

## Follow-up evidence priorities

1. Recover first-party Air Pro manual / archived product sheet and exact regulatory model number.
2. Capture Max Pro / Station Pro manuals and separate glasses-vs-host specifications.
3. Preserve Glass 3 manual, SDK demo, Android/YodaOS details, and model-number evidence.
4. Resolve RV203 versus RV201/RV202 mechanical/electrical differences before deciding whether Bolon AI Glasses deserves a separate canonical row.
5. Add report cards for Air Pro, Max Pro, and Glass 3 only from generation-specific evidence; do not inherit Air/Max/Rokid Glasses scores.
6. Preserve X-Craft ATEX/IECEx variant boundaries and treat certifications as variant-specific.
