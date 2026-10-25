# Q-000130 — Porting Google Glass GDK applications to Vuzix M100

**Original observed question:** [Public developer question](https://stackoverflow.com/questions/32070647/develop-for-vuzix-m100-smart-glasses), preserved in `research/questions/registry.json` as Q-000130; do not create another Q ID for this observation. Reviewed 2026-10-25.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Original developer reported GDK APK would not run on M100 | [Source](https://stackoverflow.com/questions/32070647/develop-for-vuzix-m100-smart-glasses) | 2015 firsthand report, not universal compatibility test |
| Glass GDK is Glass-specific | [Source](https://developers.google.com/glass/develop/gdk) | Primary legacy Google SDK documentation |
| M100 SDK targets Android API 15 | [Source](https://d2iankuf53zudv.cloudfront.net/Content/Upload/Installing-the-Vuzix-M100-SDK.pdf) | Primary Vuzix documentation |
| M100 product guide identifies Android 4.0.4 | [Source](https://files.vuzix.com/Content/Upload/Driver_File_425PB0002_03_Product_Guide_US_Enterprise_20160404131344910.pdf) | Primary Vuzix historical product guide |
| Wikitude workaround was developer's historical suggestion | [Source](https://stackoverflow.com/questions/32070647/develop-for-vuzix-m100-smart-glasses) | No independently tested cross-device portability guarantee |

## Verification and publication gate

No GlassesResearch device or period-correct SDK reproduction. Manufacturer docs are historical/archived and may not reflect modern distribution or compatibility. Do not claim successful device behavior from a source citation alone. Published answer: `docs/faq/09-development-openness.md#can-a-google-glass-gdk-app-run-unchanged-on-vuzix-m100`. **State: published after exact production content and directory verification on 2026-10-25.** The existing registry entry Q-000130 was marked `answered` only after production proof; the original observed question and uncertainty are preserved.

## Publication proof — 2026-10-25

[PR #693](https://github.com/theGreenJedi/GlassesResearch/pull/693) merged as revision `967617cdf0cf7d9b48f1cf52dbef06cc3b714b3f` after documentation, link/fragment, editorial, smoke and Lighthouse checks passed. [Production proof run #40230664224](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40230664224) succeeded: fetched the public development FAQ with exact built-page digest `455eaa9f7f24` and the Practical Answers directory with digest `827fb72f3818`. The deployed FAQ and directory contain the heading/anchor specified above, validated by strict build-time fragment checks. This is content-publication proof, **not** a device or SDK execution test.
