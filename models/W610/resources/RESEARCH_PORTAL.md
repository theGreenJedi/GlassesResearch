# W610 Research Portal

This page contains **resources we actually found** for W610 / HeyCyan research. Generic discovery routes such as “search Reddit,” “check YouTube,” or “look for a Discord” are intentionally excluded from the public portal until a concrete, useful resource is identified.

For the machine-readable source-of-truth, see the [Evidence Corpus](../../../evidence/README.md).

## Concrete community and development resources

| Resource | Type | Why it matters | Evidence state |
|---|---|---|---|
| [HeyCyanSmartGlassesSDK](https://github.com/ebowwa/HeyCyanSmartGlassesSDK) | GitHub SDK / reverse-engineering resource | Cross-platform BLE SDK for HeyCyan-compatible glasses; repository topics explicitly include W610, and the project preserves a manufacturer-original branch. | Community-primary; not yet GlassesResearch reproduced |
| [CyanBridge / Alternative HeyCyan App and SDK](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK) | Alternative Android companion app / SDK | Concrete vendor-app replacement project with media sync, assistant integration, local-AI work, and published APK releases. | Community-primary; not yet GlassesResearch reproduced |
| [CyanBridge releases](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/releases) | Release / APK archive | Versioned release notes and downloadable Android artifacts, including local-AI releases. | Community-primary; preserve metadata and hashes before testing |
| [CyanBridge v2.0.0 local-AI release](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/releases/tag/v2.0.0) | Versioned local-AI release | Names Qwen2.5 0.5B/1.5B for phone-local llama.cpp/GGUF use; multimodal image/audio support is separately attributed to LiteRT Gemma 4 and must not be generalized to Qwen. | Community-primary; not yet GlassesResearch reproduced |
| [CyanBridge v2.0.0 discussion on r/SmartGlasses](https://www.reddit.com/r/SmartGlasses/comments/1sg1fyr/alternative_heycyan_app_massive_release_v200/) | Specific Reddit thread | Concrete community discussion around CyanBridge 2.0.0 and local-AI support; useful for reports, testing feedback, and follow-up leads. | Community-report |
| [CyanBridge v1.0.2 discussion on r/SmartGlasses](https://www.reddit.com/r/SmartGlasses/comments/1qr7n6z/release_use_gemini_chatgpt_with_heycyan_smart/) | Specific Reddit thread | Documents an earlier public release of Gemini / ChatGPT assistant replacement work for HeyCyan-compatible glasses. | Community-report |
| [Cheap W610 always-on voice question on r/SmartGlasses](https://www.reddit.com/r/SmartGlasses/comments/1r88qjl/do_cheap_smart_glasses_support_alwayson_voice/) | Specific Reddit thread | A real W610 owner/buyer question about wake-word versus button-triggered assistant behavior. Useful as a concrete question to test, not proof of behavior. | Community-report |

## Regulatory and identity evidence

| Resource | Type | Why it matters | Evidence state |
|---|---|---|---|
| [FCC ID 2BNVK-W610](https://fccid.io/2BNVK-W610) | FCC equipment authorization | Direct W610 regulatory identity tied to Shenzhen Zhijing Innovation Technology Co., Ltd, with exhibits useful for OEM, radio, label, and hardware research. | Regulatory-primary |
| [W610 label exhibit](https://fccid.io/2BNVK-W610/Label/Label-and-Location-9003637) | FCC label / location document | Concrete W610 label record with applicant, equipment class, certification date, and published file hash. | Regulatory-primary |
| [SANVNET manual record containing W610 source title](https://fccid.io/2BSQU-SANVNET/User-Manual/Users-Manual-8800707) | FCC user manual | The FCC document title explicitly references `W610英文说明书2025-7-21.cdr`, providing concrete rebrand/OEM lineage evidence and a published SHA-256. | Regulatory-primary |
| [Yetrue W100 change-in-ID record](https://fccid.io/2BWON-W100) | FCC change-in-identification record | Explicitly states that W100 is a change in identification of original FCC ID `2BNVK-W610`, providing strong evidence of shared/rebranded hardware lineage. | Regulatory-primary |

## Manufacturer / supplier material

| Resource | Type | Why it matters | Evidence state |
|---|---|---|---|
| [Goodway W610 product/specification page](https://www.goodwaytechs.com/goodway-ai-smart-glasses-with-8mp-camera-real-time-translation-ip65-waterproof-42g-lightweight-w610.html) | Supplier specification | Names W610 directly and publishes chipset, camera, battery, software, firmware-feature, and customization claims. | Vendor-primary; claims require independent verification |

## What is intentionally absent

There is currently **no public placeholder entry** for a W610 Discord, Telegram group, QQ group, YouTube teardown, firmware mirror, or dedicated forum unless GlassesResearch can name and link a concrete resource that has research value.

Those channels remain valid places for **internal discovery work**, but discovery instructions are not evidence and should not appear as if they were populated resources.

## Investigation links

- [W610 Open-Hacking Dossier](../hacking/README.md)
- [W610 Community Map](../COMMUNITY_MAP.md)
- [W610 Genealogy](../GENEALOGY.md)
- [Manufacturing Intelligence Map](../manufacturing/INTELLIGENCE_MAP.md)
- [Evidence Corpus](../../../evidence/README.md)
- [Canonical Glossary](../../../glossary/README.md)

## Promotion rule

When a newly discovered external resource proves useful enough to cite, add it to the evidence corpus with a stable `EV-####` identifier, direct URL, evidence state, last-verified date, and explanation of why it matters. Public pages should then cross-reference that record instead of adding another generic search link.
