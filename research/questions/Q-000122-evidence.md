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

No GlassesResearch device or period-correct SDK reproduction. Manufacturer docs are historical/archived and may not reflect modern distribution or compatibility. Do not claim successful device behavior from a source citation alone. Proposed answer: `docs/faq/09-development-openness.md#how-do-i-register-a-sony-smarteyeglass-app-so-smart-connect-recognizes-it`. **State: researched, publication pending public-page and directory-link verification.** Only then mark Q-000122 as `answered` in the existing registry with the canonical answer URL, publication proof, and date. This evidence packet preserves the original observation and uncertainty.
