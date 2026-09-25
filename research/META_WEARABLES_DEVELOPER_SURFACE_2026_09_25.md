# Meta wearable developer surface — 2026-09-25

This note records first-party developer evidence without equating SDK access with openness, owner control, or cloud independence.

## Wearables Device Access Toolkit

Meta documents the Device Access Toolkit as a path for existing iOS and Android applications to connect to supported AI glasses. Current first-party documentation describes access paths for motion, camera, speech/audio, display, and input/gestures, with capability availability varying by device.

Meta's developer FAQ states that Device Access Toolkit 1.0 begins rolling out September 30, 2026 and lists support across Ray-Ban Meta generations, Ray-Ban Meta Display, Oakley Meta HSTN and Oakley Meta Vanguard.

Primary sources:

- https://developers.meta.com/wearables/device-access-toolkit/
- https://developers.meta.com/wearables/
- https://developers.meta.com/wearables/faq/
- https://github.com/facebook/meta-wearables-dat-ios

## Evidence interpretation

This materially expands the documented third-party development surface. It is evidence of **vendor-supported programmability**.

It is not, by itself, evidence of open firmware, unrestricted hardware access, owner-controlled boot/software, service survival, data portability, local inference, or cloud independence. GlassesResearch should continue scoring those independently.

## Meta VR Glasses / external-compute update

Unity documents day-one development support for Meta VR Glasses in Unity 6.6 through OpenXR, with existing Quest projects intended to carry forward with minimal changes and simulator-based development possible before retail hardware arrives.

Primary source:

- https://unity.com/blog/build-for-meta-vr-glasses-with-unity

This strengthens the architectural record: the external-compute glasses are being introduced as part of an existing software/tooling continuum rather than as an isolated hardware prototype. Production performance remains unverified.
