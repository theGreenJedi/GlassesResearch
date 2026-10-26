# Public Technical Network Map

Purpose: track public technical contributors, projects and discussion nodes that materially improve GlassesResearch investigations. This is **not** a personal-profile system. It records only public technical work, project participation, stated technical interests and evidence relevant to smart-glasses research.

## Current high-signal nodes

| Node | Public technical signal | GlassesResearch relevance | Status / disposition |
|---|---|---|---|
| `Panny777` | Maintains `Meizu-Myvu-Client` and `Meizu-Myvu-SDK`; documented MYVU / Star Air XGA010C transport, pairing, relay and feature behavior. | Primary MYVU/XGA010C reverse-engineering source and anchor for MYVU Open Research. | Continue monitoring repository changes, issues, forks and technically relevant interactions. Preserve upstream attribution. |
| `BimaPDev` | Maintains `SmartGlasses`; public XGA010C firmware analysis with hardware-tested modified firmware, PSRAM Thumb/compiled-C execution, BLE file-transfer mapping, and post-flash iOS/ANCS bond diagnostics. | High-signal firmware/owner-control source complementary to Panny777's application/protocol work. | Continue monitoring commits and technical interactions. Treat hardware-test reports as community-primary until GlassesResearch reproduces them. |
| `FerSaiyan` / CyanBridge | Maintains `Alternative-HeyCyan-App-and-SDK`; active HeyCyan interoperability research and downstream MYVU integration using Panny777's work. | Important bridge between protocol research and owner-usable companion software; useful for W610/HeyCyan lineage and cross-project reuse. | Continue monitoring releases, issues and hardware-validation notes. Distinguish downstream adoption from independent confirmation. |
| `vladislavkyzmenkov304-cpu` | Public participant in CyanBridge issue #5; supplied a concrete CY01 owner test with reproducible device-state observations and follow-up compatibility data. | High-value owner-testing signal for CY01 / HeyCyan compatibility research. | Track future public technical results, especially exact hardware identity and cross-device comparison. Do not generalize one specimen to the family. |
| `jacob-kruger-work` | Opened CyanBridge issue #5 and repeatedly supplied test requirements, build/test feedback and interoperability use cases around device video access. | Useful source of reproducible test scenarios and owner-facing interoperability requirements. | Track technically substantive follow-ups and resulting implementation/test evidence. |
| `mariaolivafrei-sys` | Opened CyanBridge issue #16 with an exact AX01/WIFIAX01 hardware, firmware and app-version tuple. | Valuable lineage/compatibility fingerprint for a HeyCyan-compatible device. | Preserve the identity tuple as community-reported evidence; await corroboration before lineage assignment. |

