# The List Reconciliation — Rokid Historical Audit — 2026-09-05

## Decision

Whole-lineage review of Rokid's corporate history, developer documentation, security/support records, current product pages, and surviving commercial/procurement channels establishes **three previously missing smart-glasses models** and one adjacent industrial wearable.

The active canonical smart-glasses count advances from **180 to 183**.

## New canonical smart-glasses admissions

| ID | Maker | Model | Era | State | Type | Access basis | Identity basis |
|---|---|---|---:|---|---|---|---|
| GLS-0182 | Rokid | Air Pro | 2021 | enterprise / legacy-current availability mixed | camera-equipped XR/AR display | documented enterprise/commercial availability | Rokid chronology + developer documentation distinguishes cameras/optics from Air |
| GLS-0183 | Rokid | Max Pro | 2023 | enterprise / region-limited | 6DoF XR/spatial display | priced AR Studio component + current support identity | first-party AR Studio documentation + hardware model `RA202` |
| GLS-0184 | Rokid | Glass 3 | 2026 | current / enterprise | standalone enterprise AR | current enterprise procurement | first-party manual/developer docs + model numbers `RG301/RG303` |

## Existing canonical corrections

| ID | Previous treatment | Corrected treatment |
|---|---|---|
| GLS-0062 | Rokid Glass 2, era 2021 | Rokid's corporate chronology places Glass 2 in **2020**; stable ID retained |
| GLS-0063 | under-resolved “Rokid AI Glasses,” 2024 | display-free `RV203` family; current names include **Rokid AI Glasses / Style / Neo**; stable ID retained, no duplicate row |

## Adjacent-wearable admission

| ID | Maker | Model | Era | Form | Reason excluded from GLS count |
|---|---|---|---:|---|---|
| ADJ-0010 | Rokid | X-Craft | 2020 | industrial explosion-proof AR headband / helmet-mounted system | not fundamentally eyeglass-frame eyewear |

## System / bundle dispositions

- **AR Studio** = Max Pro + Station Pro. System identity retained; Max Pro is the eyewear model.
- **AR Lite / AR Spatial** = Max 2 + Station 2. System identity retained; Max 2 remains `GLS-0094`.
- **AR Joy / AR Joy 2** = Station-family entertainment bundle around existing Max/Max 2 eyewear. No duplicate glasses row.
- **Style Pack** = `GLS-0063` eyewear plus accessories/power. No duplicate glasses row.
- **Bolon AI Glasses `RV201/RV202`** = close Rokid display-free platform/co-brand relationship; registry/lineage target only until materially distinct hardware is established.

## Identifier allocation

The highest previously allocated canonical identifier is `GLS-0181`. This packet allocates `GLS-0182` through `GLS-0184` and does not reuse or renumber any prior identifier.

## Evidence boundary

Admission establishes product identity and acquisition history, not a completed technical report card. Air Pro, Max Pro, and Glass 3 require generation-specific evidence and must not inherit scores from Air, Max/Max 2, Glass 2, or consumer Rokid Glasses.

See the full [Rokid historical audit](../research/investigations/ROKID_HISTORICAL_AUDIT_2026-09-05.md) and [Rokid lineage](../lineages/ROKID.md).
