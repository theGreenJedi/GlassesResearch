# EV-0051 — Replaceable power and modular-parts wave one

- **Captured:** 2026-08-14
- **Scope:** Vuzix M400/M4000/LX1, Solos AirGo A5-compatible products, and Oakley Meta HSTN
- **Evidence class:** current first-party product, support, accessory, and safety documentation
- **Purpose:** separate externally replaceable power modules and modular electronics from sealed batteries, while recording current retail availability.

## Findings

| Product | First-party fact | Ownership / repair consequence |
|---|---|---|
| Vuzix M400 / M4000 | Vuzix support states these products require an external battery for normal operation and support true hot swapping because a small internal bridge battery keeps the device alive briefly. Vuzix also documents that a suitable 1.5 A source can power them. Current 3200 mAh and 4800 mAh rail-mounted packs are listed as M-Series compatible. | The main runtime battery is an **owner-replaceable, currently purchasable power module**. The small internal bridge cell is not thereby proven replaceable. |
| Vuzix LX1 | The current product lists a 7000 mAh long-shift clip-in battery, an available multi-battery charger, and an easy-release mounting system. Vuzix's current accessory catalog lists the LX1 long-shift power bank and charger kit. | The runtime battery is an **owner-removable retail module**; this materially improves shift continuity and aging survival. It does not prove field replacement of internal electronics. |
| Solos AirGo A5 kit | Solos currently sells a temple kit whose modules attach to compatible AirGo 3 frame fronts. The product family also documents swappable front frames/lenses. | Certain electronics-bearing temples are **owner-removable and separately purchasable**, so a failed or upgraded temple need not force optical-front replacement. Compatibility must be checked by generation. |
| Oakley Meta HSTN | Oakley's FAQ and safety guide state that the embedded batteries in the glasses and charging case cannot be replaced and are not user-replaceable. Oakley separately sells lenses/accessories. | Optical consumables and accessories do not offset the **sealed, manufacturer-controlled battery path**. Battery aging can retire otherwise functional electronics. |

## Classification rules

1. Hot-swappable external power is strong battery serviceability even when a small internal bridge cell remains sealed.
2. A removable runtime battery does not prove replacement of every battery inside the device.
3. A retail temple kit proves modular service only for listed compatible generations.
4. A sold accessory is current parts availability; a historical manual alone is preservation evidence, not a current purchase route.
5. Replaceable lenses, chargers, cases, or nose pieces must not inflate the battery or board-repair classification.

## Primary sources

- Vuzix external-battery support: https://support.vuzix.com/docs/external-battery
- Vuzix M400: https://www.vuzix.com/products/m400-smart-glasses
- Vuzix 3200 mAh M-Series battery: https://www.vuzix.com/products/3200mah-xtreme-weather-power-bank
- Vuzix 4800 mAh M-Series battery: https://www.vuzix.com/products/4800mah-extended-use-power-bank
- Vuzix LX1: https://www.vuzix.com/products/vuzix-lx1-smart-glasses
- Vuzix accessories: https://www.vuzix.com/collections/accessories
- Solos AirGo A5 Temple Kit: https://solosglasses.com/products/temple-kit-solos-airgo%E2%84%A2-a5
- Oakley Meta FAQ: https://www.oakley.com/en-us/oakley-meta-faq
- Oakley Meta safety/warranty guide: https://media.oakley.com/LegalPDFs/OakleyMeta/OakleyMeta_AIGlasses_SafetyWarrantyGuide.pdf

## Remaining validation

- Determine whether Vuzix supplies or services the M400/M4000 internal bridge cell.
- Capture exact LX1 battery insertion/removal instructions and whether operation survives a live swap.
- Track Solos temple-kit compatibility, stock, firmware pairing, and whether camera/battery temples can be independently purchased for newer generations.
- Obtain manufacturer/depot battery-replacement pricing and end-of-life policy for Meta/Oakley products.
