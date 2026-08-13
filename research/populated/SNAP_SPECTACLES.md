# Snap Spectacles — populated research fields

This record applies the GlassesResearch evidence frameworks to current Snap Spectacles development hardware.

## Evidence base

Primary evidence includes the official Spectacles developer portal (`EV-0018`), the official API compatibility list (`EV-0019`), and public sample code (`EV-0020`).

## Product architecture

Current Spectacles are spatial-computing/AR glasses built around first-party development through Snap's Lens Studio ecosystem. Confidence: confirmed from vendor-primary evidence.

## Developer access

Snap provides official development documentation, API compatibility information and sample code. This is strong evidence of a supported application-development environment.

The public developer environment should not be conflated with unrestricted owner control. Firmware access, bootloader access, replacement operating systems, unrestricted sensor access and custom system services require separate evidence.

## Display and sensing

AR display capability is central and HUD/display is therefore applicable. Sensor access should be recorded API by API from the compatibility documentation rather than inferred from hardware marketing.

## Visual AI

Computer-vision and spatial capabilities may support visually aware experiences, but Visual AI should be scored from documented user-facing perception and reasoning functions rather than from the presence of AR sensors alone.

## Cloud and account dependence

Development and distribution are tightly associated with Snap's software ecosystem. Exact offline runtime behavior, account requirements, service dependence and what survives if cloud services are unavailable should be measured explicitly.

## Owner control

Application-level access is substantial within the supported platform. System-level owner control is not established by the current evidence base and remains unknown where undocumented.

## Report-card implications

- Hardware: strong evidence for advanced AR/display architecture, with exact values kept model-specific.
- HUD: applicable and central.
- Software: mature first-party development tooling is a positive signal.
- Openness: meaningful SDK/API access, but within a controlled platform.
- Owner Control: lower confidence beyond application-layer development.
- Cloud Independence: unresolved and should not be inferred from SDK availability.
- Hackability: supported app development is strong; low-level modification remains a separate question.

## Unknowns retained

Firmware replacement, bootloader state, unrestricted sensor access, repairability, prescription serviceability, battery aging, long-term platform survival and precise offline capability remain open research questions.