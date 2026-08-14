# EV-0045 — Meta / Ray-Ban / Oakley service-survival boundary

**Verified:** 2026-08-14  
**Evidence class:** Current first-party Ray-Ban and Oakley product/support documentation  
**Scope:** Ray-Ban Meta and Oakley Meta families; generation-specific exceptions remain explicit

## Question

Which functions have a plausible local or phone-level life, and which parts of the Meta smart-glasses experience require Meta's account, application, network or AI services?

## First-run and ownership gate

Ray-Ban and Oakley both state that normal operation requires:

- a compatible Android or iOS smartphone;
- wireless internet access;
- a valid Meta account; and
- the Meta AI companion application.

Initial pairing is completed inside the signed-in application. Ray-Ban states that glasses pair with one Meta account at a time. Transfer to another owner requires factory reset, and factory reset permanently erases captures and account associations.

This is a hard activation/ownership dependency, not merely an optional AI feature.

## Function-by-function boundary

| Function | Device/phone-local evidence | Service/application dependency | Survival conclusion |
|---|---|---|---|
| Wearing as ordinary eyewear | Physical frame and fitted lenses remain | None for passive optics | Survives |
| Bluetooth audio from phone | Ray-Ban documents touch control and automatic reconnection to the phone for streamed audio | Requires a compatible Bluetooth source; service-specific music catalogs remain separate | Likely survives as a phone peripheral after setup; post-account-loss behavior still requires testing |
| Photo/video capture | Gen 2 product documentation lists 32 GB storage and more than 500 photos or 100+ 30-second videos; return/reset instructions require importing captures before reset | Setup/account gate remains; exact capture behavior after sign-out or backend loss is not documented | Hardware/local-storage capability exists, but service-loss behavior is unverified |
| Media import and management | Captures are retained on the glasses until imported or erased | First-party instructions route import through the Meta AI app; no standard USB mass-storage or documented independent importer is established | Vulnerable to app/platform loss |
| Offline translation | Ray-Ban Meta Gen 2 documentation identifies downloadable offline language packs | Pack download, availability, language coverage and initial setup remain ecosystem-dependent | Narrow partial survival |
| Calls and phone audio | Bluetooth/phone integration is documented | Messaging providers, contacts and companion configuration vary | Basic phone-peripheral value may survive; integrated services may not |
| Meta AI / vision | Defining assistant and multimodal functions are presented through Meta AI | Meta account, application, wireless internet, supported country/language and maintained backend | Does not independently survive service loss |
| Messaging, music, Shazam and fitness integrations | Some transport may be ordinary Bluetooth | Provider linking and supported services are required for integrated commands/results | Provider- and platform-dependent |
| Firmware, settings and device management | Managed through the Meta AI application | No general owner firmware or replacement-management path is documented | High vendor dependence |
| Resale / reassignment | Factory reset allows reassignment while activation infrastructure operates | New owner must pair through Meta account/application; reset destroys unimported captures | Continued vendor activation matters |

## Generation distinctions

- **Ray-Ban Stories** used the earlier Facebook View workflow and should not inherit every current Meta AI conclusion.
- **Ray-Ban Meta Gen 1** and **Gen 2** share the current account/app architecture, but Gen 2 adds larger documented storage, longer battery life and offline translation packs.
- **Oakley Meta HSTN** shares the required phone/account/app/internet checklist.
- **Oakley Meta Vanguard** uses additional fitness integrations; those do not reduce the activation or Meta AI dependency.
- **Meta Ray-Ban Display** adds display and Neural Band dependencies and needs its own delivered-hardware survival test.

## Interpretation

The family is not a single all-or-nothing cloud appliance. Passive eyewear, local storage and ordinary phone-audio pathways provide a residue of durable hardware value. However, activation, capture import, settings, updates and defining visual-AI functions remain tightly tied to the Meta account/application/service stack.

Accordingly, the correct survival label is **dependent with limited local residue**, not “useless without cloud” and not “offline-capable.”

## Required physical tests

1. Complete setup, then block internet while leaving Bluetooth enabled.
2. Test capture button, local storage, playback cues and Bluetooth audio.
3. Test media import with internet blocked.
4. Sign out without resetting and repeat the tests.
5. Block Meta endpoints while preserving LAN/Bluetooth connectivity.
6. Preserve app version, firmware version, phone OS and region.
7. Test whether previously downloaded translation packs function fully offline.
8. Do not factory-reset until every capture and state observation is preserved.

## Primary sources

- [Ray-Ban Meta FAQ](https://www.ray-ban.com/usa/c/frequently-asked-questions-ray-ban-meta-smart-glasses)
- [Ray-Ban Meta Gen 2 product specification](https://www.ray-ban.com/usa/electronics/RW4012ray-ban%20%7C%20meta%20wayfarer-cosmic%20blue/8056262721438)
- [Oakley Meta FAQ](https://www.oakley.com/en-us/oakley-meta-faq)
- [Oakley Meta HSTN product documentation](https://www.oakley.com/en-us/product/W0OW8002)
- [Oakley Meta Vanguard product documentation](https://www.oakley.com/en-us/product/W0OW8001)

## Confidence and limits

High confidence for stated setup/account/application requirements, storage specifications, first-party import/reset workflow and service-linked AI. Medium confidence for post-setup Bluetooth-audio durability because backend-loss behavior is not explicitly tested by the vendor. Offline capture/import behavior remains an empirical test target.
