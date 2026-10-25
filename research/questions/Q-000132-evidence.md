# Q-000132 — Sony SmartEyeglass host platform

**Original observed question:** [Stack Overflow, October 24, 2014](https://stackoverflow.com/questions/26547629/can-sony-smart-glass-be-used-on-platforms-other-than-android). Asks if Sony SmartEyeglass can be used directly with Windows or Linux via Bluetooth. Preserved as Q-000132 in the canonical registry.

**Primary manufacturer evidence:** [Sony SmartEyeglassControl API reference](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/SmartEyeglassControl) explicitly describes Android SmartExtension. [Sony SmartEyeglassControl.Intents](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/SmartEyeglassControl.Intents) requires Android manifest permissions and messages to the HostApp. [Sony control utilities](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassControlUtils) describes Android-hosted camera, display and audio features.

**Attributed historical confirmation:** 2014 Stack Overflow reply states the official SDK and host application were Android-only at that time. Do not treat this as independent confirmation of 2026 device compatibility.

**Claim boundary:** Sony's *documented SDK* does not provide a native Windows/Linux route. This does not prove direct Bluetooth protocol work is impossible. No GlassesResearch Windows/Linux or Sony hardware reproduction.

**Published answer:** `docs/faq/09-development-openness.md#can-sony-smart-glass-be-used-on-platforms-other-than-android`. **State:** published and exact production FAQ content verified 2026-10-25; reviewed 2026-10-24. No device reproduction.

## Publication proof — 2026-10-25

[PR #691](https://github.com/theGreenJedi/GlassesResearch/pull/691) merged at revision `3221f106e1853fe0ffd1885cbb14d945319c3465`. [Production content proof run #40161886546](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40161886546) succeeded, fetching the public `/docs/faq/09-development-openness/` page and confirming the exact built content digest `ae61abc38c7f` on 2026-10-25. The FAQ source contains this question's heading and cited answer; the production proof verifies the complete deployed page. This does not verify physical-device behavior.
