# Ray-Ban Meta — populated research fields

This record applies the GlassesResearch evidence frameworks to Ray-Ban Meta smart glasses.

## Evidence base

Primary evidence includes the Ray-Ban Meta operational FAQ (`EV-0027`) and Meta's multimodal AI system documentation (`EV-0028`).

## Product architecture

Ray-Ban Meta is a camera/audio AI-glasses platform with no wearer-facing HUD. Display/HUD is therefore N/A for the current product class.

## Connectivity and software dependence

Vendor documentation establishes Bluetooth/Wi-Fi use, companion-application setup, media transfer and firmware-update behavior. The product is tightly integrated with Meta's companion software ecosystem.

## Visual AI

Meta's system documentation establishes that camera and voice inputs can participate in multimodal AI processing. This is strong evidence that visual input is part of the AI stack, not merely a separate camera feature.

## Cloud independence

Core capture/audio functions and AI functions should be separated. Multimodal AI relies on Meta's service stack, while some local device functions may continue without cloud access. Exact survival behavior should be measured function by function.

## Owner control

Current evidence supports normal user controls and first-party software operation, but does not establish a public owner SDK, custom AI endpoints, firmware replacement or unrestricted sensor access. Those fields remain unknown or unsupported unless additional evidence is found.

## Privacy and institutional research

Because the product combines cameras, microphones and cloud AI in an ordinary-eyewear form factor, recording indicators, media handling, permissions, service retention and institutional restrictions are especially important fields.

## Report-card implications

- Hardware: strong consumer integration evidence, with exact scores kept model-specific.
- Wearability: ordinary-eyewear form factor is a positive structural signal; fit requires evidence.
- HUD: N/A.
- Visual AI: strongly applicable and supported by primary documentation.
- Software: strong first-party ecosystem support.
- Openness: limited evidence for public developer access compared with SDK-oriented competitors.
- Owner Control: custom endpoints/local AI/firmware access are not established.
- Cloud Independence: AI layer is service-dependent; local non-AI functions require separate testing.

## Unknowns retained

Repairability, low-level protocol access, firmware replacement, bootloader state, independent AI endpoint selection, exact offline function survival, battery aging and long-term post-service survivability remain open.