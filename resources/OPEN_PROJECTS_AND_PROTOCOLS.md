# Open Projects, Protocols, and Developer Resources

Last reviewed: 2026-08-05

This ledger records substantive public projects that expose source code, protocol information, hardware design files, developer interfaces, or preservation-worthy implementation history for smart glasses.

Inclusion does **not** mean GlassesResearch has tested the project. Each entry identifies the evidence lane and explains what the source actually contributes.

## How to read this ledger

- **Project-primary** means the source is maintained by the organization responsible for the project or platform.
- **Community** means the source is maintained by an independent developer or community.
- **Archived** means the project remains useful for historical or technical research but is no longer the active upstream.
- **License** is reported from the source repository when visible. `Check upstream` means the project must be inspected before reuse or redistribution.

## Cross-device operating systems and application platforms

| Project | Evidence lane | Models / scope | License | Substantive content | Research value |
|---|---|---|---|---|---|
| [MentraOS](https://github.com/Mentra-Community/MentraOS) | Project-primary / community | Mentra Live, Even Realities G1 and G2, Vuzix Z100, additional devices in development | MIT | Mobile runtime, cloud services, TypeScript SDK, MiniApp framework, device integrations, build instructions, releases, and compatibility claims | One of the strongest public examples of a hardware-agnostic smart-glasses application layer. It is particularly useful for comparing how different glasses expose display, camera, microphone, speaker, and sensor capabilities through a common API. |
| [MentraOS developer documentation](https://docs.mentraglass.com/) | Project-primary | MentraOS application and platform development | Documentation terms; check upstream | SDK concepts, MiniApp development, platform architecture, deployment, and contribution guidance | Canonical companion to the code repository and necessary for understanding intended interfaces versus implementation details. |
| [ARCHIVED_CONVOSCOPE](https://github.com/Mentra-Community/ARCHIVED_CONVOSCOPE) | Community / archived | Earlier AugmentOS / MentraOS lineage; Vuzix Z100, Vuzix Shield, INMO Air, RayNeo X2, Android glasses | Check upstream | Historical application platform, supported-hardware notes, Android requirements, and early cross-device architecture | Preserves the lineage leading into MentraOS and documents devices and assumptions that may have disappeared from current documentation. Treat compatibility claims as historical until reverified. |
| [OpenGlass](https://github.com/BasedHardware/OpenGlass) | Community / archived | DIY camera glasses built from off-the-shelf components | Check upstream | ESP32-S3-based wearable camera design, enclosure files, software, component list, and setup path | Useful low-cost reference architecture and a record of the project before development moved to Omi. Preserve as history rather than treating it as the active upstream. |
| [Omi](https://github.com/BasedHardware/omi) | Project-primary / community | Wearable AI hardware and software descended in part from OpenGlass | MIT | Firmware, mobile applications, backend components, integrations, and wearable-AI workflows | Important successor project for understanding how an experimental glasses project evolved into a broader wearable platform. Not all Omi hardware is glasses-shaped, so model relationships must be recorded carefully. |

## Open hardware and complete device codebases

| Project | Evidence lane | Models / scope | License | Substantive content | Research value |
|---|---|---|---|---|---|
| [Open Source Smart Glasses](https://github.com/Mentra-Community/OpenSourceSmartGlasses) | Project-primary / community | DIY all-day wearable display glasses | MIT | Mechanical files, electronics and firmware, a Python websocket server, imagery, build history, and releases | A rare complete public stack spanning mechanical, electrical, firmware, and host software. The repository is useful for BOM, architecture, repairability, enclosure, and power-system comparisons. |
| [Brilliant Labs Frame codebase](https://github.com/brilliantlabsAR/frame-codebase) | Project-primary | Brilliant Labs Frame | Check upstream | Firmware and device code for Frame, including hardware-facing implementation | High-value primary evidence for an unusually open commercial smart-glasses platform. Use it to separate marketed capabilities from code-visible capabilities and to map firmware evolution. |
| [Brilliant Labs Frame application examples](https://github.com/brilliantlabsAR) | Project-primary | Frame, Monocle, and related Brilliant Labs products | Mixed by repository | Product codebases, examples, firmware, host applications, and documentation links | The organization is more valuable than any single repository because it preserves relationships among Frame, Monocle, Noa software, firmware, and examples. Each repository still requires its own license and status check. |
| [Brilliant Labs Monocle MicroPython](https://github.com/brilliantlabsAR/monocle-micropython) | Project-primary | Brilliant Labs Monocle | Check upstream | MicroPython port and hardware support for the Monocle wearable display | Important historical bridge between single-eye developer hardware and Frame. It also provides a compact reference for embedded scripting on wearable optical hardware. |
| [OpenGlass: event-based gesture-recognition platform](https://arxiv.org/abs/2606.07431) | Academic primary source | Research smart-glasses prototype using event and frame cameras | Open-source release stated by authors; inspect linked artifacts | Modular hardware architecture, FPC interposer, nRF5340 coordinator, GAP9 RISC-V processing, power management, gesture-recognition pipeline, latency and battery measurements | A 2026 research platform with measured results rather than only a concept. The paper reports up to 11.8 hours of continuous on-device ML from a 200 mAh battery and describes released hardware, firmware, and models. Repository links should be captured from the paper and preserved separately. |

## Reverse-engineered BLE protocols and independent control libraries

| Project | Evidence lane | Models / scope | License | Substantive content | Research value |
|---|---|---|---|---|---|
| [even_glasses](https://github.com/emingenc/even_glasses) | Community | Even Realities G1 | GPL-3.0 | Python package for scanning, connecting, sending text, receiving status, RSVP display experiments, notifications, and examples | Concrete independent control code for G1. It is more useful than a generic product link because it demonstrates accessible BLE behavior and exposes executable examples. Claims remain community-sourced until independently reproduced. |
| [Even G2 protocol documentation](https://github.com/i-soxi/even-g2-protocol) | Community | Even Realities G2 | Check upstream | BLE service and packet reverse engineering, working-connection status, feature tracking, and collaborative protocol notes | Active protocol work that can become a canonical reference for G2 independence from the official app. Forks should not be counted as independent confirmation of the upstream findings. |
| [Even Realities G1 community resources in MentraOS](https://github.com/Mentra-Community/MentraOS) | Community / platform-primary | Even Realities G1 | MIT | Production device integration inside a cross-device runtime | Complements standalone protocol projects by showing how a larger application framework represents G1 capabilities and constraints. Compare implementation with independent BLE libraries to find convergent evidence. |
| [Vuzix Z100 support in MentraOS](https://github.com/Mentra-Community/MentraOS) | Community / platform-primary | Vuzix Z100 | MIT | Device integration, application runtime support, and compatibility statements | Provides an inspectable third-party implementation path for Z100. It should be compared with Vuzix's official SDK and documentation before conclusions are promoted to verified model facts. |

## Official developer ecosystems worth preserving

These are not necessarily open-source, but they expose public developer interfaces or primary documentation and therefore belong in the content archive.

| Platform | Evidence lane | Canonical entry point | Content to preserve | Current research use |
|---|---|---|---|---|
| Vuzix developer ecosystem | Project-primary | [Vuzix developer center](https://www.vuzix.com/pages/developer-center) | SDK downloads, sample code, supported models, Android requirements, release notes, device setup, and archived documentation | Baseline for enterprise Android glasses and display-only products such as Z100. Record per-model SDK boundaries rather than treating all Vuzix devices as one platform. |
| Snap Spectacles | Project-primary | [Spectacles developer site](https://www.spectacles.com/) | Lens Studio requirements, device generations, SDK and emulator behavior, publishing workflow, system capabilities, and release history | Strong example of a vertically controlled standalone AR platform. Historical generations should be preserved because the current developer surface may supersede older documentation. |
| XREAL developer ecosystem | Project-primary | [XREAL developer portal](https://developer.xreal.com/) | NRSDK versions, supported glasses and host devices, Unity requirements, tracking modes, firmware dependencies, and release notes | Necessary for distinguishing simple USB-C display behavior from features requiring XREAL software, compatible hosts, or spatial-computing accessories. |
| Rokid developer ecosystem | Project-primary | [Rokid developer site](https://developer.rokid.com/) | SDKs, Android/XR documentation, supported hardware, sample applications, account requirements, and regional differences | Useful for mapping the boundary between display glasses, Android compute accessories, and standalone AR devices in the Rokid family. |
| Meta Project Aria | Project-primary / research | [Project Aria documentation](https://facebookresearch.github.io/projectaria_tools/) | Device tooling, datasets, sensor calibration, data formats, machine-perception libraries, research publications, and sample code | One of the most substantial public research ecosystems around sensor-rich glasses. Project Aria is not a consumer Ray-Ban Meta product, so research findings must not be transferred between them without evidence. |
| Google Glass Enterprise Edition | Project-primary / historical | [Glass Enterprise developer documentation](https://developers.google.com/glass-enterprise) | Enterprise APIs, Android development model, hardware generations, migration and end-of-life notices | Critical historical evidence for one of the earliest commercial smart-glasses platforms and for studying product discontinuation, enterprise deployment, and software decay. |

## Research repositories and datasets

| Resource | Evidence lane | Scope | Substantive content | Research value |
|---|---|---|---|---|
| [Project Aria Tools](https://github.com/facebookresearch/projectaria_tools) | Project-primary / research | Project Aria | Open tools for reading, calibrating, visualizing, and processing Aria data | Enables reproducible work with a major egocentric sensing platform and should be linked from any Aria model or research chapter. |
| [EgoZero](https://arxiv.org/abs/2505.20290) | Academic primary source | Robot learning from Project Aria recordings | Method, evaluation, code and project links for deriving robot policies from human demonstrations | Demonstrates a high-value downstream use of glasses data beyond consumer assistance. It belongs in the research library rather than the buyer guide. |
| [VisionClaw](https://arxiv.org/abs/2604.03486) | Academic primary source | Always-on agent workflows using Meta Ray-Ban glasses | Architecture and user studies connecting egocentric perception with action-taking agents | Useful evidence for emerging agentic use cases, while also raising privacy, consent, latency, and cloud-dependence questions that should be tracked separately. |

## Abandoned, renamed, and successor relationships

| Earlier project | Successor / current direction | Evidence | Why preserve both |
|---|---|---|---|
| OpenGlass by Based Hardware | [Omi](https://github.com/BasedHardware/omi) | The OpenGlass repository states that development moved to Omi | The original repository contains glasses-specific design history that may not remain visible in the broader successor. |
| Convoscope / AugmentOS-era work | [MentraOS](https://github.com/Mentra-Community/MentraOS) | The archived repository identifies itself as old work now represented by the newer platform | Old compatibility lists, Android assumptions, and architecture decisions are historically useful and may explain current implementation choices. |
| Team Open Smart Glasses hardware work | MentraOS and newer Mentra ecosystem projects | The open-hardware repository explicitly points readers toward the later software-platform effort | The hardware repository remains a complete mechanical/electrical reference even though the community's primary software focus changed. |
| Brilliant Labs Monocle | Brilliant Labs Frame | Both remain represented in the official GitHub organization | Preserving both shows the technical progression from a compact monocular developer device toward consumer-shaped glasses. |

## Immediate preservation targets

The following material is sufficiently substantive to justify preservation work now:

1. Release metadata, tags, licenses, and repository inventories for MentraOS, Open Source Smart Glasses, Brilliant Labs Frame, Monocle MicroPython, Omi, and archived OpenGlass.
2. A normalized capability map for Even G1 and G2 protocol work: connection, display writes, notifications, status, input, firmware/update behavior, and unresolved features.
3. Build prerequisites and platform dependencies for official Vuzix, XREAL, Rokid, Snap, and Project Aria developer environments.
4. Successor-history records so renamed or abandoned projects do not disappear from the research graph.
5. Paper-to-artifact records for OpenGlass event-camera research, EgoZero, and VisionClaw, including code, datasets, hardware files, and licenses.

## Evidence cautions

- A GitHub repository proves that code or documentation was published; it does not prove that every listed feature works on every hardware revision.
- Repository forks are preservation copies or development branches, not independent confirmations.
- Compatibility statements can become stale quickly. Record the source date and software release whenever possible.
- Official developer documentation is primary evidence for intended behavior, while independent implementations are evidence for observed or reverse-engineered behavior. They answer different questions.
- Never copy firmware, APKs, datasets, CAD, or documentation into this repository until license and redistribution status are recorded.