| `Iam5tillLearning` / OpenSource-Ai-Glasses | Maintains an Apache-2.0 embedded-Linux smart-glasses project targeting RV1106B hardware, with public C/C++ SDK, BLE/SPP and Wi-Fi control, RTSP camera streaming, optional display support, firmware and an Android companion client. [v0.7.2 release](https://github.com/Iam5tillLearning/OpenSource-Ai-Glasses/releases/tag/v0.7.2) was published August 24, 2026; the upstream README warns that later firmware builds require hardware manufactured after January 1, 2026. | Adjacent owner-control and open development reference: compare reproducible build artifacts, firmware/hardware revision gating, protocol access and camera data path against closed-platform clients. No demonstrated MYVU lineage or interoperability. | **Project-primary code/release and developer documentation verified present; runtime and compatibility claims not GlassesResearch hardware-verified.** Preserve release artifacts/compatibility caveat, inspect SDK interfaces and test on identified hardware before claiming working features. |
| `macedonga` / Visor | Maintains [Visor](https://github.com/macedonga/visor), an independent Android companion for Meta smart glasses. October 23–25 code documents reverse-engineered camera orientation, on-phone video processing, segmented assistant messages and media deletion. | Adjacent owner-control, transport and data-lifecycle reference; **not** a MYVU/XGA010C lineage connection. | **Inspectably committed source; individual features vary between upstream hardware-tested and explicitly untested.** Follow reproducible owner testing, media retention safeguards and protocol-version gating. |

| `v-modal` / VModal Smart Glass SDK | Maintains [vmodal_sdk_smartglass](https://github.com/v-modal/vmodal_sdk_smartglass), an Android/Meta DAT camera-streaming SDK. [October 20 commit `da21728`](https://github.com/v-modal/vmodal_sdk_smartglass/commit/da217283a3187b9c64b490bfedb402aacf0a6931) adds an independent speech-to-image-search/display example and Meta Mock Device Kit integration tests; the example expressly says physical glasses and live-collection acceptance are pending. | Relevant to phone-hosted visual AI, capture ownership, stream lifecycle and explicit simulator-vs-hardware evidence boundaries; **no MYVU interoperability implied**. | **Public source/CI implementation confirmed; runtime behavior on real glasses not verified.** Follow physical acceptance, permissions, session cleanup, network handling and cloud data flow before promoting feature claims. |

## Project relationships currently worth following

- [Panny777/Meizu-Myvu-Client](https://github.com/Panny777/Meizu-Myvu-Client)
- [Panny777/Meizu-Myvu-SDK](https://github.com/Panny777/Meizu-Myvu-SDK)
- [BimaPDev/SmartGlasses](https://github.com/BimaPDev/SmartGlasses)
- [FerSaiyan/Alternative-HeyCyan-App-and-SDK](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK)
- [ebowwa/HeyCyanSmartGlassesSDK](https://github.com/ebowwa/HeyCyanSmartGlassesSDK)
- [aimindseye/rokid-ai-glasses](https://github.com/aimindseye/rokid-ai-glasses)
- [Iam5tillLearning/OpenSource-Ai-Glasses](https://github.com/Iam5tillLearning/OpenSource-Ai-Glasses)

## Evidence rules

- Public participation is a **signal to inspect the work**, not a credibility score by itself.
- Praise, criticism and project popularity carry no automatic evidentiary weight.
- A repeated technical contributor can be useful without being treated as an authority.
- Owner tests remain community-reported until GlassesResearch reproduces them.
- A fork, star, follow or comment is not evidence of technical agreement.
- Record only information needed to understand the public technical contribution; do not infer private relationships, sensitive traits or unrelated personal information.

## Current watch items

1. MYVU/XGA010C protocol or hardware revisions that change Panny777's documented behavior.
2. HeyCyan/CY01/AX01 compatibility evidence that clarifies whether current differences are branding, firmware branches, protocol differences or materially different hardware.
3. Independent reproduction of CyanBridge findings on identified hardware.
4. New public smart-glasses projects that materially overlap with protocol, firmware, teardown, sourcing, owner-control or interoperability research.
5. Public mentions of GlassesResearch or glassesresearch.org that contain factual corrections, criticism, useful citations, adoption signals, contributor opportunities or misunderstandings requiring clarification.

## GlassesResearch mention handling

When a public mention is found, preserve the public source and classify the substance before deciding whether to act:

- **Correction needed** — investigate promptly and correct the record if warranted.
- **Useful criticism / methodology feedback** — evaluate on substance and fold into process when justified.
- **Citation / adoption** — record only when it materially demonstrates research reuse or exposes a new technical audience.
- **Contributor/contact opportunity** — consider outreach when the person's public technical work directly overlaps an active investigation.
- **Misunderstanding** — clarify publicly only when the misunderstanding is material enough to affect the research record.

No meaningful external public mention of GlassesResearch was established in the most recent review pass.

### October 25, 2026 — Visor import deletion and segmented assistant messages

**Primary-source technical evidence (new since the October 20 Visor watch entry):**

- [October 24: assistant message segmentation, commit `f9069f9`](https://github.com/macedonga/visor/commit/f9069f92569edeb7f1223df0a61314f347ef25d9): Visor's developer documents Meta protocol-version gating and a 1,024-byte threshold, with segmented message types 1002/1003 for long AI events. The commit explains that a multi-byte-language answer can exceed the threshold even when its visible text is short. **Status:** directly inspectable source/author's protocol analysis; author explicitly says *not tried on the glasses yet*. Do not claim verified repair of the reported Korean/Russian silent-answer problem.
- [October 24: media stabilization and landscape handling, commit `8453483`](https://github.com/macedonga/visor/commit/8453483c08c1036c7d8be1c419b25d3d4d2d2533): adds phone-side motion-based stabilization for video not already stabilized by glasses. The developer reports a measured 1080p walk on their specimen, but states 3K moving-video calibration is not checked. **Status:** upstream code and developer-reported specimen measurement; not independently reproduced by GlassesResearch.
- [October 25: capture deletion after import, commit `5b81993`](https://github.com/macedonga/visor/commit/5b81993ee2058c2de444db2f568e6c7c7cb23932): adds media service 18/type 3 delete-by-handle, type 4 success and type 5 failure handling; requests deletion after phone save and for already indexed/dismissed captures. The stated goal is to avoid glasses storage filling up. **Status:** directly inspectable code and author protocol report; the commit explicitly says *not tried on the glasses*. **Owner-data caution:** deletion is potentially irreversible; confirm file integrity, gallery persistence, deletion acknowledgments and recovery behavior on identified hardware before recommending it as safe.
- [October 24: concurrent transfer channel correction, commit `c4dd5f9`](https://github.com/macedonga/visor/commit/c4dd5f9b4acb5ab191525ca716933adf4ba69d36): distinguishes outgoing-channel answers from unsolicited glasses file offers using the originator bit. **Status:** inspectable code, developer reports not hardware-tested.

**Disposition:** Maintain `macedonga` as an adjacent *public technical project* node, not a personal profile. Prioritize a non-destructive protocol review of message segmentation and a controlled capture-import/deletion safety test with before/after media hashes and recovery steps. Treat the author's measured 1080p behavior separately from untested features. No GlassesResearch hands-on validation or live-site publication is implied by this repository note.

### October 26, 2026 — Visor follow-up turn protocol and VModal integration example

**Material primary-source changes:**

- [Visor October 25 commit `6a4ac0f`](https://github.com/macedonga/visor/commit/6a4ac0f691fbd7f37a0c4203c4f24b07c7bb1263): the maintainer documents `ev60` completion semantics, `shouldSmartFollowUp` (fulfillment result field 11), `requiresAnswer`, and follow-up invocation method 5. In phone-voice mode, omitting completion reportedly left the glasses microphone/listening indicator active and blocked a subsequent question. The change sends turn completion for both voice paths and adds an `end_conversation` tool. **Status:** source and protocol implementation inspectable; developer says phone-voice follow-ups were tried on glasses; glasses-own-voice path and reliable `end_conversation` invocation were *not* established. **Disposition:** record as a hardware-reported protocol clue; add explicit microphone-off and session-termination checks to any independent owner test; do not treat as a universally verified Meta protocol.
- [Visor October 25 commit `ae90d9c`](https://github.com/macedonga/visor/commit/ae90d9ca2859eb8c9fbd843b71d1e85a56f66c7a): repackages third-party Android `MessagingStyle` notifications as messages the displayless Ray-Ban/Oakley glasses can read aloud, preserving reply routing via the source app's action. **Status:** inspectable implementation; maintainer explicitly says *not tried on the glasses*. **Disposition:** track as an unverified interoperability technique, with opt-in notification/privacy and reply-attribution testing before recommending.
- [VModal October 20 commit `da21728`](https://github.com/v-modal/vmodal_sdk_smartglass/commit/da217283a3187b9c64b490bfedb402aacf0a6931): publishes a standalone Android voice-search example that links Meta DAT 1.0.1, speech, VModal rank-one image retrieval and glasses display, with simulator/CI acceptance. [Example README](https://github.com/v-modal/vmodal_sdk_smartglass/blob/main/examples/01_voice_search/README.md) explicitly identifies physical-device and live-search validation as pending. **Status:** project-primary published code and simulator-oriented tests, not independent hardware proof. **Disposition:** add project-level technical node; follow hardware acceptance, capture consent, cloud dependence, streaming backpressure and failure cleanup. No asserted connection to MYVU/XGA010C.

**Scope:** only public technical work and attributed developer testing are recorded. No private profiles, personal inferences or unverified GlassesResearch bench claims.
