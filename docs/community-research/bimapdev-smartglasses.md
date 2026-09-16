# BimaPDev / SmartGlasses

**Scope:** Meizu MYVU / StarV Air / XGA010C firmware research  
**Evidence class:** Community-primary; hardware-tested where explicitly stated by the project  
**GlassesResearch verification:** Not independently reproduced

BimaPDev's public SmartGlasses work is tracked here because it provides unusually concrete firmware-level evidence about the XGA010C family. Findings below remain attributed to the project until GlassesResearch reproduces them on its own hardware.

## Compiled code execution from PSRAM

On 2026-09-15, BimaPDev reported hardware-confirmed execution of compiled C from PSRAM. A corrected payload detoured LVGL glyph callbacks and rendered on physical glasses while calling back into vendor firmware.

**Why it matters:** this is evidence of a substantially deeper owner-controlled execution path than static asset replacement alone and is relevant to Owner Control and Hackability research.

**Boundary:** this is community-primary, hardware-tested evidence from the project. GlassesResearch has not independently reproduced arbitrary compiled-code execution on its own XGA010C-family specimen.

**Primary source:** https://github.com/BimaPDev/SmartGlasses/commit/8f5c6b71a23de9d7453bb9d5df7f6a2993dbaae9

## LittleFS and BLE file transfer

On 2026-09-16, the project documented a LittleFS-backed storage path and a BLE file-transfer protocol supporting named, chunked transfers, MD5 verification, per-chunk acknowledgements, and retrieval by known filename.

Follow-up investigation reported an important negative boundary: the examined firmware-side LittleFS adapter appeared read-only, and the investigated 15-operation transfer family did not expose a filesystem-list operation.

**Why it matters:** known-file retrieval and structured transfer behavior are useful Software/Firmware and interoperability evidence, but they do not by themselves establish arbitrary filesystem enumeration or simple replacement-file injection.

**Primary source:** https://github.com/BimaPDev/SmartGlasses/commit/01a374068fba8730b4b497a82bacfda730412428

## Boot and power-off assets appear distinct

With a modified firmware image flashed to hardware, BimaPDev reported that power-off displayed the modified BIMA asset while boot continued to display MYVU. Expanded searching reportedly located the power-off asset in the OTA-carried image but not a corresponding boot/splash asset.

**Working implication:** the evidence supports investigating whether the boot logo resides outside the OTA-carried image or follows a separate boot-stage resource path.

**Boundary:** this is a supported community hypothesis, not a GlassesResearch-confirmed flash-layout fact. Absence from the searched OTA image does not alone prove the boot asset's exact location.

**Primary source:** https://github.com/BimaPDev/SmartGlasses/commit/b9bbe7dbe87660736c5016baef0fee36ab270cf4

## GlassesResearch disposition

- Add the compiled-C result to the XGA010C Owner Control / Hackability investigation queue.
- Add LittleFS and the BLE transfer behavior to Software / Firmware evidence, preserving the no-listing/read-only boundary.
- Add the boot-versus-power-off asset distinction to firmware-layout research as a hypothesis for independent testing.
- Treat BimaPDev as a high-signal public technical contributor for XGA010C-family firmware work and monitor the project alongside Panny777's MYVU work.
- Do not promote these findings to independently verified GlassesResearch results until reproduced on GlassesResearch hardware.

## Provenance rule

Statements above describe what the public project reports or demonstrates. They are not manufacturer claims and are not GlassesResearch laboratory findings. Corrections, contradictory hardware results, or stronger primary evidence should update this record rather than being silently discarded.
