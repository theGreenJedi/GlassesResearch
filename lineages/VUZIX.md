---
description: "Vuzix smart-glasses lineage across consumer video eyewear, Wrap and STAR AR, enterprise Android wearables, host-driven M400-C, Z100, and adjacent wearable displays."
---
# Vuzix smart-glasses lineages

**Whole-manufacturer audit:** 2026-09-05  
**Audit packet:** [Manufacturer Completeness Wave 02](../research/investigations/MANUFACTURER_COMPLETENESS_WAVE_02_2026-09-05.md)

Vuzix spans almost the full history of wearable displays: early monocular industrial displays, consumer video eyewear, tracked VR/AR glasses, Android enterprise wearable computers, host-driven enterprise peripherals, waveguide safety glasses and modern phone-peripheral displays. GlassesResearch therefore tracks Vuzix as a **corporate lineage with multiple technical branches**, not as one homogeneous hardware platform.

## 1. Pre-Wrap consumer video-eyewear branch — 2003–2009

First-party SEC filings establish that Vuzix sold monocular **M920** products from 2003–2009 and, by 2009, four consumer binocular iWear-era products: **AV230 XL, AV310 widescreen, AV920 and VR920**. Vuzix describes the binocular products as two-microdisplay systems mounted to frames with eyeglass-style temples and sold for mobile, hands-free private video viewing.

Canonical Wave 02 additions:

- `GLS-0195` — M920
- `GLS-0196` — AV230 XL
- `GLS-0197` — AV310 widescreen
- `GLS-0198` — AV920
- `GLS-0199` — VR920

VR920 adds head tracking and developer/gaming behavior; it is not merely a color/fit variant of AV920.

## 2. Wrap / STAR consumer display and AR branch — 2009–2015

Vuzix calls Wrap its fourth generation of consumer Video Eyewear and documents a succession of differently resolved, tracked, camera-equipped and see-through models. These products are in scope for the same reason XREAL, VITURE, Rokid and RayNeo host-driven display glasses are in scope: they are eyewear-form near-eye displays sold for use with external hosts.

Canonical identities:

- `GLS-0200` — Wrap 230
- `GLS-0201` — Wrap 310XL
- `GLS-0202` — Wrap 920
- `GLS-0203` — Wrap 920VR
- `GLS-0204` — Wrap 920AR
- `GLS-0205` — Wrap 1200
- `GLS-0206` — Wrap 1200VR
- `GLS-0207` — STAR 1200
- `GLS-0208` — Wrap 1200DX
- `GLS-0209` — Wrap 1200DX VR
- `GLS-0210` — Wrap 1200DX-AR
- `GLS-0211` — STAR 1200DX

The DX generation introduces HDMI-era connectivity; VR members add tracking; AR members add cameras and/or see-through presentation. Those are material architecture/function boundaries, not fashion SKUs.

## 3. Early waveguide/enterprise transition

Vuzix began selling the hardhat/goggle-mounted **M2000AR** in late 2013 and M100 in early 2014. M2000AR belongs in the adjacent head-worn catalog because the manufacturer explicitly describes it as mounted to hardhats or goggles. M100 is conventional enough in role/form to remain canonical eyewear.

Existing canonical enterprise chronology:

- `GLS-0095` — M100
- `GLS-0096` — M300
- `GLS-0097` — M300XL
- `GLS-0098` — M400
- `GLS-0099` — M4000
- `GLS-0100` — LX1
- `GLS-0121` — Shield

### M400-C host-driven split

`GLS-0212` — **M400-C** uses the M400-style eyeglass-mounted camera/display hardware but moves application compute to a USB-C host. That architectural split materially affects Software, Owner Control, Cloud Independence and Hackability; M400 scores must not be inherited.

## 4. Z100 / Ultralite peripheral-display branch

**Relationship type:** corporate + protocol/software lineage  
**Confidence:** Confirmed

`GLS-0056` — **Z100** is a phone-peripheral display. The paired phone performs application processing and sends instructions over Bluetooth. Vuzix provides Android and iOS development paths for this branch.

## 5. Android standalone wearable-computer branch

