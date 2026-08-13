# Vuzix — populated research fields

This record applies the GlassesResearch evidence frameworks to the current Vuzix lineage while preserving the distinction between the Z100 peripheral-display branch and the standalone Android branch.

## Evidence base

Primary evidence currently includes Vuzix Z100 documentation (`EV-0016`) and the Vuzix Ultralite SDK overview (`EV-0017`), plus the Vuzix lineage's linked developer and support resources.

## Architecture

**Z100 / Ultralite branch:** phone-assisted peripheral display. The glasses are documented as a Bluetooth-connected display peripheral whose application logic runs primarily on the paired mobile device. Confidence: confirmed.

**Standalone Android branch:** M400/M4000, Blade 2, Shield, LX1 and related devices are documented as self-contained Android wearable computers. Confidence: confirmed at the branch level; exact capabilities remain model-specific.

## Connectivity

Z100: Bluetooth connectivity is vendor documented. Official development paths exist for Android and iOS. Confidence: confirmed from vendor-primary evidence.

Standalone Android branch: Vuzix documents Wi-Fi, Bluetooth/BLE, USB debugging and app installation routes across supported devices. Exact radios and interface limits remain model-specific.

## Developer access and owner control

Z100 has an official SDK intended to let applications drive display, connection, input and battery-related functions. This is strong evidence of public developer access, but does not by itself establish firmware access or unrestricted protocol control.

The standalone Android branch benefits from standard Android application development plus Vuzix SDKs and documented APK installation routes. This is strong evidence for application-layer owner/developer access relative to closed consumer-only glasses.

Bootloader access, firmware replacement, low-level sensor access and service independence remain unknown unless established per model.

## Cloud independence

The Z100 architecture is host-dependent rather than inherently cloud-dependent. Core display behavior appears to depend on the paired host application, not necessarily a remote service. Exact offline behavior should still be tested.

Standalone Android products can run applications locally on the glasses, which is favorable for cloud independence. Vendor cloud features, licensing and account dependencies still require model-specific evidence.

## Sensors and visual AI

Vuzix spans display-centric and camera-equipped enterprise products. Sensor and visual-AI capability must be recorded per model rather than inherited across the corporate lineage. Z100 should not receive visual-AI credit merely because other Vuzix products include cameras.

## Silicon and OEM lineage

Corporate lineage is confirmed. Shared chipset or ODM relationships are not assumed across branches. The large architecture difference between phone-assisted Z100 and standalone Android products argues strongly against collapsing the family into one hardware genealogy.

## Prescription, serviceability, battery and aging

These remain under-populated. Vuzix's enterprise orientation and long support history make these high-priority fields for later research, especially replacement optics, batteries, service paths, accessory continuity and software support duration.

## Report-card implications

- Openness: evidence supports meaningful public SDK/application access, strongest on the Android branch.
- Owner Control: stronger than consumer-locked platforms at the application layer; low-level control remains model-specific.
- Cloud Independence: structurally promising because both branches can perform key functions through local host/device software, but exact offline testing is still needed.
- Hackability: likely above average where Android debugging, APK installation and SDK documentation are available; avoid converting this into a universal score without per-model evidence.

## Unknowns retained

Firmware replacement, bootloader state, exact sensor exposure, regional restrictions, prescription serviceability, battery aging, component repairability and long-term account/service dependence remain unknown until supported by device-specific evidence.