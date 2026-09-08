---
description: "MicroOLED ActiveLook Light AR lineage covering ENGO, Julbo EVAD-1, Cosmo Vision and ActiveLook Enterprise eyewear, with open BLE API and reference-platform boundaries."
---
# ActiveLook / MicroOLED Light AR Lineage

**Lineage audit:** 2026-09-07  
**Audit packet:** [Competitor Completeness Sweep](../research/investigations/COMPETITOR_COMPLETENESS_SWEEP_2026-09-07.md)

ActiveLook is MicroOLED's lightweight heads-up-display platform for eyewear. It is both an optical/electronic module family and an interoperability ecosystem: ActiveLook documents a Bluetooth Low Energy architecture, mobile SDKs, an open API, partner eyewear, and development/reference platforms.

A shared ActiveLook platform does **not** mean ENGO, Julbo, Cosmo and Enterprise glasses are identical hardware. Product identity and platform identity are tracked separately.

## Canonical eyewear population

- `GLS-0223` — ENGO 1 — legacy sport HUD
- `GLS-0224` — ENGO 2 — current sport HUD
- `GLS-0225` — ENGO3 — current sport HUD
- `GLS-0226` — Julbo EVAD-1 — legacy sport HUD
- `GLS-0227` — Cosmo Vision — legacy/current-unclear navigation HUD
- `GLS-0228` — ActiveLook Enterprise — current enterprise/developer HUD

Lens colors, frame colors, standard/large sizing and photochromic variants do not receive separate GLS identities absent evidence of materially different electronics generations.

## Platform architecture

ActiveLook describes its technology as a compact near-eye display module with a low-power controller, graphical engine, gesture/light sensors and BLE transport. Its developer documentation says all ActiveLook glasses share the same open API interface, with mobile SDKs and an exposed BLE command/service model.

That is meaningful openness at the application/protocol layer. It does **not** establish open firmware, bootloader access, unrestricted hardware modification, or cloud independence for every application built on top of the platform.

Primary architecture: https://www.activelook.net/pages/the-tech  
Developer onboarding: https://www.activelook.net/news-blog/developing-with-activelook-getting-started

## Evolution

### Julbo EVAD-1

EVAD-1 is preserved as the first commercial ActiveLook sport-eyewear identity. ActiveLook announced it as available for sale in 2021.

### ENGO 1 → ENGO 2 → ENGO3

ENGO is MicroOLED's own sports-eyewear brand within the ActiveLook ecosystem. ENGO 2 had a documented paid first-run preorder in 2022; ENGO3 is the current retail generation. The generation sequence is a corporate/product lineage, but product-specific battery, optics, fit and compatibility claims remain generation-bound.

### Cosmo Vision

Cosmo Vision applied the ActiveLook platform to cycling navigation/performance eyewear. The surviving manufacturer page is now sold out, so GR treats the product as historical commercial evidence rather than assuming current availability.

### ActiveLook Enterprise

Enterprise adapts the platform to industrial/developer workflows. The current ActiveLook store sells the named unit directly and describes it as an AR development/deployment platform.

## Reference designs and non-canonical relatives

MicroOLED, Quanta Computer and STMicroelectronics announced an ActiveLook-enabled reference design in 2025. It remains a platform/reference design, not a purchaser-history eyewear identity. Similarly, developer kits and sample units are ecosystem artifacts unless they establish a separately marketed glasses product.

Reference-design source: https://www.activelook.net/news-blog/microoled-quanta-computer-and-stmicroelectronics-partner-to-deliver-reference-design-foractivelook-enabled-augmented-reality-smart-glasses

## Research priorities

- capture the exact firmware/API behavior of current ENGO3 and Enterprise hardware;
- test whether open-API applications can operate indefinitely without ActiveLook-hosted services;
- preserve firmware/update and app compatibility over time;
- reconstruct exact first/last retail dates for ENGO 1, EVAD-1 and Cosmo Vision;
- watch new ActiveLook partner eyewear without converting reference designs or lens variants into duplicate models;
- investigate repairability, battery replacement and optical-module serviceability;
- map upstream MicroOLED display/module revisions where they materially change shipping eyewear.

## Primary sources

- [ActiveLook technology](https://www.activelook.net/pages/the-tech)
- [ActiveLook consumer eyewear](https://www.activelook.net/pages/for-consumers)
- [ActiveLook store](https://shop.activelook.net/)
- [ENGO eyewear](https://us.engoeyewear.com/)
- [Cosmo Vision](https://cosmoconnected.com/en/products/cosmo-vision)

## Related research

- [The List](../models/THE_LIST.md)
- [Competitor Completeness Sweep](../research/investigations/COMPETITOR_COMPLETENESS_SWEEP_2026-09-07.md)
- [Community & Development](../resources/COMMUNITY_AND_DEVELOPMENT.md)
