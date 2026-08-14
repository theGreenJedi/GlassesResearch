# Survival / Cloud-Independence Matrix

What happens to smart glasses when the vendor app, account system, AI service, or company disappears?

This matrix treats long-term survival as a first-class product characteristic. A device can have excellent hardware and still lose much of its usefulness if essential functions depend on a service the owner cannot replace.

## Survival matrix

| Device / family | Basic use without cloud | Core function without vendor service | Documented developer path | Usefulness after service loss | Assessment |
|---|---|---|---|---|---|
| Brilliant Labs Frame | Strong | Substantial device-level utility can remain; cloud AI is a separate dependency | Strong | High relative to consumer AI glasses | Published technical and project material improves preservation prospects. |
| Brilliant Labs Halo | Promising; verify shipped implementation | Product-release dependent | Strong in stated design | Potentially high | Treat announced openness separately from delivered, preserved capability. |
| Vuzix Z100 | Strong as a phone-driven display peripheral | Core display role is not inherently an AI-cloud appliance | Strong official Android/iOS SDK path | High if compatible host software remains available | Narrow architecture is an advantage for survival. |
| Solos AirGo family | Model-dependent | Audio and local device functions may remain while AI/service features vary | Official SDK exists for supported generations | Moderate to good | Exact generation matters; transport and feature sets differ. |
| XREAL One family | Strong for basic host/display use where standard host compatibility applies | Many display functions are less cloud-dependent than assistant glasses | Developer ecosystem exists | Moderate to high for display use | Proprietary spatial features, firmware, and accessories remain separate dependencies. |
| Ray-Ban Meta / Meta AI glasses | Limited relative to open platforms | Mainstream assistant and account-centered functions are service-dependent | Limited general-purpose hardware path | Low to moderate | Strong present-day ecosystem, weaker independent survival posture. |
| Even Realities G1/G2 | Physical eyewear remains useful; smart functions are ecosystem-dependent | Verify exact generation and current app requirements | Third-party access should be verified | Moderate / uncertain | Prescription value increases the importance of long-term software continuity. |
| MentraOS-compatible devices | Hardware-dependent | Cross-device software can reduce dependence on one vendor application | Strong where supported | Potentially high | Survival depends on the underlying glasses plus preserved compatibility. |
| HTC VIVE Eagle | Strong for capture; partial for other functions | Button capture, onboard storage and documented basic commands work offline; advanced VIVE AI requires VIVE Connect plus phone internet | No broad public hardware SDK documented | Moderate: camera/audio appliance survives, defining AI degrades | Function-level split is documented in [EV-0041](../evidence/EV-0041-HTC-VIVE-Eagle-service-survival.md). |
| Magic Leap 1 | Weak after shutdown | Vendor says cloud services and core device/app functionality reached end of life on 2024-12-31 | Historical developer stack no longer changes service loss | Low | Destructive-shutdown control; intact hardware does not guarantee intended utility. |
| HoloLens 1 / 2 | Stronger local survival | HoloLens 1 continues functioning after support; HoloLens 2 security servicing runs through Dec. 2027 | UWP/Windows deployment paths are documented | Moderate to high, with security/app aging | Support loss is not function loss; OS branch controls remaining runway. |
| Bose Frames | Strong for Bluetooth audio | Core audio survives discontinued Bose AR; owner support/app surfaces remain | Bose AR path abandoned | Moderate for audio, low for former AR layer | Separate standard Bluetooth utility from the discontinued experimental service layer. |
| RealWear HMT-1 / HMT-1Z1 | Strong for local device use | Vendor says EOL units still work; final firmware 12.6; some dictation languages remain local | Android application path survives with aging risk | Moderate | Third-party app and security decay remain, but this is not a destructive shutdown. |
| Recon Jet family | Activation risk | Recon Engage/support ended; activation-screen bypass remains a preservation problem | Community preservation only | Low / uncertain | Concrete example of account infrastructure blocking otherwise local hardware. |
| W610 / HeyCyan variants | Capture/media hardware is promising; exact offline baseline remains hands-on work | Community CyanBridge path documents BLE-triggered Wi-Fi Direct/local-HTTP media retrieval; vendor AI, configuration and OTA boundaries remain | Independent community companion exists but presently retains vendor-binary dependencies | Recoverable potential; not yet hands-on graded | [EV-0044](../evidence/EV-0044-W610-community-protocol-and-owner-access.md) establishes a concrete continuity route without proving full vendor independence. |

## Survival levels

**A — Durable:** core purpose continues with standard interfaces, published source, documented SDKs, or reproducible local software.

**B — Recoverable:** important functions require vendor software, but documented interfaces or preserved software provide a realistic continuity path.

**C — Dependent:** major smart functions require a maintained vendor application, account, or proprietary service.

**D — Cloud-essential:** loss of vendor service substantially removes the product's intended smart function.

**Unknown:** evidence is insufficient. Unknown is not a failing grade; it is a research target.

## Minimum survival test

For hands-on devices, record whether the device boots without internet, pairs without internet, retains basic audio, captures media locally, allows local media access, operates its display or HUD offline, requires a vendor account for setup, remains useful after sign-out, and has retrievable installers, SDKs, firmware notes, or recovery documentation.

## Why this belongs beside price and performance

A lower-cost device that remains useful for years can be a better value than a more expensive device whose defining features disappear with a subscription, server shutdown, or abandoned app. Survival therefore contributes directly to **Cloud Independence**, **Owner Control**, **Hackability**, and **Value** in the GlassesResearch Report Card.
