# EV-0036 — Service-survival control cases

Verified: 2026-08-13
Source class: vendor primary / vendor support primary
Confidence: confirmed for stated support/service conditions
Scope: Magic Leap 1, Microsoft HoloLens 1/2, Bose Frames, Recon Jet family

## Magic Leap 1 — destructive shutdown control
Primary source: https://www.magicleap.care/hc/en-us/articles/18878883445645-Magic-Leap-1-End-of-Life

Magic Leap states that authorized purchases ended 2022-12-31. As of 2024-12-31, Magic Leap 1 no longer receives OS updates or Care support, cloud services are unavailable, and the company describes the device and apps' core functionality as end-of-life.

Service-survival interpretation: **Destructive shutdown / end-of-life**. EV-0064 records the exact mechanism: annual Identity re-authentication and certificate-controlled app installation/update fail alongside Device Manager, Private App Sharing and Backup/Restore. Electrical boot or unsupported local residue remains unknown pending hands-on testing.

## Microsoft HoloLens 1 — graceful local-survival control
Primary source: https://learn.microsoft.com/en-us/previous-versions/mixed-reality/hololens-1/hololens1-release-notes

Microsoft states that December 2024 was the final monthly servicing update. After 2024-12-10, HoloLens 1 devices **continue to function**, but receive no further security updates or technical support; there is no out-of-warranty exchange inventory.

Service-survival interpretation: **Discontinued-functional**. Support loss and security aging are real, but the vendor explicitly distinguishes them from device-function loss.

## Microsoft HoloLens 2 — supported security runway after final feature release
Primary source: https://learn.microsoft.com/en-us/hololens/hololens-release-notes

Microsoft documents November 2024 as the final feature release for HoloLens 2 while monthly security servicing continues through December 2027. Windows 10 branches reached their final monthly servicing in December 2024, with Windows 11 recommended for continued servicing.

Service-survival interpretation: **Maintenance / winding down**, not dead. EV-0066 documents local-account offline provisioning, USB/Device Portal application installation and pre-downloaded FFU recovery, while retaining the default network/account OOBE boundary. OS version materially changes support horizon.

## Bose Frames — product discontinued, owner support persists
Primary sources:
- https://www.bose.com/bose-frames
- https://www.bose.com/apps/bose-connect
- https://www.bose.com/apps/bose-app

Bose states Frames are no longer available for purchase on Bose.com but that it still supports owners. Bose Connect still lists Alto/Rondo, and the Bose app lists Tempo/Tenor/Soprano. Core Frames architecture is standard Bluetooth audio; historical Bose AR is a separable software layer.

Service-survival interpretation: **Discontinued-functional / supported-owner**. EV-0065 separates local Bluetooth audio, calls and physical controls from abandoned Bose AR experiences and identifies the remaining reset-pairing/app/firmware tests.

## Recon Jet / Pro / Pro+ — vendor support lost with activation risk
Primary/vendor-support source: https://community.intel.com/t5/Wireless/How-to-bypass-the-recon-jet-activation-screen/m-p/1379242

An Intel Customer Support Technician states Intel stopped support for Recon Engage and Recon Snow2, Jet, Jet Pro and Jet Pro+. The support thread itself concerns bypassing the Jet activation screen, establishing a concrete ownership risk when activation/service infrastructure disappears.

Service-survival interpretation: **Degraded**, with activation/login dependence a specific failure mechanism requiring hands-on or community preservation evidence to determine what can still be recovered locally.

## Comparative lesson
These four cases should calibrate Cloud Independence and lifecycle research:

- End of sales is not end of function.
- End of support is not necessarily end of function.
- End of cloud/account infrastructure can be catastrophic when activation/core apps depend on it.
- Standard local interfaces (Bluetooth, local apps, local OS execution) materially improve survival odds.
- Security/support decay remains a meaningful ownership cost even when core functions survive.

Service status must therefore be function-specific and dated rather than inferred from a single `legacy` or `discontinued` label.
