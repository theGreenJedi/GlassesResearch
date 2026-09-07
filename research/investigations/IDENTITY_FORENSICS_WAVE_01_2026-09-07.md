# Identity Forensics — Wave 01

**Date:** 2026-09-07  
**Scope:** unresolved purchaser-history and model-identity records surfaced by the current candidate ledger.

This investigation separates two different kinds of stale state: a candidate that has now crossed the canonical acquisition threshold, and a marketplace lead whose product identity can be narrowed materially without yet claiming a complete OEM/regulatory lineage.

## Halliday G2 — acquisition threshold crossed

The candidate ledger previously kept Halliday G2 outside the canonical purchaser-history ledger because only a refundable Priority Access reservation was available and the manufacturer said actual preorders would open later.

That condition has changed.

Halliday now exposes a direct manufacturer product page with:

- **Halliday G2** as the named product;
- **USD $599** price;
- an **Add to cart** purchase path;
- first-batch shipment estimates beginning **September 15, 2026** for non-prescription orders;
- a published specification sheet identifying a **binocular waveguide display**, **dual microLED optical engines**, **600 × 300 pixels per eye**, **25.2° FOV**, **49 g** weight and **210 mAh** battery;
- current support documentation describing active G2 preorders and order modification, tracking and fulfillment behavior.

Primary evidence:

- https://www.hallidayglobal.com/products/halliday-g2
- https://support.hallidayglobal.com/hc/en-us/articles/60154389484825-General-FAQs

**Disposition:** admit Halliday G2 as the next canonical purchaser-history model. The acquisition threshold is satisfied by an actual manufacturer preorder/purchase path, not merely a refundable priority reservation.

**Evidence boundary:** purchaser-history admission does not verify Halliday's performance claims, privacy claims, subscription value, battery-life claim or owner-control implications. G2 does not inherit Report Card scores from `GLS-0049`.

## Coucur Amazon ASIN B0GTYKGR5X — product identity narrowed to M01

The candidate ledger currently describes Amazon ASIN `B0GTYKGR5X` as an unresolved Coucur 8 MP camera-glasses offer. Multiple independent commercial mirrors now expose a stable model identity for that exact ASIN:

- **Model number: M01**;
- **Manufacturer: Shenzhen Buzz Tech CO., LTD.**;
- **8 MP camera / 1080P video**;
- **270 mAh battery**.

A separate Coucur M01 user-manual record independently describes the M01 as an 8 MP / 1080P smart-glasses product using the **HeyCyan** companion app and a **270 mAh** battery. Those attributes line up with the exact-ASIN mirrors and materially narrow the identity.

Evidence:

- Exact-ASIN commercial mirror: https://www.ubuy.co.th/en/product/U0RBCFNYC-ai-smart-glasses-with-camera-8mp-4k-camera-glasses-1080p-video-recording-glasses-chatgpt-voice-assistant-139-languages-real-time-translation
- Exact-ASIN commercial mirror: https://tiendamia.com.uy/p/amz/b0gtykgr5x/coucur-lentes-inteligentes-ai-con-camara-gafas-de-camara-4k
- M01 manual record: https://manuals.plus/asin/B0FC69VC4T

The currently sold Coucur **G1** is not the same identity: Coucur's present G1 material advertises different stabilization, battery/case and current-generation specifications. Do not collapse M01 into G1 merely because both are Coucur camera glasses.

**Disposition:** change the forensic assessment from "model number unresolved" to **Coucur M01 strongly indicated / exact-ASIN identity resolved at model-name level**. Keep the candidate on an evidence hold for a separate canonical admission until regulatory identifier, full OEM/rebrand topology and acquisition-history evidence are packaged cleanly enough for the ledger.

## OICIIDO / Ear Dance note

The current OICIIDO Walmart lead remains appropriately held rather than admitted as a separate model. Public OICIIDO manuals confirm that multiple OICIIDO products use the **Ear Dance** app, including a documented **KM03** identity, while the canonical `GLS-0157` W100/Ear Dance ecosystem has strong OEM evidence for W100 hardware using the same app. App commonality alone is not hardware identity. Continue to resolve frame geometry, Bluetooth identity, battery/chipset and exact seller variant before aliasing the Walmart listing to W100 or KM03.

## Outcome

- **Canonical admission:** Halliday G2 → `GLS-0218`.
- **Identity resolution, no admission yet:** Coucur ASIN `B0GTYKGR5X` → **M01** strongly established; OEM/regulatory lineage still open.
- **Hold preserved:** OICIIDO Walmart `16914411854`; Ear Dance app evidence alone does not prove W100/KM03 hardware identity.
