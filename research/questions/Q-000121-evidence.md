# Q-000121 — Installing a custom Sony SmartEyeglass app

**Original observed question:** [Public developer question](https://stackoverflow.com/questions/37791282/app-installation-in-sony-smart-glass), preserved in `research/questions/registry.json` as Q-000121; do not create another Q ID for this observation. Reviewed 2026-10-25.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| SmartEyeglass apps are Android SmartExtensions mediated by a host application | [Source](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/SmartEyeglassControl) | Primary archived Sony API; not a claim of 2026 platform support |
| Accessory extensions register with host application using Android registration provider | [Source](https://developer.sony.com/reference/seg-sdk/com/sonyericsson/extras/liveware/aef/registration/Registration) | Primary Sony API; registration mechanism only |
| SDK extensions rather than a bare Android Activity are needed to appear in SmartEyeglass menu | [Source](https://stackoverflow.com/questions/42295084/how-to-install-the-custom-app-to-the-android-phone-for-using-sony-smarteyeglass) | 2017 attributed developer support exchange; not device reproduction |
| USB-debug/sideload advice was speculative | [Source](https://stackoverflow.com/questions/37791282/app-installation-in-sony-smart-glass) | Original community answer expressly conditional; not Sony installation instructions |

## Verification and publication gate

No GlassesResearch device or period-correct SDK reproduction. Manufacturer docs are historical/archived and may not reflect modern distribution or compatibility. Do not claim successful device behavior from a source citation alone. Published answer: `docs/faq/09-development-openness.md#how-do-i-install-a-custom-app-for-sony-smarteyeglass`. **State: published after exact production content and directory verification on 2026-10-25.** The existing registry entry Q-000121 was marked `answered` only after production proof; the original observed question and uncertainty are preserved.

## Publication proof — 2026-10-25

[PR #693](https://github.com/theGreenJedi/GlassesResearch/pull/693) merged as revision `967617cdf0cf7d9b48f1cf52dbef06cc3b714b3f` after documentation, link/fragment, editorial, smoke and Lighthouse checks passed. [Production proof run #40230664224](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40230664224) succeeded: fetched the public development FAQ with exact built-page digest `455eaa9f7f24` and the Practical Answers directory with digest `827fb72f3818`. The deployed FAQ and directory contain the heading/anchor specified above, validated by strict build-time fragment checks. This is content-publication proof, **not** a device or SDK execution test.
