# Q-000126 — Installing legacy Vuzix M100 SDK in Android Studio

**Original observed question:** [Public developer question](https://stackoverflow.com/questions/42242199/how-to-setup-android-studio-to-use-vuzix-m100-smart-glass-sdk), preserved in `research/questions/registry.json` as Q-000126; do not create another Q ID for this observation. Reviewed 2026-10-25.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| M100 SDK 1.4+ uses Vuzix M100 API 15 add-on and documented manual folder fallback | [Source](https://d2iankuf53zudv.cloudfront.net/Content/Upload/Installing-the-Vuzix-M100-SDK.pdf) | Primary Vuzix historical guide; no current download verification |
| Vuzix M100 developer guide demonstrates Android Studio API 15 add-on | [Source](https://files.vuzix.com/Content/Upload/Driver_File_VoiceControlSDK_1__20160317210049767.pdf) | Primary Vuzix 2015 guide; not 2026 Android Studio compatibility |
| Stub JARs should not be bundled in APK | [Source](https://d2iankuf53zudv.cloudfront.net/Content/Upload/Installing-the-Vuzix-M100-SDK.pdf) | Explicit Vuzix runtime guidance |
| Original asker reported add-on URL failure | [Source](https://stackoverflow.com/questions/42242199/how-to-setup-android-studio-to-use-vuzix-m100-smart-glass-sdk) | 2017 report, not a current status test |

## Verification and publication gate

No GlassesResearch device or period-correct SDK reproduction. Manufacturer docs are historical/archived and may not reflect modern distribution or compatibility. Do not claim successful device behavior from a source citation alone. Proposed answer: `docs/faq/09-development-openness.md#how-do-i-set-up-android-studio-with-the-vuzix-m100-sdk`. **State: researched, publication pending public-page and directory-link verification.** Only then mark Q-000126 as `answered` in the existing registry with the canonical answer URL, publication proof, and date. This evidence packet preserves the original observation and uncertainty.
