# Q-000122 — Registering a Sony SmartEyeglass extension

**Original observed question:** [Public developer question](https://stackoverflow.com/questions/38713859/how-to-register-an-app-for-sony-smart-glass), preserved in `research/questions/registry.json` as Q-000122; do not create another Q ID for this observation. Reviewed 2026-10-25.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| RegistrationInformation is an abstract SDK class with required methods | [Source](https://developer.sony.com/reference/seg-sdk/com/sonyericsson/extras/liveware/extension/util/registration/RegistrationInformation) | Primary archived Sony class definition |
| ExtensionService requires getRegistrationInformation() | [Source](https://developer.sony.com/reference/seg-sdk/com/sonyericsson/extras/liveware/extension/util/ExtensionService) | Primary Sony class definition; Android service, not Activity |
| Host registers extension capabilities via ContentProvider | [Source](https://developer.sony.com/reference/seg-sdk/com/sonyericsson/extras/liveware/aef/registration/Registration) | Primary Sony API |
| Question includes missing sample classes and unbound variables | [Source](https://stackoverflow.com/questions/38713859/how-to-register-an-app-for-sony-smart-glass) | Original code/errors; incomplete project means no validated full fix |

## Verification and publication gate

No GlassesResearch device or period-correct SDK reproduction. Manufacturer docs are historical/archived and may not reflect modern distribution or compatibility. Do not claim successful device behavior from a source citation alone. Published answer: `docs/faq/09-development-openness.md#how-do-i-register-a-sony-smarteyeglass-app-so-smart-connect-recognizes-it`. **State: published after exact production content and directory verification on 2026-10-25.** The existing registry entry Q-000122 was marked `answered` only after production proof; the original observed question and uncertainty are preserved.

## Publication proof — 2026-10-25

[PR #693](https://github.com/theGreenJedi/GlassesResearch/pull/693) merged as revision `967617cdf0cf7d9b48f1cf52dbef06cc3b714b3f` after documentation, link/fragment, editorial, smoke and Lighthouse checks passed. [Production proof run #40230664224](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40230664224) succeeded: fetched the public development FAQ with exact built-page digest `455eaa9f7f24` and the Practical Answers directory with digest `827fb72f3818`. The deployed FAQ and directory contain the heading/anchor specified above, validated by strict build-time fragment checks. This is content-publication proof, **not** a device or SDK execution test.
