# Vuzix M400 / M4000

Enterprise monocular smart glasses in Vuzix's standalone Android wearable-computer branch.

## Architecture

Vuzix's developer documentation classifies the M400 and M4000 as standalone devices that do not require an outside connection. Applications can run on the glasses themselves, while Wi-Fi and Bluetooth can be used for connectivity.

## Developer access

Vuzix recommends Android Studio and standard Android APIs, supplemented by Vuzix SDKs including Speech, Barcode, Connectivity, and HUD resources. The Connectivity SDK supports app-to-app communication between an Android phone and M400/M4000 glasses.

Vuzix View also supports the M400/M4000 and can install APKs through USB debugging, mirror/control the display, capture screenshots, and retrieve logs.

## GlassesResearch significance

This family is useful as a counterexample to cloud-first consumer glasses: the hardware is a wearable Android computer with an explicit application-development path. That creates substantive Openness, Owner Control, Cloud Independence, and Hackability questions worth evaluating separately from consumer AI assistant quality.

No report-card grade is assigned here yet.

## Primary sources

- [Vuzix Developer Resources](https://support.vuzix.com/docs/developer-resources)
- [Vuzix Connectivity SDK](https://github.com/Vuzix/connectivity-sdk)
- [Vuzix View functionality](https://support.vuzix.com/docs/vuzix-view-functionality)

## Related research

- [Vuzix lineage](../../lineages/VUZIX.md)
- [Developer resources](../../hacking/README.md)
- [The List](../THE_LIST.md)
