# AI, cameras, audio, and connectivity

“AI” often describes a cloud service reached through the phone rather than intelligence running entirely inside the glasses.

**Information reviewed:** 2026-08-05. Product availability, software, prices, and advertised battery life can change. Unless explicitly marked hands-on, statements below are sourced from manufacturers, project documentation, or attributed community material.

## 51. Do AI glasses run AI locally on the glasses?

Usually only limited models or signal processing run on the frame. Speech recognition, vision-language reasoning, and web answers commonly use a phone and cloud services. Brilliant Halo advertises an onboard low-power NPU, while MentraOS is moving miniapps to a local phone runtime. Ask which functions work offline, where images/audio go, and whether a cloud account is mandatory. Sources: [Brilliant Halo](https://brilliant.xyz/products/halo), [MentraOS architecture](https://mentraglass.com/blogs/blog/mentra-roadmap-update-moving-to-miniapps-on-the-phone).

## 52. Can AI glasses work without internet access?

Basic capture, audio, controls, and some display functions may work offline, but generative AI, web search, translation, and scene analysis often need a phone data connection. Tethered display glasses can show offline content from a computer or handheld. Verify each required feature in airplane mode before depending on it.

## 53. Which smart glasses let users choose the AI model?

Solos advertises integrations spanning ChatGPT, Claude, Gemini, and DeepSeek; MentraOS is intended to give developers and users a cross-hardware app layer; HTC has promoted multi-provider AI for VIVE Eagle. Model availability can be regional, subscription-dependent, or changed by software updates. Sources: [Solos AirGo V2](https://solosglasses.com/blogs/news/solos-airgo-v2-modular-smart-glasses-with-camera-and-accessible-ai), [MentraOS](https://mentraglass.com/os), [VIVE](https://www.vive.com/).

## 54. Which smart glasses are best for voice assistants?

Ray-Ban Meta is the polished mainstream choice for Meta AI and connected communication. Solos is attractive for multi-assistant experimentation, while Mentra Live is the developer-oriented choice for custom voice workflows. Audio quality, wake-word reliability, country support, contact integrations, and account requirements should decide the purchase. Sources: [Ray-Ban Meta FAQ](https://www.ray-ban.com/usa/c/frequently-asked-questions-ray-ban-meta-smart-glasses), [Solos](https://solosglasses.com/), [Mentra Live](https://mentraglass.com/live).

## 55. Which smart glasses have the best camera?

Camera quality cannot be ranked by megapixels alone. Ray-Ban Meta Gen 2 offers a mature 3K consumer capture pipeline; Mentra Live advertises a 12 MP camera and stabilized livestreaming; Solos AirGo V2 advertises 16 MP. Image processing, orientation, stabilization, low light, aspect ratio, heat, and app export matter more than the sensor number. Sources: [Ray-Ban FAQ](https://www.ray-ban.com/usa/c/frequently-asked-questions-ray-ban-meta-smart-glasses), [Mentra announcement](https://mentraglass.com/blogs/blog/our-first-press-release-mentra-releases-first-smart-glasses-with-an-app-store), [Solos AirGo V2](https://solosglasses.com/blogs/news/solos-airgo-v2-smart-glasses-bring-ai-16mp-camera-and-live-streaming-power).

## 56. Can smart glasses livestream video?

Some can. Ray-Ban’s official FAQ currently says its Facebook/Instagram livestream feature is available only on Gen 1, an important generational caveat. Mentra Live and Solos AirGo V2 advertise live video workflows. Livestreaming produces heavy battery, heat, bandwidth, privacy, and moderation demands. Sources: [Ray-Ban FAQ](https://www.ray-ban.com/usa/c/frequently-asked-questions-ray-ban-meta-smart-glasses), [Mentra Live](https://mentraglass.com/live), [Solos AirGo V2](https://solosglasses.com/blogs/news/solos-airgo-v2-smart-glasses-bring-ai-16mp-camera-and-live-streaming-power).

## 57. Can smart glasses make phone calls and play music?

Audio-equipped models such as Ray-Ban Meta, Solos AirGo, Halliday G2, and Mentra Live can handle calls or audio. Camera-free display-only products such as Even G2 intentionally omit speakers, and tethered XR glasses act more like external displays/audio devices. Check microphone wind performance, sound leakage, Bluetooth multipoint, and continuous-audio battery life.

## 58. Do smart glasses need Bluetooth, Wi-Fi, or both?

Bluetooth commonly handles control, audio, notifications, and low-rate data to a phone. Wi-Fi may transfer media, support higher-bandwidth video, or connect a companion compute device. Some low-cost camera glasses expose multiple radios or device identities. A radio’s presence does not imply an open protocol; protocol documentation and captured services matter.

## 59. Can smart glasses connect to iPhone and Android?

Many do, but feature parity varies. Ray-Ban Meta supports compatible recent iOS and Android phones; Mentra app support spans both; Vuzix Z100 provides Android and iOS SDK paths. Tethered display glasses require a compatible video output, which many—but not all—USB-C phones provide. Verify the exact phone model and OS version. Sources: [Ray-Ban Meta FAQ](https://www.ray-ban.com/usa/c/frequently-asked-questions-ray-ban-meta-smart-glasses), [Mentra Live](https://mentraglass.com/), [Vuzix Z100 SDK](https://support.vuzix.com/docs/overview-28), [VITURE compatibility](https://www.viture.com/compatibility).

## 60. Can AI glasses translate conversations in real time?

They can provide useful machine translation, but `real time` does not mean simultaneous, perfect, private, or offline. Accuracy varies with language pair, noise, accents, context, speaker separation, and network latency. Use translated text or audio as assistance, not as the sole authority for medical, legal, safety, or contractual communication.

## Which smart glasses can translate speech offline?

**Some Meta AI glasses have a documented offline live-translation path, but “supports translation” does not mean every language pair works without internet.** [Meta's September 2025 announcement](https://about.fb.com/news/2025/09/ray-ban-meta-gen-2-better-battery-life-video-capture/) described downloaded language packs for back-and-forth translation among **six languages**, including use in airplane mode. That is a manufacturer capability statement for supported Meta glasses, not an independent GlassesResearch offline test or proof that every subsequent language rollout has an offline pack. Check the exact model, region, app version, supported **pair**, and installed pack before relying on it.

By contrast, [Even Realities' G2 Conversate instructions](https://support.evenrealities.com/hc/en-us/articles/14273795154319-Conversate) explicitly require the paired phone to have internet before starting live transcription/translation. Do **not** treat its downloadable app, saved transcript history, or a glasses display as proof of offline translation. The processing may be on a phone rather than inside the frame even when the user-facing function works without internet.

**Practical offline acceptance test:** install the chosen packs while online; then disable cellular and Wi-Fi on the phone while leaving Bluetooth available, start a fresh session, and try both directions of the exact language pair with normal conversation and background noise. Record whether the feature starts, the result appears or is spoken, and the delay. A failed test should override marketing shorthand. [Original observed question](https://www.reddit.com/r/SmartGlasses/comments/1xgxt02/what_smart_glasses_have_offline_live_translation/). Reviewed October 29, 2026; no device bench verification.

## How do I troubleshoot Even G2 microphone speech-recognition failures?

**Isolate the input path before assuming the glasses microphone is broken.** [Even Realities' official G2 guide](https://support.evenrealities.com/hc/en-us/articles/17206473148815-Voice-Features-Do-Not-Work-with-the-G2-Microphone) says to open **Conversate** or **Translate**, select **Glasses** as the audio source, and check whether recognized text appears in both app and glasses. Repeat with **Phone** selected. **Even AI does not allow its input source to be switched** in that menu. [Even's recognition guide](https://support.evenrealities.com/hc/en-us/articles/17203734229775-Even-AI-Voice-Recognition-Is-Inaccurate) separately says to verify the spoken-language setting and test in a relatively quiet place.

If still failing, Even documents a restart by **rapidly tapping both touchpads five times**, waiting for the beep, force-closing/reopening the companion app, and repeating both microphone tests. If recognition works from the phone but not the glasses, that narrows the failure to the glasses-input path **without proving physical microphone damage**. If both fail, do not diagnose a bad glasses microphone from that result. Even also recommends testing another phone network if Even AI reports an error before speech finishes: [network troubleshooting](https://support.evenrealities.com/hc/en-us/articles/17203580053519-Even-AI-Reports-an-Error-Before-You-Finish-Speaking).

For unresolved failures, send Even Support the G2 serial number, exact time, tests performed, app logs, and—if possible—a video showing transcription with each input. [Original observed report](https://www.reddit.com/r/SmartGlasses/comments/1xghpj8/even_g2_mic_issues_ai_cant_understand_suggestions/). Reviewed October 29, 2026; no independent G2 microphone test.

## How do people input commands into AI glasses, and what tradeoffs matter?

**There is no single input method across AI wearables.** The documented options include wake-word speech, touchpad/button gestures, a paired phone, and accessory controllers. [Ray-Ban Meta's FAQ](https://www.ray-ban.com/usa/c/frequently-asked-questions-ray-ban-meta-smart-glasses) documents voice requests and touch controls for photos, video and media. [Even G2's menu guide](https://support.evenrealities.com/hc/en-us/articles/14269160297999-Menu) documents temple touchpad navigation and optional R1 ring input; [Even's microphone troubleshooting](https://support.evenrealities.com/hc/en-us/articles/17206473148815-Voice-Features-Do-Not-Work-with-the-G2-Microphone) distinguishes phone and glasses microphone paths for some features.

**The irritating part depends on the task, and no representative user poll is established here.** Voice can be socially awkward, noisy or privacy-sensitive; touch requires memorized gestures and can misfire; a phone restores precise text entry but undermines hands-free use; a ring adds another device to charge and pair. For an AI pin, do not assume glasses controls transfer to it—check that pin's own documentation.

**Try four tasks before deciding:** issue a short private command in a quiet room, repeat in traffic/crowd noise, enter a correction to a name or address, and recover from a missed gesture or lost connection. Count attempts, latency and whether you had to take out the phone. The [original owner-experience question](https://www.reddit.com/r/SmartGlasses/comments/1xj81yv/if_you_use_ai_glasses_or_an_ai_pin_how_do_you/) invites firsthand reports; this answer describes documented control paths and a testing method, **not** a fabricated consensus about which annoyance is most common. Reviewed October 30, 2026.

## Which smart glasses are best for live translation, and how should I choose?

**There is no defensible universal winner without your language pair and output needs.** First decide whether you need **translated text in your eyes**, spoken translation through speakers, or both; then check the exact source and target languages, two-way conversation mode, region, phone compatibility, connectivity, prescription fit, subscription and privacy/retention policy.

For example, [RayNeo iO's product page](https://www.rayneo.com/pages/rayneo-io-ai-glasses) advertises **on-lens live captions/translation in 55 languages**, whereas [RayNeo X3 Pro's specifications](https://www.rayneo.com/products/x3-pro-ai-display-glasses?variant=51473095033119) list **14-language real-time translation**. These counts are manufacturer marketing for different products, **not** measured accuracy or a promise that every pair, direction, accent or offline mode is supported. [Even G2's translation troubleshooting](https://support.evenrealities.com/hc/en-us/articles/18153388264975-Translate-Shows-No-Translated-Text-on-G2) warns that some languages' fonts may appear on the phone but **not** on the glasses, and describes switching between phone and glasses microphones when text fails.

**Practical acceptance test:** take a real conversation in your target pair, test both directions in background noise, note end-to-end delay and missed names/numbers, then repeat without internet if offline use matters. Check whether the display renders the script and whether the other speaker must use your phone. Never infer translation reliability from language counts alone.

The [original community question](https://www.reddit.com/r/SmartGlasses/comments/1xk2omw/best_glasses_for_translation/) did not specify a pair or scenario. These are attributed product and support claims, **not GlassesResearch comparative translation benchmarks**. Reviewed October 31, 2026.
