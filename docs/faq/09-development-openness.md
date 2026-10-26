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

**Evidence notice:** This is a research FAQ, not an endorsement or hands-on review. The October 18 developer/community announcement is the basis for attributed release claims; [October 18 Veyra Android v4 developer announcement and discussion](https://www.reddit.com/r/RaybanMeta/comments/1x9be1z/veyra_for_android_v4_is_out_go_live_to_youtube/). This is the developer's public account, not independent device verification. No independent bench verification is claimed.

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

## Why downloaded APK files are not displaying in Vuzix SmartGlass's download folder?

**Short answer:** A downloaded APK can be present in device storage without being shown by an on-glasses Downloads app. The [original M100-era developer report](https://stackoverflow.com/questions/41234245/why-downloaded-apk-files-are-not-displaying-in-vuzix-smartglasss-download-folde) describes exactly that situation; it does not establish a single universal cause. Avoid treating an invisible Downloads entry as proof the APK was not transferred.

For **M300/M300XL**, [Vuzix's installation instructions](https://support.vuzix.com/docs/can-i-install-applications-on-my-m-series-device-using-usb) document two routes: transfer the APK in the appropriate USB file-transfer mode, then locate and open it under **Settings > Storage & USB > Explore**, or install from a computer using Android Debug Bridge with `adb install path/to/app.apk`. The [Vuzix App Store](https://support.vuzix.com/docs/how-do-i-install-applications-on-my-m-series-smart-glasses) is another vendor-supported deployment route. These instructions are model-specific: do **not** assume identical menus, connectors, or supported files on the older **M100**. Community replies to the original question also described an M100 System File Manager, but its historical download links and present-day availability have **not** been independently verified.

**Practical next step:** confirm the exact glasses model and firmware, verify where the APK was transferred, and follow that model's supported installation procedure rather than relying only on the Downloads app listing. **Evidence:** direct Vuzix instructions for M300/M300XL and an attributed 2016–2018 community troubleshooting thread; no GlassesResearch M100/M300 device reproduction. Reviewed October 24, 2026.

## Detect Google Glass Programmatically

**Short answer:** For the original Android-based Google Glass Explorer devices, check the Android build manufacturer **and** model as a practical *heuristic*, not a guaranteed hardware attestation. The [original developer question (2013)](https://stackoverflow.com/questions/18723689/detect-google-glass-programmatically) includes this community-tested Java approach:

```java
boolean looksLikeExplorerGlass =
    "Google".equalsIgnoreCase(android.os.Build.MANUFACTURER)
    && android.os.Build.MODEL != null
    && android.os.Build.MODEL.startsWith("Glass");
```

[Android's official `Build` reference](https://developer.android.com/reference/android/os/Build) defines `MANUFACTURER` as the hardware manufacturer and `MODEL` as the end-user-visible product name. The original thread reports `MODEL = "Glass 1"` and `MANUFACTURER = "Google"` for a historic device. This is more discriminating than checking Android 4.4 / API 19, which also ran on ordinary phones.

**Limits:** these fields are software-provided build properties; they are not proof of a genuine device and do not establish compatibility with every later Glass Enterprise edition, firmware, or emulator. If an app needs a particular feature, test that feature or its documented API separately. Google's [Glass Development Kit documentation](https://developers.google.com/glass/develop/gdk) concerns the legacy Android-based Glass platform, not an all-generation identity guarantee. **Evidence:** official Android and legacy Glass developer documentation plus attributed historical device output; no current Glass hardware test. Reviewed October 24, 2026.

## Can Sony Smart Glass be used on platforms other than Android?

**Short answer:** Sony's published **SmartEyeglass SDK** is an **Android SmartExtension/host-app framework**, not an official Windows or Linux Bluetooth SDK. The [original October 2014 developer question](https://stackoverflow.com/questions/26547629/can-sony-smart-glass-be-used-on-platforms-other-than-android) explicitly asks about using the glasses from Windows or Linux over Bluetooth; the contemporary answer states that the supported SDK and host application were Android-only.

Sony's own [SmartEyeglassControl API reference](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/SmartEyeglassControl) describes extensions to Android's SmartExtension framework. Its [intents documentation](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/SmartEyeglassControl.Intents) specifies Android manifest permissions and communication with the Android HostApp. The [control utilities reference](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassControlUtils) describes the Android-hosted display, camera and audio interfaces.

**Practical path:** use an Android host for the supported SDK, and if a desktop workflow is required, connect the Windows/Linux application to that host using a separately designed, authorized bridge. Direct desktop-to-glasses communication would require an independently documented and tested protocol implementation; Bluetooth hardware support alone does **not** establish SDK compatibility. This is a statement about the *documented Sony SDK*, not a claim that reverse-engineered integrations are impossible. **Evidence:** Sony API reference and attributed 2014 developer discussion; no Windows/Linux direct-connection bench test. Reviewed October 24, 2026.

## Does the Even R1 ring work with MentraOS on Even G2?

**Partially, according to the MentraOS project; reliable full control is not established.** [Mentra's G2 compatibility instructions](https://mentrahelp.zendesk.com/hc/en-us/articles/46816258641556-Does-MentraOS-support-Even-Realities-G2-glasses) confirm that the **G2 glasses** can pair with the Mentra app, but they do **not** promise that the separate **R1 ring** can launch and switch between Mentra miniapps. The distinction matters: G2 compatibility is not an R1 feature guarantee.

The [MentraOS R1 tracking issue #3042](https://github.com/Mentra-Community/MentraOS/issues/3042), opened June 1, 2026, says some ring input is supported in principle while recording user reports of failed ring control, unclear pairing, and missing app-open/app-switch gestures. The issue remains open as reviewed October 25, 2026; its proposed goals should **not** be read as delivered functionality. Community complaints quoted there are user reports, not independently reproduced tests. No release-by-release R1 gesture compatibility matrix or verified fix was found in the reviewed sources.

**Practical choice:** If ring-based navigation is essential, confirm pairing, swipes, taps, opening apps, and switching apps on the **exact Mentra app, G2 firmware, R1 firmware, and phone** before relying on it. The [Even Realities R1 troubleshooting instructions](https://support.evenrealities.com/hc/en-us/articles/17131158230159-G2-and-R1-Are-Connected-in-the-App-but-R1-Cannot-Control-G2) apply to the **official Even app** and do not establish that the same controls work in MentraOS. **Evidence status:** official Mentra G2 compatibility, an open upstream R1 issue containing attributed community reports, and official Even-app troubleshooting; no GlassesResearch G2/R1 bench verification. Reviewed October 25, 2026.


## How do I install a custom app for Sony SmartEyeglass?

**Install the SmartEyeglass extension on the paired Android phone, not as an ordinary APK on the eyeglass display.** The [observed 2016 developer question](https://stackoverflow.com/questions/37791282/app-installation-in-sony-smart-glass) asks where to install an Android Studio app. Sony's [SmartEyeglassControl API reference](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/SmartEyeglassControl) identifies the platform as an Android **SmartExtension** communicating through a **HostApp**, while its [registration API](https://developer.sony.com/reference/seg-sdk/com/sonyericsson/extras/liveware/aef/registration/Registration) documents how the host discovers registered extensions.

For the historical **SED-E1 SmartEyeglass** development workflow, install the compatible **Smart Connect / SmartEyeglass companion** software on the Android phone, then install the built SmartExtension APK **on that phone**, register the extension with the host, and launch it from the accessory's app interface. The separate [2017 developer exchange about a custom app not appearing](https://stackoverflow.com/questions/42295084/how-to-install-the-custom-app-to-the-android-phone-for-using-sony-smarteyeglass) confirms that a normal Android Activity by itself is not sufficient: the app must use Sony's SmartEyeglass SDK. Do **not** blindly follow the original thread's speculative advice to enable USB debugging and sideload an APK onto the glasses; that was not a tested Sony-specific procedure.

**Limits:** This is a historically documented SDK route, not a promise that Sony's discontinued companion apps or old Android SDK install cleanly on current phones. Preserve the original SDK/companion versions and test on a supported period-correct phone. No GlassesResearch SED-E1 hardware installation test. Reviewed October 25, 2026.

## How do I register a Sony SmartEyeglass app so Smart Connect recognizes it?

**Use Sony's extension-registration classes rather than making your main Activity implement the registration API.** The [observed 2016 Android Studio question](https://stackoverflow.com/questions/38713859/how-to-register-an-app-for-sony-smart-glass) contains errors such as missing `RegistrationInformation`, `SampleRegistrationInformation`, and `HelloLayoutsSEGControl`. Those sample identifiers are not automatically present in a fresh Android project.

Sony's archived [`RegistrationInformation` reference](https://developer.sony.com/reference/seg-sdk/com/sonyericsson/extras/liveware/extension/util/registration/RegistrationInformation) defines an **abstract class** with required methods for supported APIs and registration configuration. Its [`ExtensionService` reference](https://developer.sony.com/reference/seg-sdk/com/sonyericsson/extras/liveware/extension/util/ExtensionService) requires an implementation of `getRegistrationInformation()`; the [Registration/Capability API](https://developer.sony.com/reference/seg-sdk/com/sonyericsson/extras/liveware/aef/registration/Registration) describes how the Android host stores and discovers extensions. A practical repair is to import/link the correct Sony SDK, define a concrete `RegistrationInformation` subclass, return it from an `ExtensionService` subclass, supply required manifest declarations, and replace sample-only names with actual classes in the project. A regular `MainActivity` is not a substitute for the extension service. The community reply outlines the same class separation, but does not prove the questioner's full project was fixed.

**Limits:** The 2016 question includes additional undefined variables and incomplete code, so the precise set of compile errors cannot be resolved without the whole project and matching historical SDK. The archived API does not establish compatibility with modern Android Gradle Plugin releases. No GlassesResearch build or device test. Reviewed October 25, 2026.

## Can I add a normal Wi-Fi network connection to Sony SmartEyeglass?

**Do not treat the glasses' WLAN address as a normal, user-configurable Wi-Fi client menu.** In the [observed 2016 question](https://stackoverflow.com/questions/37879755/installing-wifi-option-in-sony-smart-glass), the owner sees a WLAN address but cannot enter a protected network password. Sony's archived [`SmartEyeglassControlUtils.setPowerMode()` reference](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassControlUtils) describes **normal mode using Bluetooth** and **high-power mode allowing Wi-Fi** for higher-throughput communication with the host; its [power-mode constants](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/SmartEyeglassControl.Intents) explicitly distinguish Bluetooth from Wi-Fi.

That Wi-Fi path is a **host-accessory transport mode**, not evidence of an SDK-supported facility for manually joining arbitrary SSIDs or installing a separate Wi-Fi settings app on the eyewear. A historical developer reply describes activating high-power mode (including during camera use), but this was not independently reproduced. If the project needs internet access, use the paired Android host's network path; if it needs higher-bandwidth host/glasses communication, test the documented high-power mode on the exact firmware and app combination.

**Limits:** No claim is made that all possible custom firmware or independent protocol work is impossible. The historical Sony guide URLs may now redirect, and no current SED-E1 Wi-Fi pairing test is available. Reviewed October 25, 2026.

## How do I set up Android Studio with the Vuzix M100 SDK?

**Use the legacy M100 SDK add-on for Android API 15; do not substitute a current M300, M400, or Z100 SDK.** The [observed 2017 developer question](https://stackoverflow.com/questions/42242199/how-to-setup-android-studio-to-use-vuzix-m100-smart-glass-sdk) asks specifically for the Vuzix SDK without Wikitude. Vuzix's own [M100 SDK 1.4+ installation guide](https://d2iankuf53zudv.cloudfront.net/Content/Upload/Installing-the-Vuzix-M100-SDK.pdf) documents the historical add-on site, the **Vuzix M100 Add-On (API 15)** build target, and a manual `add-ons/addon-vuzix_m100_sdk_addon-vuzix-15` folder installation route when an SDK package has no `addon.xml`. Its [M100 Voice Control SDK developer guide](https://files.vuzix.com/Content/Upload/Driver_File_VoiceControlSDK_1__20160317210049767.pdf) separately demonstrates an Android Studio project selecting the same M100 add-on.

For a preserved legacy toolchain, obtain the authentic M100 SDK package, check its version and provenance, install the API-15 add-on into a compatible Android SDK installation, and verify that **Vuzix M100 Add-On** appears as a selectable build target before compiling. If the historical update URL fails, do not download an unknown replacement from an unofficial mirror. Vuzix's guide also warns that the SDK's stub JARs should **not** be bundled into the APK: the device supplies their runtime implementations. The original Stack Overflow answer proposed the add-on URL, but the asker reported that it still failed to install; the discussion is **not** proof of a working current download.

**Limits:** Vuzix's documents describe a 2015–2017 toolchain, not verified operation in Android Studio 2026. The legacy add-on site's present availability has not been established, and no GlassesResearch M100 build or device test was performed. Reviewed October 25, 2026.

## Can a Google Glass GDK app run unchanged on Vuzix M100?

**Not as a general drop-in port.** The [observed 2015 developer question](https://stackoverflow.com/questions/32070647/develop-for-vuzix-m100-smart-glasses) reports a Google Glass Development Kit (GDK) APK failing on M100. The [Google Glass GDK documentation](https://developers.google.com/glass/develop/gdk) describes the legacy Glass-specific APIs; Vuzix's [M100 SDK installation guide](https://d2iankuf53zudv.cloudfront.net/Content/Upload/Installing-the-Vuzix-M100-SDK.pdf) targets **API 15**, and the [M100 product guide](https://files.vuzix.com/Content/Upload/Driver_File_425PB0002_03_Product_Guide_US_Enterprise_20160404131344910.pdf) identifies Android **4.0.4**. Android application code that relies on Glass-only GDK classes or newer platform APIs cannot be assumed to work on this older Vuzix runtime.

**Practical migration:** Separate portable Android logic from Glass-specific voice, cards, UI, and device services; build a dedicated M100 variant targeting the correct Android/API and available Vuzix APIs, then test on real M100 hardware. The questioner later reported that a **Wikitude** SDK could help target both products, but this is a historical project-specific report, **not** proof that an arbitrary GDK APK runs unchanged or that the old Wikitude integration is supported today. Do not attempt to flash a different Android version merely to satisfy a build requirement without manufacturer-backed firmware and recovery procedures.

**Limits:** No current compatibility matrix, supported M100 Android 4.4 upgrade path, or GlassesResearch cross-device bench test was established. Reviewed October 25, 2026.


## Voice-session control and smart-glasses SDK testing — 15 practical answers (October 2026)

**Sources:** [Visor protocol and follow-up changes](https://github.com/macedonga/visor/commit/6a4ac0f691fbd7f37a0c4203c4f24b07c7bb1263); [VModal voice-search integration and simulator tests](https://github.com/v-modal/vmodal_sdk_smartglass/commit/da217283a3187b9c64b490bfedb402aacf0a6931). These are public project primary sources. No GlassesResearch independent hardware testing is claimed.

### 1. Can smart glasses accept follow-up questions without repeating a wake phrase?

Yes, in some implementations. Visor's developer reports successfully chaining follow-ups on actual glasses with phone-generated speech. This is a project-specific result, not a universal Meta feature. **Evidence: developer hardware test.**

### 2. Why might a glasses microphone remain active after an AI answer?

An incomplete end-of-turn protocol exchange can leave a device in its answering state. Visor's developer documented that missing `ev60` signaling caused this with phone-generated speech. **Evidence: developer diagnosis; not independently reproduced.**

### 3. How can an app signal that a spoken answer has finished?

Visor documents an `ev60` end-of-turn message and flags such as `shouldSmartFollowUp` and `requiresAnswer`. These are reverse-engineered project observations, not a guarantee of stable public protocol support. **Evidence: source commit.**

### 4. Can users explicitly end a follow-up conversation?

Visor added an `end_conversation` tool intended to send a final answer without requesting another turn. Its developer describes phrases such as 'goodbye' or 'that's all'. **Evidence: developer implementation; coverage beyond reported testing unverified.**

### 5. Do phone-generated and glasses-generated speech use the same session signaling?

Not necessarily. Visor's developer found different handling paths and changed both to close turns correctly. **Evidence: reverse-engineering report; implementation-specific.**

### 6. Can a follow-up question arrive with a different invocation method?

Yes in the Visor protocol observations: invocation method 5 was added to the project's follow-up handling alongside method 3. **Evidence: source commit; protocol stability unknown.**

### 7. Does a blinking indicator always mean the microphone is recording?

Not conclusively. In a documented Visor failure, a blinking light coincided with an active microphone and stuck answer state. Indicator semantics should be checked per device and firmware. **Evidence: developer observation; generalization unverified.**

### 8. How should owners test whether a voice session really ends?

After a response, check the documented device indicator, attempt an expected follow-up, issue an end-session phrase, and observe whether further speech triggers processing. Avoid recording others; instrument microphone state where accessible. **Evidence: proposed GlassesResearch test method, not a verified product claim.**

### 9. What is a smart-glasses mock device kit?

A mock device kit simulates device interfaces for automated development testing. VModal's project uses Meta Mock Device Kit tests to exercise integration without requiring physical hardware for every CI run. **Evidence: project source.**

### 10. Do passing simulator tests prove an app works on physical glasses?

No. VModal explicitly documents physical-device and live acceptance as pending despite simulator and native contract tests. **Evidence: project source.**

### 11. Can a glasses app retrieve images using voice search?

VModal's implementation connects speech, ranked search, image preparation, and display orchestration. That demonstrates an implemented software path, not independently verified performance on glasses. **Evidence: project source; physical acceptance pending.**

### 12. What does rank-one image search mean in a glasses app?

In VModal's implementation, the search pipeline selects a top-ranked result for downstream image preparation and display. Accuracy and relevance need task-based testing. **Evidence: project architecture; performance unverified.**

### 13. Why separate a glasses SDK into an independent package?

An independent package can isolate device-specific integration from application logic and make contract testing easier. VModal's developer describes consuming its Android SDK as a separate Maven package. **Evidence: project source.**

### 14. What should automated smart-glasses CI test?

Useful checks include SDK contracts, session lifecycle, permission/error paths, speech/display orchestration, and mock-device behavior. VModal gates public CI on native contract and Meta Mock Device Kit tests. **Evidence: project source; broader checklist is GlassesResearch guidance.**

### 15. What should be tested on real glasses after simulator success?

Verify pairing, activation, latency, image legibility, battery, thermals, interrupted connectivity, microphone shutoff, and safe session termination. VModal's physical/live acceptance is still pending. **Evidence: proposed owner test protocol and project disclosure.**

## Can Sony SmartEyeglass use voice input from a microphone?

**Yes—but distinguish Sony's built-in voice-to-text path from a separate phone microphone.** The [original 2016 developer question](https://stackoverflow.com/questions/36347593/sony-smart-glasses-mic-input) asks whether menu voice control must use the touch-controller microphone or can use an external Bluetooth mic. Sony's [SmartEyeglass control API](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassControlUtils) documents a **microphone on the controller** and `enableVoiceTextInput()`, which waits for the wearer to press **Talk** and returns recognized text asynchronously through [`onVoiceTextInput()`](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassEventListener). The app needs Sony's SmartEyeglass permission and the separate `VOICE_TEXT_INPUT` permission.

Sony also documents the glasses as a **Bluetooth headset** for host-phone audio using standard Bluetooth Hands-Free Profile (HFP). A host Android app can instead request [`RECORD_AUDIO` permission](https://developer.android.com/media/platform/mediarecorder) and use its own microphone/audio-input routing and recognition, then translate recognized commands into app UI actions. **That is not proof that Sony's built-in `enableVoiceTextInput()` accepts any arbitrary microphone paired to the phone**, nor that speech automatically controls SmartEyeglass menus. Those functions need explicit application logic and hardware testing.

**Limits:** Legacy Sony SDK documentation, not a GlassesResearch microphone-routing or speech-recognition bench test. Specific Android/firmware combinations and third-party Bluetooth mics remain unverified. Reviewed October 26, 2026.

## Does Google Glass GDK provide stereoscopic 3D for Epson Moverio?

**No supported cross-device stereoscopic rendering path is documented for the legacy Google Glass Development Kit.** The [observed 2014 developer question](https://stackoverflow.com/questions/23477637/google-glass-sdk-for-epson-moverio) asks whether the monocular Glass GDK can generate distinct left- and right-eye views on binocular Epson Moverio. The [Google GDK](https://developers.google.com/glass/develop/gdk) was built for Google Glass-specific hardware and APIs; it is **not an Epson stereoscopic SDK**. The original discussion's historical answer also reports no Glass-native stereo support; that community answer is not a current vendor certification.

For Moverio, use the **SDK matching the exact Epson headset and host**. Epson's [Moverio Basic Function SDK](https://tech.moverio.epson.com/en/basic_function_sdk/developers_guide/introduction.html) documents Android development with display/camera/sensor access and a [Unity development route](https://tech.moverio.epson.com/en/basic_function_sdk/developers_guide_unity/developing_apps.html). Crucially, Epson says this modern Basic Function SDK **does not support BT-350 and earlier**; those models require their own legacy SDK. Stereo output, marker tracking and alignment must be implemented and tested through a compatible Moverio toolchain, not assumed from a Glass APK.

**Limits:** No Epson device or historical GDK compatibility test was conducted. This does not claim that Epson never shipped third-party marker tools or that all current Moverio models share one SDK. Reviewed October 26, 2026.
