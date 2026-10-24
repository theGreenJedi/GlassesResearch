# Q-000132 — Sony SmartEyeglass host platform

**Original observed question:** [Stack Overflow, October 24, 2014](https://stackoverflow.com/questions/26547629/can-sony-smart-glass-be-used-on-platforms-other-than-android). Asks if Sony SmartEyeglass can be used directly with Windows or Linux via Bluetooth. Preserved as Q-000132 in the canonical registry.

**Primary manufacturer evidence:** [Sony SmartEyeglassControl API reference](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/SmartEyeglassControl) explicitly describes Android SmartExtension. [Sony SmartEyeglassControl.Intents](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/SmartEyeglassControl.Intents) requires Android manifest permissions and messages to the HostApp. [Sony control utilities](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassControlUtils) describes Android-hosted camera, display and audio features.

**Attributed historical confirmation:** 2014 Stack Overflow reply states the official SDK and host application were Android-only at that time. Do not treat this as independent confirmation of 2026 device compatibility.

**Claim boundary:** Sony's *documented SDK* does not provide a native Windows/Linux route. This does not prove direct Bluetooth protocol work is impossible. No GlassesResearch Windows/Linux or Sony hardware reproduction.

**Proposed answer:** `docs/faq/09-development-openness.md#can-sony-smarteyeglass-apps-run-directly-from-windows-or-linux-instead-of-android`. **State:** researched; pending deployment and exact live-page verification. Reviewed 2026-10-24.
