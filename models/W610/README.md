# W610 Model Chapter

This directory is the dedicated research chapter for the W610 smart-glasses platform and closely related W610-branded retail variants.

## Begin with a question

Use [`QUESTIONS.md`](QUESTIONS.md) as the human-facing entrance. It organizes the chapter around practical questions rather than requiring readers to understand the file hierarchy first.

## Scope

This chapter collects everything specific to the W610:

- physical hardware, components, measurements, repair, and optics
- BLE behavior and protocol research
- firmware and update mechanisms
- companion applications, SDKs, APIs, and integrations
- open hacking, owner control, and vendor-independence research
- manufacturing and supply-chain intelligence
- diagnostics and reproducible test procedures
- diagrams and schematics
- photographs, manuals, listings, captures, and other evidence
- model-specific resources and communities
- chronology, hardware genealogy, and research history
- open questions and a living research backlog

## Current baseline

Known observations from the received unit include:

- Bluetooth name observed as `HeyCyan Glasses`
- electronics concentrated primarily in the right temple
- two controls on the right temple, with the rear control used for power
- status LED near the hinge
- startup tone and brief LED activity during power-on
- vendor application intentionally avoided during initial community-oriented testing

These observations are provisional until tied to dated evidence or repeated tests.

## Primary navigation

- [Questions](QUESTIONS.md)
- [Open-hacking dossier](hacking/README.md)
- [Research backlog](RESEARCH_BACKLOG.md)
- [Timeline](TIMELINE.md)
- [W6xx genealogy](GENEALOGY.md)
- [Community map](COMMUNITY_MAP.md)

## Technical chapter map

- [Open hacking and vendor independence](hacking/README.md)
- [Hardware](hardware/README.md)
  - [Component database](hardware/COMPONENTS.md)
- [BLE and protocol](ble/README.md)
- [Firmware](firmware/README.md)
- [Software, apps, and SDKs](software/README.md)
- [Manufacturing intelligence](manufacturing/README.md)
  - [Manufacturing intelligence map](manufacturing/INTELLIGENCE_MAP.md)
- [Diagnostics](diagnostics/README.md)
- [Diagrams and schematics](engineering/README.md)
- [Evidence archive](evidence/README.md)
- [Resources](resources/README.md)
- [Research log](research-log/README.md)

## Hacking publication rule

Only procedures verified working on an identified device environment may appear as working guides. Community leads and plausible methods remain clearly labeled **Not Verified Yet** until qualifying reproduction and evidence are complete.

## Evidence rule

Every factual claim should identify its basis where practical: direct observation, repeated experiment, captured data, manufacturer material, regulatory filing, retail listing, community report, or inference. Inferences must be labeled. Follow the repository-wide [`Evidence and Confidence Standard`](../../docs/EVIDENCE_STANDARD.md).
