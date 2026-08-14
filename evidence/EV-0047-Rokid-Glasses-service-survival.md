# EV-0047 — Rokid Glasses service-survival boundary

**Verified:** 2026-08-14  
**Evidence class:** Current first-party Rokid product and FAQ documentation  
**Scope:** Integrated Rokid Glasses / Rokid AI Glasses Style; host-driven Air/Max displays are a separate architecture

## Activation and account gate

Rokid states that operation requires a compatible smartphone, wireless internet, a valid Rokid account and the Hi Rokid app. The glasses pair with one Rokid account at a time; pairing to another account clears information on the glasses. Firmware updates and device settings are routed through the app.

## Function matrix

| Function | Local/device evidence | App/service dependency | Survival assessment |
|---|---|---|---|
| Passive eyewear / prescription insert | Magnetic prescription carrier can be fitted by a local optician | None for passive optics | Survives |
| Bluetooth calls/audio | Rokid documents use as phone microphone and speaker over Bluetooth | Compatible phone and completed setup required | Likely phone-peripheral residue |
| Capture | Onboard camera and storage support photos and video | Exact post-sign-out behavior is not documented | Hardware residue; empirical test needed |
| Media transfer | High-speed transfer uses the glasses' built-in Wi-Fi | Initiated and managed through Hi Rokid; app foreground/network constraints are documented | App-dependent recovery path |
| Offline translation | Six-language model can be downloaded, then translation runs without Wi-Fi/cellular | Pairing/activation and model download happen in the app; supported phone hardware is required | Genuine but pre-provisioned local function |
| Online translation | 89-language path uses cloud models | Network, app version and region | Service-dependent |
| Teleprompter | Script and display controls are app-managed | App/phone required; exact network-free operation after loading needs testing | Plausible phone-local function |
| Voice assistant / multimodal AI | Camera, microphones and display provide the interface | Rokid support requires stable phone network and model/provider services | Service-dependent |
| Navigation | App and regional mapping service | Phone/network/provider/region | Service-dependent |
| Firmware/settings | Managed in Hi Rokid | App, network and vendor update infrastructure | Vendor-dependent |

## Important correction

Rokid's “offline translation” is real local processing, but it is not independent first use. The glasses must first be paired and activated through the mobile app, and the language model must be downloaded. Current documentation lists Chinese, English, Japanese, German, French and Spanish; availability can vary by app version and region.

Rokid also states that the local translation model uses about 2.67 GB of phone storage/memory and requires relatively recent phone hardware. The exact split between glasses-side and phone-side local processing should therefore be tested rather than inferred from marketing shorthand.

## Correct label

**Recoverable with pre-provisioned local translation and phone-peripheral residue; defining AI remains service-dependent.**

This is stronger than a wholly cloud-essential appliance and weaker than a device whose activation, firmware and application stack can be independently replaced.

## Empirical test queue

1. Complete setup and download one offline language model.
2. Block internet and test translation, teleprompter, Bluetooth calls, capture and media transfer.
3. Sign out without resetting and repeat.
4. Preserve captures before attempting account reassignment because re-pairing clears device information.
5. Record whether offline translation executes on the phone, glasses or both.
6. Block Rokid endpoints while retaining local Wi-Fi/Bluetooth.
7. Archive app/firmware versions and installer provenance.
8. Test whether captured media is accessible by any documented standard interface.

## Primary sources

- [Rokid FAQ](https://global.rokid.com/pages/faq)
- [Rokid Glasses product page](https://global.rokid.com/products/rokid-glasses)

## Confidence

High for the required phone/account/app/internet checklist, account reassignment behavior, six-language offline translation prerequisites, built-in-Wi-Fi media transfer and cloud dependence of broader translation/assistant functions. Medium for post-setup phone-peripheral and capture survival until endpoint-blocked and sign-out tests are run.
