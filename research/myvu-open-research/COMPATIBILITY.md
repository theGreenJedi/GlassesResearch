# MYVU Compatibility Matrix

This matrix deliberately separates **identity** from **branding**. Unknown cells stay unknown.

| Hardware / identity | Firmware | Host | Software | Evidence | Current result |
|---|---|---|---|---|---|
| Meizu MYVU / Star Air `XGA010C` | upstream test firmware unspecified here | Android API 31 test context | Panny777 Meizu-Myvu-Client | UPSTREAM-DOCUMENTED | Hardware-verified working client |
| Meizu MYVU / Star Air `XGA010C` | may vary | Android minSdk 26 / compiled SDK 34 | Panny777 Meizu-Myvu-SDK v0.3.0 documentation | UPSTREAM-DOCUMENTED | Core connection/features documented; firmware drift explicitly warned |
| Imiki-branded MYVU, exact model pending | pending | Android, exact version pending | Panny777 client v0.3 | COMMUNITY-REPORTED | Discovery/pairing failure reported; MAC-directed pairing proposed, outcome not established |
| MYVU regional variant, exact model pending | pending | iOS, UK owner | official MYVU app | COMMUNITY-REPORTED | App/account/pairing friction reported; requires reproduction and exact app-region identification |

## Required fields for every new compatibility record

- Printed/model identifier
- Brand/market name
- Hardware revision if exposed
- Firmware/build
- Host device and OS/version
- Companion/client name, version and distribution region/source
- BLE advertised name/address behavior
- GATT service + characteristic inventory
- BR/EDR/RFCOMM behavior where applicable
- Pairing method
- Result and reproducibility
- Evidence state
- Source/provenance

## Investigation priority

The highest-value question is whether apparent MYVU/Imiki/Air/Air2 differences represent:

1. branding only,
2. firmware/app-region differences,
3. protocol-generation differences,
4. materially different hardware lineage,
5. or combinations of the above.

Do not collapse these possibilities without evidence.