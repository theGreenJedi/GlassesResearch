# Android XR — populated research fields

This record applies the GlassesResearch evidence frameworks to Android XR as a platform lineage rather than a single hardware model.

## Evidence base

Primary evidence includes the official Android XR developer hub (`EV-0031`) and official OpenXR documentation (`EV-0032`).

## Platform architecture

Android XR is a software/platform lineage intended to support multiple XR hardware classes, including glasses. Hardware capabilities therefore must not be inherited automatically across devices merely because they run Android XR.

## Developer access

Google documents first-party development routes and OpenXR support. This is strong evidence for application portability and a formal developer ecosystem.

Application development does not establish device-specific firmware access, bootloader policy, unrestricted sensor access or owner replaceability of system services.

## Connectivity, sensing and display

These are device-specific. Android XR can provide common APIs, but each hardware implementation must still document radios, sensors, display architecture and what the developer can actually access.

## Owner control and cloud independence

The platform structure is potentially favorable to local applications and cross-device software portability. Exact account requirements, vendor overlays, local inference, cloud dependencies and software installation policies remain device-specific.

## Report-card implications

- Software: strong platform-level development support.
- Openness: positive at the application/API layer due to Android XR and OpenXR.
- Owner Control: cannot be generalized across hardware vendors.
- Cloud Independence: potentially strong for local applications, but vendor services may vary.
- Hackability: platform familiarity and standard APIs are positive signals; low-level access remains hardware-specific.

## Unknowns retained

Bootloader policy, firmware replacement, system privileges, repairability, prescription serviceability, battery behavior and vendor-specific cloud/account dependence must be populated per device.