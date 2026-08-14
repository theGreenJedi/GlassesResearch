# EV-0061 — CyanBridge Qwen2.5 local-model boundary

**Status:** Community-primary release evidence; GlassesResearch reproduction pending  
**Verified against:** CyanBridge release `v2.0.0` and current release line through `v2.1.1`  
**Reviewed:** 2026-08-14  
**Affected scope:** CyanBridge on Android with compatible HeyCyan smart glasses

## Question

Does CyanBridge establish a phone-local Qwen pathway for HeyCyan-compatible glasses, and which capabilities can defensibly be attributed to Qwen?

## Finding

CyanBridge v2.0.0 lists **Qwen2.5 0.5B and 1.5B** in its curated local-model catalog. The same release documents local inference through **llama.cpp using GGUF models** and says that data remains on the Android phone when a local model is selected.

This is evidence of a user-selectable, phone-local language-model path connected to the HeyCyan companion workflow. It is not evidence that Qwen runs on the glasses themselves.

The release separately attributes multimodal image/audio input through LiteRT to **Gemma 4** models. The release does not establish multimodal image or audio support for the listed Qwen2.5 models. GlassesResearch therefore records Qwen2.5 here as a local text-model option and does not transfer Gemma-specific multimodal claims to Qwen.

## Established from the community release

- CyanBridge exposes llama.cpp/GGUF and LiteRT local-runtime paths.
- Its curated catalog names Qwen2.5 0.5B and 1.5B.
- Local-model operation is available without the paid cloud subscription.
- Model controls include temperature, top-p, top-k, context size and repetition penalty.
- The developer recommends at least 4 GB of phone RAM for Gemma 4 E4B; this is not a Qwen-specific memory benchmark.
- CyanBridge v2.1.1 retains local-agent diagnostics and fixes independently hosted OpenAI-compatible endpoints, but those remote endpoints are a separate architecture from phone-local Qwen execution.

## Not established

- Successful GlassesResearch reproduction on Pete's owned W610.
- Exact Qwen quantization files, hashes, licenses or download origins used by every app build.
- Qwen image, audio or continuous-camera understanding in CyanBridge.
- On-glasses inference.
- Offline speech recognition, text-to-speech or every end-to-end assistant step.
- Battery, latency, heat, memory pressure or sustained reliability on a representative Android phone.
- That no data leaves the phone under every optional feature or configuration.

## Why it matters

This is a concrete implementation of the architecture GlassesResearch evaluates: **glasses → owner-controlled phone → user-selected local model**. Even inexpensive camera glasses can remain useful when their intelligence is replaceable, but the evidence must distinguish local language inference from capture, speech, storage and multimodal processing.

## Sources

- [CyanBridge v2.0.0 — Local AI Support](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/releases/tag/v2.0.0)
- [CyanBridge v2.1.1](https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK/releases/tag/v2.1.1)

## Preservation note

The tagged release URLs and capability boundary are recorded. GlassesResearch does not redistribute model weights or CyanBridge release artifacts in this evidence note.
