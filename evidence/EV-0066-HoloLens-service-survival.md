# EV-0066 — Microsoft HoloLens post-support survival matrix

**Status:** Source boundary completed; post-2027 hands-on validation remains  
**Scope:** HoloLens (1st generation) and HoloLens 2, adjacent head-worn MR controls  
**Reviewed:** 2026-08-15

## Question

What remains locally usable after Microsoft support winds down, and which setup, application-deployment and recovery paths depend on Microsoft services?

## Finding

Microsoft explicitly states that HoloLens 1 continues to function after its final December 2024 servicing update. Its preserved development documentation supports local custom-application installation through Windows Device Portal or Visual Studio. This is a graceful-support-loss control: security and vendor support ended, but the vendor did not impose a destructive identity shutdown.

HoloLens 2 is more nuanced. Ordinary first-run setup requires a network connection and a Microsoft or Entra account. Once deliberately provisioned, Microsoft documents secure offline deployments using a local account, provisioning packages and locally deployed applications. Signed Appx bundles can also be copied over USB and installed through File Explorer, and Device Portal remains a local sideloading path. Offline recovery is possible only if the owner has downloaded the required FFU image in advance.

## Function-by-function matrix

| Function | HoloLens 1 | HoloLens 2 | Evidence boundary |
|---|---|---|---|
| Boot and installed local apps after support | Microsoft says device continues to function | Local applications and offline deployment documented | Hands-on long-term aging remains |
| First-run setup | Historical setup details not resolved by this pass | Normal OOBE requires network plus Microsoft/Entra account | Offline secure provisioning is a separate managed path |
| Custom app installation | Device Portal or Visual Studio | USB/File Explorer App Installer, Device Portal, provisioning package or MDM | Packages must satisfy signing/trust requirements |
| Offline operation | Local Windows Holographic applications survive | Microsoft documents secure offline deployments with local account | Cloud-backed apps remain service-dependent |
| Store applications | Store availability/aging uncertain after support | Store/WinGet/Intune paths remain Microsoft-service dependent | Preserve packages separately |
| Device management | Local Device Portal exists | Local provisioning exists; Intune/Autopilot require services | Do not treat optional cloud management as core-device necessity |
| OS/security updates | Ended after December 2024 | Final feature release November 2024; supported Windows 11 servicing through December 2027 | Windows 10 branches ended servicing in December 2024 |
| Recovery | Preserved recovery-image path not established here | Offline FFU flashing works only with image downloaded beforehand | Automatic download/flashing no longer supported |
| Account loss | Local installed applications may survive | Normal account-based setup and cloud apps are exposed; offline-local provisioning mitigates | Test sign-in expiry and reset behavior empirically |

## Lifecycle classification

- **HoloLens 1:** discontinued-functional. Strong local survival, no security runway.
- **HoloLens 2:** maintenance/winding down. Recoverable and locally deployable when deliberately provisioned, but consumer-style first setup and cloud applications remain service exposed.

## Scoring effect

HoloLens 1 retains Cloud Independence 9.0 because Microsoft explicitly preserves device function and local app deployment. HoloLens 2 remains 8.0: it has excellent offline enterprise provisioning and owner-deployed apps, but default OOBE and several management/application paths rely on Microsoft identity and services.

## Required preservation work

Archive the relevant Appx bundles, dependencies, signing certificates, development tools and HoloLens 2 FFU image while official routes remain available. Test one locally provisioned and one account-managed HoloLens 2 after endpoint blocking, sign-out and clock advancement. Record Store, installed apps, USB/MTP, Device Portal, certificate trust, reset and recovery behavior. Do not reset the only preservation unit without a verified FFU and restore procedure.

## Sources

- [HoloLens 1 final servicing and continued function](https://learn.microsoft.com/en-us/previous-versions/mixed-reality/hololens-1/hololens1-release-notes)
- [HoloLens 1 local custom-app installation](https://learn.microsoft.com/en-us/hololens/holographic-custom-apps)
- [HoloLens 2 ordinary first-run requirements](https://learn.microsoft.com/en-us/hololens/hololens2-start)
- [HoloLens 2 offline-secure deployment scenarios](https://learn.microsoft.com/en-us/hololens/hololens-requirements)
- [HoloLens 2 USB/App Installer deployment](https://learn.microsoft.com/en-us/hololens/app-deploy-app-installer)
- [HoloLens 2 offline recovery-image requirement](https://learn.microsoft.com/en-us/hololens/hololens-recovery)
- [HoloLens 2 servicing history](https://learn.microsoft.com/en-us/hololens/hololens-release-notes)
