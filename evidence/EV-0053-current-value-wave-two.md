# EV-0053 — Current-value wave two

- **Checked:** 2026-08-14
- **Market:** United States / USD
- **Scope:** XREAL One and current Vuzix standalone/enterprise systems
- **Evidence class:** first-party stores, product specifications, and the repository's current-price observations
- **Scoring rule:** one catalog-wide Value ruler; enterprise workflow ROI is described separately and does not erase acquisition cost.

## Current acquisition anchors

| Model | Current first-party price | Capability / ownership context | Value |
|---|---:|---|---:|
| XREAL One — GLS-0074 | $399 sale; $499 regular | Dedicated X1 spatial processor, 1080p-per-eye Micro-OLED, local spatial stabilization, standard host-driven content, no mandatory AI cloud; optional $199 Beam Pro and prescription lenses can raise total cost. | **8.0 at $399; 7.5 at $499** |
| Vuzix Blade 2 — GLS-0055 | $799.99 | Standalone Android, camera, color monocular waveguide, standard application deployment and owner-installable $149.99 prescription assembly. Current price is much lower than launch list but remains premium relative to consumer display/camera glasses. | **6.5** |
| Vuzix M400 — GLS-0098 | $1,499.99 | Rugged XR1 Android wearable, camera/sensors, local apps, hot-swappable external power and current mounts/batteries. Strong field utility; narrow 16.8° occluded display and head-mounted form reduce general acquisition value. | **5.5** |
| Vuzix M4000 — GLS-0099 | $2,499.99 | M400-class compute/control with a higher-value see-through waveguide, but a $1,000 premium over M400. External power and Android deployment preserve ownership utility. | **4.5** |
| Vuzix LX1 — GLS-0100 | $2,199.99 | Current Android 15/QCS4490 warehouse system, 128 GB storage, removable 7000 mAh battery, rugged/freezer operation, accessory ecosystem and long-shift design. Purpose-built industrial utility is high; catalog-wide acquisition value is mixed. | **5.0** |
| Vuzix Shield — GLS-0121 | $2,499.99 | Binocular full-color microLED waveguides, stereo HD cameras, XR1 and Android-oriented developer posture; current price is extremely high and physical-service evidence remains limited. | **5.0** |

## Calibration rationale

XREAL One is a high-value local display peripheral at its checked sale price: its dedicated spatial silicon and standard host architecture deliver substantial utility without bundled standalone-compute or cloud-service costs. The score drops at regular price and total cost must include any Beam Pro, adapter, prescription, or console accessory actually required.

Vuzix products are judged on the same ruler. Their prices can be rational for a company replacing tablets, travel or downtime in a managed workflow, but a hypothetical enterprise ROI cannot be treated as owner acquisition value without a documented deployment. Android application control, ruggedness, replaceable power and parts improve the scores; enterprise pricing, constrained wearability and proprietary internals cap them.

## Primary sources

- XREAL One Series store: https://us.shop.xreal.com/collections/xreal-one-series
- XREAL One specification: https://tutorials.xreal.com/docs/glasses/one-series/spec/
- Vuzix Blade 2: https://www.vuzix.com/en-ca/products/vuzix-blade-2-smart-glasses
- Vuzix M400: https://www.vuzix.com/products/m400-smart-glasses
- Vuzix M400/M4000 technical details: https://support.vuzix.com/docs/m400-m4000-technical-details
- Vuzix LX1: https://www.vuzix.com/products/vuzix-lx1-smart-glasses
- Vuzix current catalog: https://www.vuzix.com/collections/all
- Repository price ledger: ../data/price-observations.json

## Recheck triggers

- Sale expiration or a change in included accessories.
- Model sold-out/discontinued status.
- Required subscription, MDM, cloud license or companion compute.
- Verified depot/field repair pricing.
- Official refurbished or supported secondary-market route.
