# Solos — populated research fields

This record applies the GlassesResearch evidence frameworks to the current Solos AirGo ecosystem.

## Evidence base

Primary evidence includes the official Solos developer SDK (`EV-0026`), covering current AirGo audio and camera glasses.

## Product architecture

Solos spans lightweight audio-first glasses and camera-enabled AI-glasses variants. These should remain separate model classes within one corporate/software lineage rather than inherit capabilities from one another.

## Connectivity and developer access

The official SDK documents supported connectivity and device interaction, including Bluetooth and, on supported models, additional network and camera-related capabilities. This is strong evidence of an intentional developer surface.

SDK availability does not establish unrestricted firmware access, bootloader access or every sensor being exposed.

## Visual AI and sensing

Camera-equipped AirGo variants can support visually aware functions, while audio-only models cannot be assumed to do so. Visual AI must therefore be scored per model from documented camera-assisted behavior.

## Owner control and cloud independence

Public SDK access improves owner/developer control at the application layer. Exact ability to replace the default assistant, choose model endpoints, operate locally, or continue functioning without Solos services remains model- and software-specific.

## Wearability and prescription

The lineage's ordinary-eyewear form factor is a major research dimension. Prescription compatibility, lens replacement, frame options, weight distribution and long-duration comfort should be populated per model rather than inferred from product styling.

## Report-card implications

- Wearability: structurally promising, but needs model-specific fit evidence.
- Visual AI: N/A on audio-only variants; applicable on camera variants.
- Openness: official SDK is a strong positive signal.
- Owner Control: meaningful at application level, unknown at firmware/system level.
- Cloud Independence: unresolved for AI features and account/service dependencies.
- Hackability: stronger than closed consumer-only products because a supported developer interface exists.

## Unknowns retained

Firmware replacement, bootloader state, full sensor exposure, exact offline behavior, subscription dependence, repairability, battery aging, prescription serviceability by model and long-term service survival remain open.