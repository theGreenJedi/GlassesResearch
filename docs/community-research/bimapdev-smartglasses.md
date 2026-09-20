# BimaPDev / SmartGlasses

**Scope:** Meizu MYVU / StarV Air / XGA010C firmware research  
**Evidence class:** Community-primary; hardware-tested where explicitly stated by the project  
**GlassesResearch verification:** Not independently reproduced  
**Last substantive review:** 2026-09-20

BimaPDev's public SmartGlasses work is tracked here because it provides unusually concrete firmware-level evidence about the XGA010C family. Findings below remain attributed to the project until GlassesResearch reproduces them on its own hardware.

## Research progression

The important result is not a single patch. The public project now documents a progression from firmware analysis and bounded patching into hardware-confirmed execution of owner-supplied code:

**firmware extraction/analysis → bounded image and behavior patching → hardware-visible modified firmware → PSRAM Thumb execution → compiled-C execution → filesystem and transfer-boundary mapping**

This progression materially changes the XGA010C investigation. Earlier GlassesResearch notes correctly quarantined firmware-level owner control while the primary artifact was missing. That artifact is now directly inspectable and includes hardware-test reports. The evidence state therefore advances from an unresolved lead to **community-primary, hardware-tested**. It does **not** advance to GlassesResearch Verified.

## Hardware-visible firmware modification

BimaPDev documented modified firmware running on physical glasses, including a BIMA rebrand and altered shutdown behavior. A later hardware test showed the modified power-off asset while boot continued to display MYVU, providing a visible distinction between the OTA-carried shutdown asset and the separate boot path.

This matters as a positive control: the project is not relying solely on static binary analysis to infer that a modified image was accepted and executed by hardware.

**Primary sources:**
- https://github.com/BimaPDev/SmartGlasses/commit/1b898a3cfb6967d57479e7abd99383422c57e2a7
- https://github.com/BimaPDev/SmartGlasses/commit/b9bbe7dbe87660736c5016baef0fee36ab270cf4

## Owner-supplied code execution from PSRAM

The project subsequently reported hardware-confirmed execution of hand-written Thumb code from PSRAM and then compiled C from the same general execution path. Follow-up hardware testing used multiple detoured callbacks and calls from PSRAM back into vendor firmware; a two-entry glyph fix produced clean on-device rendering consistent with the stated diagnosis.

This is stronger evidence than static patchability alone. It demonstrates a bounded owner-controlled execution surface inside the running firmware environment.

**Important boundary:** the published work does not establish unrestricted native application execution, root access, a complete replacement firmware, or a general-purpose custom-firmware environment. At the reported stage, payload support still had explicit limits including unresolved use of payload-owned data/BSS/string-literal/literal-pool state.

**Primary sources:**
- https://github.com/BimaPDev/SmartGlasses/commit/8f5c6b71a23de9d7453bb9d5df7f6a2993dbaae9
- https://github.com/BimaPDev/SmartGlasses/commit/d2aa057a7de6dc7aa3cce0d4de68bc9e9ac99757

## Firmware-build boundaries matter

The project has repeatedly corrected assumptions when evidence from one firmware build did not transfer cleanly to another. Region offsets and executable/resource boundaries must therefore be treated as build-specific until demonstrated otherwise.

**GlassesResearch implication:** never generalize an address, partition boundary, patch offset, or resource location across XGA010C firmware versions without recording the exact build and reproducing the mapping.

## LittleFS and BLE file transfer

On 2026-09-16, the project documented a LittleFS-backed storage path and a protobuf ShareMessage BLE file-transfer family supporting named, chunked transfers, MD5 verification, per-chunk acknowledgements, destination path/name fields, and retrieval by known filename.

The same investigation established an important negative boundary. The examined firmware-side LittleFS adapter reports writes as unsupported and loads its partition from flash into PSRAM at boot. The investigated 15-operation transfer family exposes named push/pull behavior but no filesystem-list operation. The project used positive controls when asserting these absences.

**Why it matters:** known-file transfer/retrieval is useful interoperability evidence, but it does not establish arbitrary filesystem enumeration or a simple route for replacing LittleFS assets.

**Primary source:** https://github.com/BimaPDev/SmartGlasses/commit/01a374068fba8730b4b497a82bacfda730412428

## Boot and power-off assets are distinct

With modified firmware flashed to hardware, power-off displayed the modified BIMA asset while boot continued to display MYVU. The project's expanded whole-image search then located the shutdown asset in the OTA-carried firmware while finding no corresponding boot/splash asset there.

The project explicitly corrected an earlier incomplete search that had covered only one color format and one resource-registration block. The revised search expanded across formats and the whole image before making the negative claim.

**Working implication:** the boot asset follows a path outside the examined OTA-carried image. Its exact physical location remains unresolved without additional device/flash evidence.

**Primary source:** https://github.com/BimaPDev/SmartGlasses/commit/b9bbe7dbe87660736c5016baef0fee36ab270cf4

## GlassesResearch disposition

- Promote the former firmware/OTA lead from **unresolved lead** to **community-primary, hardware-tested evidence**.
- Record owner-supplied PSRAM Thumb and compiled-C execution under XGA010C Owner Control / Hackability, while preserving the payload and recovery boundaries.
- Record hardware-visible firmware modification as a positive-control result, distinct from arbitrary custom firmware.
- Add LittleFS and the BLE transfer behavior to Software / Firmware evidence, preserving the read-only/no-listing boundary.
- Add the boot-versus-power-off asset distinction to firmware-layout research; keep the boot asset's exact location unresolved.
- Treat firmware offsets and region boundaries as build-specific until independently mapped for each version.
- Keep BimaPDev as a high-signal public technical contributor for XGA010C-family firmware work and monitor the project alongside Panny777's MYVU client/SDK work.
- When GlassesResearch controls an XGA010C specimen, prioritize reproduction of one deliberately benign, hardware-visible modification before broader write experiments.
- Do not promote these findings to GlassesResearch Verified until reproduced on GlassesResearch hardware.

## Provenance rule

Statements above describe what the public project reports or demonstrates in directly inspectable source, tooling, gates, and hardware-test reports. They are not manufacturer claims and are not GlassesResearch laboratory findings. Corrections, contradictory hardware results, or stronger primary evidence should update this record rather than being silently discarded.
