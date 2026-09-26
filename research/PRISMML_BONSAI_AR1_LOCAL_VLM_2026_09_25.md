# PrismML Bonsai on Snapdragon AR1 Gen 1 — local VLM evidence

## Evidence identity

PrismML announced and demonstrated a roughly 2B-parameter vision-language model running locally on a Snapdragon AR1 Gen 1 smart-glasses platform.

The configuration combines a **1.7B 1-bit language model** with a **0.3B 4-bit vision encoder**. PrismML says the model and Qualcomm Hexagon NPU were co-optimized for constrained wearable hardware.

Primary source:

- https://prismml.com/news/prismml-brings-1-bit-bonsai-models-to-ai-smart-glasses-powered-by-snapdragon

Independent coverage:

- https://techcrunch.com/2026/09/24/prismml-brings-its-tiny-llms-to-qualcomm-powered-smart-glasses/

## Published test conditions

PrismML's footnotes attribute AR1 Gen 1 testing to Qualcomm Technologies International in September 2026 on a 4 GB platform with a 1,024-token context and an internal QNN SDK with 1-bit kernel support.

Reported LLM-weight memory was **0.43 GB** for the 1-bit 1.7B language model versus **1.66 GB** for the corresponding 4-bit model. Reported generation was **15.36 tokens/s** versus **7.44 tokens/s**.

These are vendor/partner benchmark results, not GlassesResearch measurements.

## Architectural significance

This adds a fifth pattern to the local-agent research map: **useful multimodal inference may run on glasses-class silicon itself**.

That does not make cloud or host compute obsolete. Model quality, sustained thermals, battery cost, camera pipeline cost, context limits and application integration remain open questions. No commercial glasses using Bonsai have been announced.

Treat this as strong architectural evidence, not as evidence that a shipping product is cloud-independent.
