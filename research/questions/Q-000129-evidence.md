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

No GlassesResearch device or period-correct SDK reproduction. Manufacturer docs are historical/archived and may not reflect modern distribution or compatibility. Do not claim successful device behavior from a source citation alone. Published answer: `docs/faq/09-development-openness.md#can-i-add-a-normal-wi-fi-network-connection-to-sony-smarteyeglass`. **State: published after exact production content and directory verification on 2026-10-25.** The existing registry entry Q-000129 was marked `answered` only after production proof; the original observed question and uncertainty are preserved.

## Publication proof — 2026-10-25

[PR #693](https://github.com/theGreenJedi/GlassesResearch/pull/693) merged as revision `967617cdf0cf7d9b48f1cf52dbef06cc3b714b3f` after documentation, link/fragment, editorial, smoke and Lighthouse checks passed. [Production proof run #40230664224](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40230664224) succeeded: fetched the public development FAQ with exact built-page digest `455eaa9f7f24` and the Practical Answers directory with digest `827fb72f3818`. The deployed FAQ and directory contain the heading/anchor specified above, validated by strict build-time fragment checks. This is content-publication proof, **not** a device or SDK execution test.
