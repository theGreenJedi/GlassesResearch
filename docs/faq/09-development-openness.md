# Development, openness, protocols, and repairability

Openness is a stack: hardware documentation, boot access, firmware, protocols, SDKs, app licensing, cloud dependence, and repair parts can each be open or closed.

**Information reviewed:** 2026-08-05. Product availability, software, prices, and advertised battery life can change. Unless explicitly marked hands-on, statements below are sourced from manufacturers, project documentation, or attributed community material.

## 81. Which smart-glasses platforms are open source?

MentraOS is published under an MIT license and supports several hardware platforms. Brilliant Labs publishes repositories and documentation for its devices, and Halo is presented as open hardware and software. Team Open Smart Glasses publishes mechanical, electrical, and software files. Sources: [MentraOS](https://github.com/Mentra-Community/MentraOS), [Brilliant Labs GitHub](https://github.com/brilliantlabsAR), [Open Source Smart Glasses](https://github.com/Mentra-Community/OpenSourceSmartGlasses).

## 82. What is MentraOS?

MentraOS is an open-source smart-glasses software platform with an SDK and miniapp store. It supports Mentra Live, Even G1/G2, and Vuzix Z100, with other hardware planned. Its architecture uses the phone as the app runtime so lightweight glasses can share one connection and run multiple miniapps. Sources: [MentraOS overview](https://mentraglass.com/os), [MentraOS roadmap](https://mentraglass.com/blogs/blog/mentra-roadmap-update-moving-to-miniapps-on-the-phone).

## 83. Can developers build apps for Ray-Ban Meta glasses?

Consumers can use Meta’s supported features and integrations, but Ray-Ban Meta is not the default recommendation for unrestricted hardware/protocol development. Access is controlled relative to Mentra, Brilliant Labs, Vuzix, or Rokid developer ecosystems. Before choosing it for a project, verify the current official SDK/API scope rather than assuming camera, sensors, or BLE characteristics are available.

## 84. Can developers build apps for Even G2 or Vuzix Z100?

Yes, through supported routes. Vuzix provides its Ultralite SDK for text, images, simple animations, taps, screen state, and battery state. MentraOS lists Even G1/G2 and Vuzix Z100 as supported hardware for its miniapps. Sources: [Vuzix Z100 SDK overview](https://support.vuzix.com/docs/overview-28), [MentraOS compatibility](https://mentraglass.com/os).

## 85. What makes smart glasses hackable?

Useful indicators include accessible firmware/update files, documented USB or BLE protocols, an SDK without restrictive gates, unlockable boot paths, serial/debug pads, reproducible builds, available recovery images, standard components, community captures, and replaceable hardware. Marketing phrases such as `open AI` do not prove any of these.

## 86. What is the difference between an SDK and an open protocol?

An SDK is vendor-supplied code and documentation for approved functions. An open protocol documents the messages on the wire so independent implementations can interoperate. An SDK may be proprietary, cloud-bound, revocable, or limited; an open protocol may enable clients on unsupported platforms. Serious research records both.

## 87. Why capture BLE services and packets from smart glasses?

Captures reveal advertised identities, services, characteristics, notifications, commands, and state transitions. They can preserve knowledge even if the app disappears. Capture only devices and traffic you are authorized to inspect, record firmware/app versions, redact personal data, and store raw evidence plus decoded notes.

## 88. Can smart-glasses firmware be replaced?

Sometimes, but usually not safely without signed images, bootloader access, hardware documentation, and a recovery method. A firmware dump is not the same as a flashable replacement. Begin by preserving official updates, hashes, partitions, logs, and recovery procedures; do not experiment on the only working specimen without a rollback path.

## 89. Are smart-glasses batteries and parts repairable?

Fashion-oriented models often use glued or sealed batteries and proprietary charging; Ray-Ban explicitly says its embedded batteries are not replaceable. Enterprise modules and open hardware projects offer better prospects. Repairability should include parts availability, disassembly damage, calibration, waterproofing, firmware pairing, and lens service—not just whether screws exist. Source: [Ray-Ban Meta FAQ](https://www.ray-ban.com/usa/c/frequently-asked-questions-ray-ban-meta-smart-glasses).

## 90. What artifacts should a smart-glasses research repository preserve?

Preserve lawful copies or metadata for manuals, APKs, SDKs, firmware and update URLs, hashes, BLE captures, protocol schemas, logs, model files, PCB photographs, regulatory filings, lens templates, flashing/recovery instructions, tools, repositories, and community posts. Record provenance, retrieval date, license, redistribution status, model/revision, and authenticity caveats.


## Veyra Android v4: 25 practical questions (October 2026)

**Evidence notice:** This is a research FAQ, not an endorsement or hands-on review. The October 18 developer/community announcement is the basis for attributed release claims; [locate the original Veyra discussion](https://www.reddit.com/r/augmentedreality/search/?q=Veyra&restrict_sr=1&sort=new). This search link is a discovery pointer, not a verified permalink to the original post. No independent bench verification is claimed.

### 1. What is Veyra?

Veyra is a third-party Android project for using AI with Meta smart glasses. Its developer announced Android v4 in October 2026. **Evidence: developer report; not GlassesResearch hands-on verified.**

### 2. Is Veyra a pair of smart glasses?

No. Veyra is software associated with compatible Meta smart glasses, not a separately manufactured eyewear model. **Evidence: developer description.**

### 3. Which glasses does Veyra support?

The developer describes Meta smart-glasses integration. An exhaustive model-by-model compatibility list has not been independently established here; check the developer's current release information before installation. **Status: partially documented.**

### 4. Does Veyra run on Android?

The developer announced an Android v4 release. Specific minimum Android versions and supported phone models require direct testing or published requirements. **Evidence: developer report.**

### 5. Is there a Veyra iPhone app?

The Android v4 announcement does not establish current iOS availability. Check the developer's official distribution channels. **Status: unknown.**

### 6. Can Veyra use different AI providers?

The developer reports user-selectable AI providers in Android v4. Available providers, account requirements, and feature differences should be confirmed against the current app. **Evidence: developer report.**

### 7. Can Veyra work entirely offline?

No independently verified fully offline operating mode is documented in this research entry. Provider selection alone does not prove on-device inference. **Status: unknown; testing needed.**

### 8. Does Veyra use Meta's Device Access Toolkit?

The developer states that Veyra depends on Meta's Device Access Toolkit. Toolkit permissions and availability may constrain integrations. **Evidence: developer statement.**

### 9. Is Veyra open source?

The developer described Veyra as closed-source. That is distinct from whether Meta publishes portions of its developer toolkit. **Evidence: developer statement.**

### 10. Can users audit Veyra's source code?

Not through a publicly available Veyra source repository established by this research. Closed-source distribution limits independent code auditing. **Status: developer-reported closed source.**

### 11. Can Veyra stream video?

The Android v4 announcement reports video streaming. Resolution, frame rate, sustained duration, and end-to-end latency are not independently measured here. **Evidence: developer report.**

### 12. Can Veyra be activated with a physical button?

The developer reports physical-button activation in Android v4. Exact button mapping and model coverage require confirmation. **Evidence: developer report.**

### 13. Does Veyra record continuously?

No verified conclusion about continuous recording or background capture can be drawn from the release announcement. Review permissions and test camera/microphone behavior. **Status: unknown.**

### 14. What happens to images or video sent through Veyra?

Data handling may depend on the app, selected AI provider, and Meta's platform. No independently audited end-to-end data-flow map is available here. **Status: unverified.**

### 15. Does Veyra identify people?

The cited release information does not establish face-recognition or person-identification functionality. Do not infer it from camera or AI access. **Status: not established.**

### 16. Does Veyra require a network connection?

Network requirements likely vary by feature and provider, but exact offline/online behavior has not been verified. **Status: testing needed.**

### 17. Are there Veyra connection problems?

Some users reported connection difficulties in the developer discussion. Their frequency, causes, and affected configurations are not established. **Evidence: community reports, not independently reproduced.**

### 18. Does Veyra cause overheating?

The developer acknowledged thermal limitations during streaming. That does not quantify temperature rise or establish which devices or sessions are affected. **Evidence: developer statement; testing needed.**

### 19. How long can Veyra stream video?

No independently verified continuous-stream runtime is available here. Thermal behavior, battery depletion, and network conditions should be measured together. **Status: unknown.**

### 20. How does Veyra affect glasses battery life?

No controlled Veyra-versus-stock battery comparison is available here. Video capture and connectivity may affect runtime, but numerical claims require measurement. **Status: unknown.**

### 21. Can Veyra replace the official Meta companion app?

The release announcement does not establish complete replacement of Meta's setup, pairing, update, or account workflows. **Status: not established.**

### 22. Can Veyra work with MYVU or XGA010C glasses?

No documented Veyra support for MYVU/XGA010C is established. Shared smart-glasses terminology does not imply compatible firmware or protocols. **Status: unsupported claim; do not assume compatibility.**

### 23. Does Veyra expose an SDK or documented protocol?

The developer's closed-source statement does not itself establish a public Veyra SDK or stable protocol. Verify official documentation before planning integrations. **Status: unknown.**

### 24. How should owners test Veyra safely?

Record phone and glasses models, firmware and app versions, pairing steps, permissions, activation behavior, provider used, network dependence, battery change, temperature symptoms, and failures. Avoid recording bystanders or exposing credentials. **Status: GlassesResearch proposed test protocol, not a product claim.**

### 25. Has GlassesResearch independently verified Veyra?

No hands-on Veyra bench results are documented in this entry. Features are attributed to the developer; connection issues are attributed to users. Independent repeatable tests are needed before promotion to verified findings. **Status: not independently verified.**


## Is RayNeo iO support being considered for the MentraOS roadmap?

**A public request exists, but MentraOS has not publicly committed to RayNeo iO support in the sources reviewed.** A community member opened [MentraOS issue #4841](https://github.com/Mentra-Community/MentraOS/issues/4841) on October 17, 2026, requesting RayNeo iO compatibility, especially on iOS. As reviewed October 24, the issue is open without a maintainer response; it is a *request*, not a supported-device announcement or delivery date.

Mentra's [official compatibility page](https://mentraglass.com/os) does not list RayNeo iO as supported. The separate [pluggable OEM glasses-adapter proposal (#3017)](https://github.com/Mentra-Community/MentraOS/issues/3017) describes a potential route for third-party devices but does not itself promise an iO adapter, working pairing, MiniApp compatibility, or iOS support. The requester also cites independent [Turbo-IO](https://github.com/Turbo1123/Turbo-IO) and [Spare io](https://github.com/owenc1122/spare-io) projects; neither is evidence of an official MentraOS integration.

**Practical answer:** Do not purchase RayNeo iO assuming it works with MentraOS today. Follow issue #4841 and the official supported-device list for an explicit maintainer decision and tested release. **Evidence status: public request confirmed; roadmap acceptance, integration, and compatibility unverified. Reviewed 2026-10-24; no GlassesResearch hardware test.**

## Does the Vuzix Speech SDK support German number-word commands on M300, and how are language files loaded?

**German-language commands are a documented capability of the Vuzix speech-command family, but the exact M300 firmware, language resources, and recognition of a developer's chosen number words still need device-level verification.** This answers an [observed M300 developer question](https://stackoverflow.com/questions/60778715/vuzix-speech-sdk-language-support), not a generic claim that every Vuzix model supports every language.

For an M300, the practical first test is to set the **glasses' system language to German**, enable Vuzix speech recognition, and then register and test the German phrases in the app. In the original developer discussion, one respondent reports that the recognizer loads language resources when the system language changes, and suggests restarting the glasses if the change does not take effect; another commenter reports that German phrases do **not** work when the system remains in English. These are **community troubleshooting observations**, not a manufacturer-guaranteed M300 installation procedure. The respondent also suggests inspecting the active vocabulary with `VuzixSpeechClient.dump()`.

[Vuzix's M300/M300XL Speech SDK instructions](https://support.vuzix.com/docs/getting-started-code-4) explicitly describe localized wake words chosen according to the device language and show how to register phrases and inspect the vocabulary. [Vuzix's supported-language documentation](https://support.vuzix.com/docs/overview-32) includes German. However, the company's [28-language OS 2.5 announcement](https://ir.vuzix.com/news-events/press-releases/detail/1966/vuzix-m-series-smart-glasses-now-fully-support-28-languages) specifically concerns the **M400 and M4000**; it must not be used as proof that an older M300 has that firmware or language pack.

**Answer on the requested language files:** The sources reviewed do not establish a supported public download-and-manual-install process for M300 German recognition files. Start with the device locale and built-in speech engine; record the M300 OS/Speech SDK versions, check the active vocabulary, and ask [Vuzix technical support](https://support.vuzix.com/docs/working-with-the-speech-sdk) for model- and firmware-specific resources if German commands still fail. **Evidence status:** manufacturer documentation plus an attributed developer report; no GlassesResearch M300 bench test, no verified recognition-accuracy result. Reviewed 2026-10-24.
