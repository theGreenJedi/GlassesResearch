# W610 and W6xx Genealogy

This document maps relationships among W610 retail names, manufacturers, software operators, and possible W6xx relatives. Matching names or frames alone do not prove common electronics.

## Current W610 platform fingerprint

The strongest repeated public fingerprint is:

- Model designation: `W610`
- Companion app: `HeyCyan`
- Main controller claim: Jerry / JL7018F
- Coprocessor claim: Allwinner V821L2
- Camera claim: 8 MP sensor, often marketed as 32 MP interpolated
- Storage claim: 4 GB / 32 Gbit
- Battery claim: usually 270 mAh
- Connectivity: Bluetooth plus Wi-Fi media transfer
- Audio: open-ear speakers and dual-microphone ENC
- Charging: magnetic cable
- Environmental claim: IP65

Repeated independent retail and OEM listings make this a strong platform-identification lead, but physical teardown and firmware evidence are still needed.

## Known names using the W610 designation

| Model or retail name | Relationship | Shared fingerprint | Evidence state |
|---|---|---|---|
| HeyCyan / unbranded W610 | Baseline platform identity | HeyCyan app, W610 name, common feature set | Confirmed retail/platform naming |
| Goodway W610 | OEM-marketed implementation | JL7018F, V821L2, 8 MP, 270 mAh, HeyCyan, IP65 | Strong commercial evidence |
| Zhiyang/OEM/ODM W610 | OEM/ODM marketplace implementation | Same chipset, camera, storage, battery, app, and IP65 claims | Strong commercial evidence |
| Mingdaln W610 | Retail rebrand | HeyCyan, 270 mAh, 32 GB, same feature family | Strong rebrand lead |
| NJYUAN W610 | Retail rebrand | Same JL7018F + V821L2 fingerprint and HeyCyan app | Strong rebrand lead |
| KLSYQ W610 | Retail rebrand/manual identity | W610, HeyCyan, camera, Wi-Fi transfer, similar controls | Strong rebrand lead; some published specs conflict |
| Mingtawn W610 | Retail rebrand/manual identity | W610, HeyCyan, 270 mAh, removable lenses, similar controls | Strong rebrand lead |
| Generic eBay W610 | Unbranded reseller variant | W610, HeyCyan, Bluetooth/Wi-Fi, 8 MP claims | Secondary commercial evidence |

## Important inconsistencies

Some manual mirrors and sellers claim different battery capacities, Bluetooth versions, weights, operating systems, or recording resolutions. These differences may reflect listing errors, hardware revisions, bundled variants, or entirely separate products reusing `W610`. Do not normalize conflicting claims without device-level evidence.

## W6xx relatives

W610 MAX, W620, W640, and W650 remain **unresolved relatives**. Shared naming suggests a commercial family, but a relationship must be demonstrated through one or more of:

- shared app support tables
- identical BLE services or device information
- firmware/update infrastructure
- matching PCB and component layout
- common OEM documentation
- certification records

## Next proof steps

1. Record package, manual, device label, and BLE identifiers from the owned unit.
2. Compare product photographs and control layouts across known W610 brands.
3. Capture app-supported model lists and update endpoints.
4. Search FCC, CE, Bluetooth SIG, and Chinese certification data using company and chipset leads.
5. Compare W620/W640/W650 listings against the W610 platform fingerprint.
