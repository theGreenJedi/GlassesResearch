# Q-000131 — Sony SmartEyeglass microphone input

**Observed question:** [2016 Sony Smart Glasses Mic Input](https://stackoverflow.com/questions/36347593/sony-smart-glasses-mic-input), Q-000131 in the canonical registry. **Reviewed:** 2026-10-26.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Original user asked whether the touch-controller mic was mandatory or whether a Bluetooth microphone on the phone could control menus | [Original question](https://stackoverflow.com/questions/36347593/sony-smart-glasses-mic-input) | User question, not an implementation report |
| SmartEyeglass controller has a microphone and built-in asynchronous voice-to-text input via `enableVoiceTextInput()` with `onVoiceTextInput()` callback | [Sony SmartEyeglassControlUtils](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassControlUtils), [Sony event listener](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassEventListener) | Manufacturer API, legacy hardware; no independent bench test |
| SmartEyeglass can operate as Bluetooth headset for host-phone audio; standard HFP applies | [Sony control API](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassControlUtils) | Does not guarantee arbitrary external microphone is routed to the glasses' built-in voice-to-text operation |
| Sony voice-to-text requires SmartEyeglass and VOICE_TEXT_INPUT permissions and a Talk-button operation | [Sony API permissions and methods](https://developer.sony.com/reference/seg-sdk/com/sony/smarteyeglass/extension/util/SmartEyeglassControlUtils) | SDK-specific interaction, not a general hands-free menu controller |
| Generic Android recording requires RECORD_AUDIO and runtime consent on modern Android | [Android MediaRecorder guide](https://developer.android.com/media/platform/mediarecorder) | Host-app path, separate from Sony's controller API |

## Verification and publication gate

The original question is from 2016; SDK behavior and device support are historical. No GlassesResearch hardware or external Bluetooth microphone routing test was performed. The FAQ distinguishes Sony's documented controller mic/voice-text path from unverified alternative microphone routing and explains the need for explicit app menu mapping. **State: researched; publication pending exact live FAQ and directory verification.** Proposed anchor: `docs/faq/09-development-openness.md#can-sony-smarteyeglass-use-voice-input-from-a-microphone`.

## Publication proof — 2026-10-26

[PR #698](https://github.com/theGreenJedi/GlassesResearch/pull/698) merged as revision `2262054aaa16529f36e768925535be576f9a17b6` after documentation, editorial, link/fragment, deploy and Lighthouse checks passed. [Production content proof #40396645760](https://github.com/theGreenJedi/GlassesResearch/actions/runs/40396645760) succeeded: fetched the complete public FAQ `/docs/faq/09-development-openness/` (digest `4208f6df07f5`), Practical Answers directory `/docs/faq/` (digest `3f42fb3fe4bc`), and this evidence page (digest `01d2dbc8dcc3`) matching the deployed build. The directory links to the exact built-page anchor [published answer](https://glassesresearch.org/docs/faq/09-development-openness/#can-sony-smarteyeglass-use-voice-input-from-a-microphone), validated by strict internal fragment checks. This proves content publication, **not** a device or SDK bench test. Registry Q-000131 was credited only after this proof; original observations and uncertainty remain intact.
