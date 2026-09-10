# Identity Forensics — Wave 02 Canonical Reconciliation

**Date:** 2026-09-10  
**Evidence packet:** [Identity Forensics — Wave 02](../research/investigations/IDENTITY_FORENSICS_WAVE_02_2026-09-10.md)

This packet records the evidence-clean canonical outcome from the second forensic pass. It admits three marketed smart-glasses identities and resolves the historical Iristick Z1 name without minting a duplicate row.

## Admit to canonical purchaser-history ledger

| ID | Maker | Model | Era | State | Type | Access | Evidence |
|---|---|---|---|---|---|---|---|
| GLS-0238 | RealWear | Arc 3 | 2025 | current/enterprise | see-through assisted-reality smart glasses | manufacturer store | https://shop.realwear.com/products/realwear-arc-3 |
| GLS-0239 | Iristick | G1 | 2021 | legacy/enterprise | camera/display smart safety glasses | enterprise sale | https://iristick.com/uploads/files/IRI-spec-sheet-Iristick.G1-32021-EU-final.pdf |
| GLS-0240 | Iristick | G1 PRO | 2021 | legacy/enterprise | camera/display smart safety glasses | enterprise sale | https://iristick.com/uploads/files/IRI-spec-sheet-Iristick.G1-32021-EU-final.pdf |

## Alias / lineage resolution

| Historical name | Canonical resolution | Evidence boundary |
|---|---|---|
| Iristick Z1 | alias / former market name of `GLS-0239` Iristick G1 | Iristick's contemporaneous April 2021 release states that G1 was formerly on the market as Z1. Do not mint a separate Z1 row. |
| Iristick G1 PRO | separate marketed PRO identity sharing the G1 core platform | The manufacturer comparison shows the same chassis, display, cameras, zoom and pocket unit; PRO adds multilingual voice commands and advanced barcode scanning. Separate catalog identity does not imply a separate core electronics generation. |

## Hold / non-admission

| Product / lead | Disposition | Reason |
|---|---|---|
| Iristick H3 | watch / pre-release | First-party material identifies H3 as coming soon, but no demonstrated paid acquisition route has been established. |
| RealWear Arc Base / thermal modules / support plans | non-product accessories/services | Accessories and support configurations do not create additional eyewear identities. |

## Count impact

Mechanical synchronization should add three active canonical rows, advancing the active purchaser-history population from **236 to 239**. Stable IDs extend through `GLS-0240` because the sequence contains a historical retired/gap identity and is not itself the active-row count.

## Evidence boundary

Admission establishes marketed identity and purchaser history only. It does not independently verify RealWear or Iristick optical, battery, camera, software, privacy, durability, safety, or owner-control claims.

For Iristick specifically, the evidence supports a shared G1/G1 PRO platform with a separately marketed PRO feature tier. The catalog split follows the same commercial-identity ruler already applied to G2 / G2 PRO and must not be cited as proof that base and PRO use different core hardware.
