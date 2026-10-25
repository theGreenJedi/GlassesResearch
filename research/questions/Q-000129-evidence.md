# Q-000129 — Wi-Fi modes in Sony SmartEyeglass

**Original observed question:** [Public developer question](https://stackoverflow.com/questions/37879755/installing-wifi-option-in-sony-smart-glass), preserved in `research/questions/registry.json` as Q-000129; do not create another Q ID for this observation. Reviewed 2026-10-25.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Sony SDK distinguishes normal Bluetooth and high-power Wi-Fi host transport | [Source](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassControlUtils) | Archived primary Sony API; historical behavior, not independently bench tested |
| Power mode constants define Bluetooth and Wi-Fi transport | [Source](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/SmartEyeglassControl.Intents) | Archived Sony primary |
| Question reports inability to enter protected SSID password | [Source](https://stackoverflow.com/questions/37879755/installing-wifi-option-in-sony-smart-glass) | 2016 user report; not evidence that custom protocol approaches are impossible |
| No supported normal SSID configuration flow established | [Source](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassControlUtils) | Absence of documented setting is not proof of technical impossibility |

## Verification and publication gate

No GlassesResearch device or period-correct SDK reproduction. Manufacturer docs are historical/archived and may not reflect modern distribution or compatibility. Do not claim successful device behavior from a source citation alone. Proposed answer: `docs/faq/09-development-openness.md#can-i-add-a-normal-wi-fi-network-connection-to-sony-smarteyeglass`. **State: researched, publication pending public-page and directory-link verification.** Only then mark Q-000129 as `answered` in the existing registry with the canonical answer URL, publication proof, and date. This evidence packet preserves the original observation and uncertainty.