M400, M4000, Blade 2, LX1 and Shield are standalone devices that can run applications on the glasses. Vuzix documentation exposes standard Android APIs plus Vuzix SDKs for speech, barcode scanning, connectivity and HUD-oriented interfaces.

Model chapters:

- [M400 / M4000](../models/VuzixM400/README.md)
- [Blade 2](../models/VuzixBlade2/README.md)
- [Shield](../models/VuzixShield/README.md)
- [LX1](../models/VuzixLX1/README.md)

The Connectivity SDK supports communication between Android phone applications and applications running on supported Vuzix Android devices. Vuzix also publishes HUD Action Menu resources and Vuzix View deployment/debug tooling.

## 6. Adjacent Vuzix wearable-HCI products

These products are real and historically important but are not fundamentally eyeglass frames:

- `ADJ-0013` — **Tac-Eye** — rugged monocular clip-on for ballistic eyewear, headsets or safety goggles.
- `ADJ-0014` — **M2000AR** — industrial waveguide HMD mounted to hardhats/goggles.
- `ADJ-0015` — **iWear Video Headphones** — headphone/visor VR and video device, shipping from December 2015.
- `ADJ-0016` — **Smart Swim** — AR display attachment for swim goggles.

This routing is important: manufacturer history is preserved without allowing every head-worn display to inflate the smart-glasses count.

## 7. Historical identities still held back

- **M3000** — strong CES/development evidence, but Wave 02 did not recover sufficient commercial-acquisition evidence.
- **VidWear B3000 / AR3000** — announced/expected future products in 2016; no shipment/acquisition proof recovered.
- **iWear Wireless** — demonstrated prototype; no commercial shipment evidence recovered.
- **M300-C** — OEM identity remains entangled with Toshiba/Dynabook dynaEdge AR100 and requires collision resolution before any separate count.

## Why the branches stay separate

A Wrap 1200 is essentially host-driven display eyewear; Wrap 920AR adds camera/tracking; M400 runs Android on-device; M400-C moves compute to a wired host; Z100 pushes application processing to a phone over a peripheral protocol. Corporate ownership alone is therefore insufficient to transfer capabilities or scores between generations.

## Developer ecosystem signals

Primary documentation establishes standard Android development for the standalone branch; Vuzix Speech, Barcode, Connectivity and HUD resources; Wi-Fi/Bluetooth/BLE communication options; USB debugging and APK installation through Vuzix View on supported models; and Android/iOS development paths for Z100.

These are strong research signals, but GlassesResearch does not convert them automatically into report-card grades. Model-specific limits, licensing, cloud dependencies, bootloader/firmware access and real-world owner control still require evidence.

## Primary sources

- [Vuzix Developer Resources](https://support.vuzix.com/docs/developer-resources)
- [Vuzix support device index](https://support.vuzix.com/)
- [Vuzix corporate history](https://ir.vuzix.com/company-information/company-history)
- [Vuzix M400-C introduction](https://ir.vuzix.com/news-events/press-releases/detail/1937/vuzix-introduces-its-new-m400-c-smart-glasses)
- [2009 Vuzix filing — AV/VR products](https://ir.vuzix.com/reports-filings/all-sec-filings/content/0000950123-09-019891/0000950123-09-019891.pdf)
- [2011 Vuzix filing — Wrap/AR/VR](https://ir.vuzix.com/reports-filings/all-sec-filings/content/0001144204-11-019283/v217067_10k.htm)
- [2013 Vuzix filing — DX generation and sales channels](https://ir.vuzix.com/reports-filings/all-sec-filings/content/0001144204-14-021666/v372331_10k.htm)

## Related GlassesResearch layers

- [The List](../models/THE_LIST.md)
- [Model Registry](../models/CATALOG.md)
- [Adjacent Wearable-HCI Catalog](../models/ADJACENT_WEARABLES.md)
- [Manufacturer Completeness](../docs/MANUFACTURER_COMPLETENESS.md)
- [Open Development Resource Ledger](../hacking/OPEN_HACKING_RESOURCE_LEDGER.md)
