# EV-0063 — Recon Jet family post-shutdown service-survival matrix

**Status:** Source boundary completed; hands-on confirmation still required  
**Models:** GLS-0123 Recon Jet; GLS-0124 Jet Pro; GLS-0125 Jet Pro+  
**Reviewed:** 2026-08-15

## Question

What survives locally after Recon Engage/Uplink shutdown, and which ownership failures are directly established rather than inferred?

## Findings

The original Jet manual makes first-run activation an explicit gate: create a Recon Engage account, install Recon Uplink, connect Jet, sign in, link the device, and update it before use. Intel later confirmed it stopped supporting Engage and the Jet, Jet Pro and Jet Pro+ products. Owners reported that offline Engage servers prevented new devices from passing activation.

This is a concrete service-terminal failure, not merely discontinued support. However, the same manual documents substantial onboard functions—menus, camera, gallery, music player, compass, maps, sensors and local Android applications. Those functions are architecturally local **after activation**; the sources do not prove that an unactivated or factory-reset unit can reach them.

## Function-by-function matrix

| Function | Activated unit | New/reset unit after shutdown | Evidence boundary |
|---|---|---|---|
| Power, display and local UI | Documented local operation | Activation screen can block menu access | Manual + owner reports |
| Camera and Gallery | Preloaded local apps documented | Unavailable if activation gate is not bypassed | Manual; no current hands-on test |
| Music Player / Compass / Maps | Preloaded apps documented | Gate-dependent | Manual; map freshness unknown |
| GPS and activity metrics | On-device sensors documented; AGPS optional | Gate-dependent; slower standalone fix plausible but untested | Manual separates GPS from phone-assisted AGPS |
| ANT+ sensors | Local external-sensor path documented | Gate-dependent | Manual/developer record |
| Phone notifications / assisted GPS | Recon Engage mobile app required | Service/app path impaired | Manual + shutdown record |
| Activity upload, history, social sharing | Engage/Uplink required | Dead service path | Manual + server-loss reports |
| Third-party apps | Original SDK/application surface documented | Preservation/sideload route uncertain | Historical developer record |
| Firmware update | Uplink workflow documented | Current vendor update path unavailable | Manual + Intel end-of-support |
| Activation / account registration | Engage/Uplink mandatory in manual | Confirmed failure mechanism after servers went offline | Manual + Intel support thread |

## Community recovery boundary

A 2024 owner follow-up reports success using an XDA community method. A separate open-source preservation issue records that an “Un-blocker” application could install on a Jet but did not clear activation after reboot in that tester's case. These are valuable recovery leads, not a reproducible GlassesResearch verification. No universal bypass, preserved signed image or safe factory-reset procedure is claimed.

## Model scope

Intel's support statement explicitly names Jet, Jet Pro and Jet Pro+, so the service-loss warning applies across the family. The detailed original manual and community bypass evidence concern Jet. Pro and Pro+ must not inherit every local function or recovery result without model-specific manuals or hands-on tests.

## Scoring effect

- **GLS-0123:** Cloud Independence remains 4.5: rich local architecture exists, but mandatory first activation can strand reset/new hardware.
- **GLS-0124 / GLS-0125:** provisional Cloud Independence 4.0 remains appropriate because family-wide service loss is established while generation-specific local recovery is not.
- Historical SDK openness does not erase a present-day activation dependency.

## Sources

- [Recon Jet owner manual preserved in FCC exhibit](https://fcc.report/FCC-ID/ZW5009/2538430.pdf)
- [Intel support: activation failure and discontinued Jet-family support](https://community.intel.com/t5/Wireless/How-to-bypass-the-recon-jet-activation-screen/m-p/1379242)
- [Intel community record: Engage servers offline](https://community.intel.com/t5/Wireless/Recon-Engage-Call-to-all-customers/td-p/1256845)
- [Community activation preservation issue](https://github.com/recom3/api-hud-goggle/issues/6)
- [Historical Recon Jet developer kit preservation](https://theiotlearninginitiative.gitbook.io/codelabs/gods/ah-puch/recon-instruments/intel-developer-zone/recon-dev-kit-for-jet)

## Required hands-on follow-up

Test one previously activated Jet and one factory-reset/new Jet. Record firmware, activation state, boot path, ADB/USB visibility, camera/gallery/music/GPS/ANT+ behavior, application installability and whether the recovery method survives reboot. Do not factory-reset a working preservation unit without a recoverable image.
