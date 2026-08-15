# EV-0064 — Magic Leap 1 destructive service-shutdown matrix

**Status:** Vendor-confirmed destructive shutdown; post-shutdown hardware probing still required  
**Scope:** Magic Leap One: Creator Edition / Magic Leap 1 (adjacent head-worn AR control)  
**Shutdown date:** 2024-12-31  
**Reviewed:** 2026-08-15

## Question

Which functions were explicitly destroyed by Magic Leap's service shutdown, and is any owner-usable local residue established after the shutdown?

## Finding

Magic Leap's current end-of-life notice states that Magic Leap 1 no longer receives OS updates or Care support, its cloud services are unavailable, and the device and apps' core functionality has reached end-of-life. The more detailed vendor FAQ preserved in Magic Leap's developer forum made the mechanism explicit:

- Device Manager, Private App Sharing, and Backup and Restore cease to function.
- Developer and publishing certificates can no longer be created or renewed, preventing application installations and updates.
- Devices require annual re-authentication.
- Magic Leap Identity shutdown prevents that re-authentication.
- Magic Leap stated that the device and apps would cease to function.

This is the catalog's destructive-shutdown control. The failure is not merely the disappearance of optional cloud content; identity and certificate infrastructure controlled continued device and application use.

## Function-by-function matrix

| Function | After 2024-12-31 | Evidence boundary |
|---|---|---|
| Magic Leap Identity / annual re-authentication | Unavailable | Explicit vendor FAQ |
| Device Manager | Unavailable | Explicit vendor FAQ |
| Private App Sharing | Unavailable | Explicit vendor FAQ |
| Backup and Restore | Unavailable | Explicit vendor FAQ |
| New developer/publishing certificates | Cannot be created or renewed | Explicit vendor FAQ |
| Application installation and updates | Prevented when certificates cannot be created/renewed | Explicit vendor FAQ |
| OS updates | Ended | Current vendor EOL notice |
| Customer Care / warranty | Ended | Current vendor EOL notice |
| Existing installed applications | Vendor stated device and apps cease to function | Strong vendor claim; per-app post-shutdown testing not preserved |
| Boot, display, controller, sensors and local shell | No durable owner-usable behavior established by current source packet | Must remain unknown pending hands-on evidence |
| Offline owner-developed software | No supported renewal/install path; continued execution is not established | Do not infer survival from the formerly local architecture |

## What this proves

Magic Leap 1 demonstrates that an apparently self-contained wearable computer can be rendered practically unusable by:

1. recurring identity re-authentication;
2. vendor-controlled signing certificates; and
3. cloud-mediated device/application management.

A product can therefore score well for local compute at launch while still having poor lifetime Cloud Independence and Owner Control.

## What this does not prove

- It does not prove that every component is electrically bricked or that the device cannot boot.
- It does not establish a lawful, reproducible community bypass.
- It does not establish that an already authenticated unit retains useful operation beyond a particular date.
- It does not transfer automatically to Magic Leap 2, whose AOSP/OpenXR/application-management architecture is different.
- It does not add Magic Leap 1 to the 145-model smart-glasses count; it remains an adjacent AR control case.

## Research effect

Magic Leap 1's Cloud Independence anchor remains 3.0 and Owner Control 4.0. Those scores recognize real onboard compute and historical developer tooling, but the shutdown mechanism proves that the owner lacked durable authority over identity, signing and continued application use.

The source-acquisition portion of this control is complete. Remaining work is empirical preservation research: boot an authenticated unit and a reset/expired unit; record firmware, clock state, authentication prompt, installed-app behavior, USB/ADB visibility, certificate dates, local media access and network endpoints. Do not reset a surviving authenticated unit without a restorable image.

## Sources

- [Magic Leap 1 current end-of-life notice](https://www.magicleap.care/hc/en-us/articles/18878883445645-Magic-Leap-1-End-of-Life)
- [Magic Leap developer-forum preservation of the detailed EOL FAQ](https://forum.magicleap.cloud/t/magic-leap-1-end-of-life-and-ability-to-compile-and-run-own-apps/3660)
- [Heru customer notice confirming application-function loss](https://kb.seeheru.com/eol)
