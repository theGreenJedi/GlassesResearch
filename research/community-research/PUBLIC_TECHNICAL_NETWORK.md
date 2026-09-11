# Public Technical Network Map

Purpose: track public technical contributors, projects and discussion nodes that materially improve GlassesResearch investigations. This is **not** a personal-profile system. It records only public technical work, project participation, stated technical interests and evidence relevant to smart-glasses research.

## Current high-signal nodes

| Node | Public technical signal | GlassesResearch relevance | Status / disposition |
|---|---|---|---|
| `Panny777` | Maintains `Meizu-Myvu-Client` and `Meizu-Myvu-SDK`; documented MYVU / Star Air XGA010C transport, pairing, relay and feature behavior. | Primary MYVU/XGA010C reverse-engineering source and anchor for MYVU Open Research. | Continue monitoring repository changes, issues, forks and technically relevant interactions. Preserve upstream attribution. |
| `FerSaiyan` / CyanBridge | Maintains `Alternative-HeyCyan-App-and-SDK`; active HeyCyan interoperability research and downstream MYVU integration using Panny777's work. | Important bridge between protocol research and owner-usable companion software; useful for W610/HeyCyan lineage and cross-project reuse. | Continue monitoring releases, issues and hardware-validation notes. Distinguish downstream adoption from independent confirmation. |
| `vladislavkyzmenkov304-cpu` | Public participant in CyanBridge issue #5; supplied a concrete CY01 owner test with reproducible device-state observations and follow-up compatibility data. | High-value owner-testing signal for CY01 / HeyCyan compatibility research. | Track future public technical results, especially exact hardware identity and cross-device comparison. Do not generalize one specimen to the family. |
| `jacob-kruger-work` | Opened CyanBridge issue #5 and repeatedly supplied test requirements, build/test feedback and interoperability use cases around device video access. | Useful source of reproducible test scenarios and owner-facing interoperability requirements. | Track technically substantive follow-ups and resulting implementation/test evidence. |
| `mariaolivafrei-sys` | Opened CyanBridge issue #16 with an exact AX01/WIFIAX01 hardware, firmware and app-version tuple. | Valuable lineage/compatibility fingerprint for a HeyCyan-compatible device. | Preserve the identity tuple as community-reported evidence; await corroboration before lineage assignment. |

## Project relationships currently worth following

- [Panny777/Meizu-Myvu-Client](https://github.com/Panny777/Meizu-Myvu-Client)
- [Panny777/Meizu-Myvu-SDK](https://github.com/Panny777/Meizu-Myvu-SDK)
- [FerSaiyan/Alternative-HeyCyan-App-and-SDK](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK)
- [ebowwa/HeyCyanSmartGlassesSDK](https://github.com/ebowwa/HeyCyanSmartGlassesSDK)
- [aimindseye/rokid-ai-glasses](https://github.com/aimindseye/rokid-ai-glasses)

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