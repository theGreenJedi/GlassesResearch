# Dymesty comparison discovery audit — 2026-08-17

Source reviewed: Dymesty, “Smart Glasses Comparison Chart 2026.” Dymesty is used here as a discovery surface, not specification authority. Every disposition below was reconciled against the canonical ledger and independent evidence.

## Final dispositions

| Lead | Final disposition |
|---|---|
| Brilliant Labs Halo | Already canonical as **GLS-0052**. |
| BooaBei AI Smart Glasses | Verified **W610 / HeyCyan** market identity; routes to **GLS-0039**, no additional model count. |
| Vital Smart Glasses | Verified **W100 / Ear Dance** market identity; routes to **GLS-0157**, no additional model count. |
| EarlySincere | W100-class audio/translation product is verified in the **W100 / Ear Dance** lineage and routes to **GLS-0157**. The exact Dymesty-described “4K camera” EarlySincere listing is not silently conflated with that audio product; absent stronger identity evidence it remains a commercial lead rather than a second model. |
| Halliday G2 | Distinct pre-release generation. As of 2026-08-17 Halliday sells priority access to a future preorder rather than the G2 product itself. Registry-only until the acquisition threshold is crossed. |
| RayNeo Air 3s | Already canonical as **GLS-0090**. |
| RayNeo Air 3s Pro | Already canonical as **GLS-0091**. |
| RayNeo Air 4 Pro | Distinct current purchasable generation; admitted as **GLS-0155**. |
| Thunderbird V3 / RayNeo V3 | One product identity, model **XRGF50**, not two models. Admitted once as **GLS-0154** with both market/corporate names preserved. |
| VITURE Luma | Already canonical as **GLS-0079**. |
| VITURE Luma Pro | Already canonical as **GLS-0080**. |
| VITURE Luma Ultra | Already canonical as **GLS-0081**. |
| VITURE Beast | Already canonical as **GLS-0082**. |
| XREAL One | Already canonical as **GLS-0074**. |
| XREAL One Pro | Already canonical as **GLS-0075**. |
| XREAL 1S | Distinct current purchasable generation; admitted as **GLS-0156**. |
| IOOIOO AI Smart Glasses | Commercial listing is real, but targeted searches did not establish a durable model number, manufacturer/OEM lineage, manual, or certification identity. Retain as a commercial discovery lead; no GLS ID. |

## Follow-on lineage findings from the same investigation

The alias-resolution search exposed two important commodity houses:

- **W100 / Ear Dance** — now canonical once as GLS-0157, with Vital, EarlySincere, Astrum W100, Tiglon TG-W100, LEEDOAR-associated W100 and other verified seller identities routed into it rather than counted separately.
- **W630 / HeyCyan** — now canonical once as GLS-0158, with Giinova W630 and GUHUAVMI W630 routed into it rather than counted separately.

It also exposed separately named HeyCyan sibling platforms **W611/W611 Pro, W620, W640 and W650**. Shared HeyCyan software or JL7018F/V821-family silicon is not sufficient to collapse those products into W610. They remain explicit follow-on model candidates for independent admission/duplicate checks.

## Discovery and UX lesson

The Dymesty page did two useful things for GlassesResearch: it exposed catalog/discovery gaps and demonstrated a more readable presentation pattern. PR #303 implemented the abbreviated, category-first comparison surface while preserving evidence depth on demand. PRs #303 and #304 also introduced a market-identity resolver so a visitor can search the name printed on a box and be routed to the underlying canonical model/lineage without inflating the canonical count.
