# Smart-Glasses Catalog Reconciliation — 2026-08-12

This reconciliation converts the completed lineage-first research queue into canonical smart-glasses admissions while keeping adjacent form factors out of the smart-glasses count.

## Stable IDs assigned

The prior canonical list contained 121 rows, with `GLS-0120` and `GLS-0121` already assigned to Anko Camera Glasses and Vuzix Shield. The next stable IDs are therefore assigned sequentially from `GLS-0122`.

| ID | Maker | Model / generation | Form / type | Catalog decision | Evidence packet |
|---|---|---|---|---|---|
| GLS-0122 | ODG | R-7 | standalone enterprise AR eyewear | admit | [ODG R-series](../docs/report-cards/LINEAGE_ODG_R_SERIES.md) |
| GLS-0123 | Recon | Jet | sport HUD eyewear | admit | [Recon Jet](../docs/report-cards/LINEAGE_RECON_JET.md) |
| GLS-0124 | Recon / Intel | Jet Pro | enterprise/sport HUD eyewear | admit | [Recon Jet](../docs/report-cards/LINEAGE_RECON_JET.md) |
| GLS-0125 | Recon / Intel | Jet Pro+ | enterprise/sport HUD eyewear | admit | [Recon Jet](../docs/report-cards/LINEAGE_RECON_JET.md) |
| GLS-0126 | Optinvent | ORA-1 | standalone AR eyewear | admit | [Optinvent ORA](../docs/report-cards/LINEAGE_OPTINVENT_ORA.md) |
| GLS-0127 | Optinvent | ORA-2 | standalone AR eyewear | admit | [Optinvent ORA](../docs/report-cards/LINEAGE_OPTINVENT_ORA.md) |
| GLS-0128 | Toshiba / Dynabook | dynaEdge AR100 + DE-100 | enterprise monocular eyewear system | admit as one hardware generation | [dynaEdge AR100](../docs/report-cards/LINEAGE_TOSHIBA_DYNAEDGE_AR100.md) |
| GLS-0129 | DAQRI | Smart Glasses | enterprise AR eyewear | admit | [DAQRI professional AR](../docs/report-cards/LINEAGE_DAQRI_PROFESSIONAL_AR.md) |
| GLS-0130 | Lenovo | ThinkReality A6 | enterprise binocular AR eyewear | admit | [ThinkReality A6](../docs/report-cards/LINEAGE_LENOVO_THINKREALITY_A6.md) |
| GLS-0131 | ThirdEye | X1 Smart Glasses | enterprise mixed-reality eyewear | admit | [ThirdEye X-series](../docs/report-cards/LINEAGE_THIRDEYE_X_SERIES.md) |
| GLS-0132 | ThirdEye | X2 MR Glasses | enterprise mixed-reality eyewear | admit | [ThirdEye X-series](../docs/report-cards/LINEAGE_THIRDEYE_X_SERIES.md) |
| GLS-0133 | ThirdEye | Alpha1 MR Glasses | enterprise mixed-reality eyewear | admit | [ThirdEye X-series](../docs/report-cards/LINEAGE_THIRDEYE_X_SERIES.md) |
| GLS-0134 | Pivothead | Camera Glasses — first generation (Recon/Aurora/Durango/Moab style family) | camera eyewear | admit as one electronics generation; style names are variants | [Pivothead](../docs/report-cards/LINEAGE_PIVOTHEAD.md) |
| GLS-0135 | Pivothead | SMART / Architect Edition | connected camera eyewear | admit | [Pivothead](../docs/report-cards/LINEAGE_PIVOTHEAD.md) |
| GLS-0136 | Mutrics | M1 / smart audio eyewear generation | audio eyewear | admit | [Mutrics](../docs/report-cards/LINEAGE_MUTRICS.md) |
| GLS-0137 | Chamelo | Dusk Classic | electrochromic/audio eyewear | admit | [Chamelo](../docs/report-cards/LINEAGE_CHAMELO.md) |
| GLS-0138 | Chamelo | Music Shield Gen 2 | electrochromic/open-ear-audio sport eyewear | admit | [Chamelo](../docs/report-cards/LINEAGE_CHAMELO.md) |
| GLS-0139 | Chamelo | Aura | electronically color-changing eyewear | admit | [Chamelo](../docs/report-cards/LINEAGE_CHAMELO.md) |
| GLS-0140 | NuEyes | e2+ | assistive standalone display eyewear | admit | [NuEyes](../docs/report-cards/LINEAGE_NUEYES.md) |
| GLS-0141 | NuEyes | Pro 3 | assistive/enterprise AR eyewear | admit; configurations remain one generation | [NuEyes](../docs/report-cards/LINEAGE_NUEYES.md) |
| GLS-0142 | NuEyes | Pro 3e | tethered display eyewear | admit | [NuEyes](../docs/report-cards/LINEAGE_NUEYES.md) |
| GLS-0143 | NuEyes | Pro 4 | assistive tethered camera/display eyewear | admit | [NuEyes](../docs/report-cards/LINEAGE_NUEYES.md) |
| GLS-0144 | Envision | Envision Glasses | assistive visual-AI eyewear on Glass EE2 hardware | admit | [Envision](../docs/report-cards/LINEAGE_ENVISION.md) |
| GLS-0145 | Envision | Ally Solos | assistive AI/audio-camera eyewear | admit | [Envision](../docs/report-cards/LINEAGE_ENVISION.md) |

**Reconciled smart-glasses count: 145.** This is 121 prior canonical rows + 24 newly admitted eyewear generations.

## Deliberately not admitted to the smart-glasses count

The following researched devices belong under [`ADJACENT_WEARABLES.md`](ADJACENT_WEARABLES.md), not `THE_LIST.md`: Optinvent ORA-X; DAQRI Smart Helmet; ThirdEye MIDAS; Microsoft HoloLens and HoloLens 2; Magic Leap One/1 and Magic Leap 2; OrCam MyEye 2 Pro and MyEye 3 Pro.

DAQRI Smart HUD is retained as lineage context but is not wearable and therefore receives neither a `GLS-` nor `ADJ-` wearable ID.

## Still not canonical rows

Research did **not** justify promoting ODG R-8 or R-9, unnamed early NuEyes devices, earlier poorly archived OrCam MyEye hardware, North Focals 2.0, prototypes/reference designs, or announced products that never crossed the acquisition threshold. These remain registry/archive work.

## Editorial rule carried forward

A lineage investigation can resolve multiple catalog outcomes at once: some members become `GLS-` smart-glasses rows, some become `ADJ-` adjacent-wearable rows, some remain research-registry candidates, and some are documented as non-wearable lineage relatives. The form-factor shelf and acquisition evidence determine the outcome, not brand or marketing language.
