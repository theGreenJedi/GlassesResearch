# SDK, Apps, and APIs

## Purpose

Catalog vendor applications, SDKs, libraries, network services, and integration surfaces associated with W610/W6xx smart glasses.

## Current position

The vendor application exists, but this project prefers to establish a device baseline before depending on it. Vendor-independent and local-first control paths are a primary research goal.

## Application inventory

| App or package | Platform | Version | Source | Hash | Notes |
|---|---|---|---|---|---|
| HeyCyan app | TBD | TBD | TBD | TBD | Preserve before analysis |

## Analysis checklist

- [ ] Record official store listing and developer identity
- [ ] Preserve legally obtainable installers and version metadata
- [ ] Inspect requested permissions
- [ ] Inventory embedded domains, API endpoints, UUIDs, and native libraries
- [ ] Observe network traffic in an authorized test environment
- [ ] Compare behavior online and offline
- [ ] Identify account requirements and cloud dependencies
- [ ] Document exported components and supported intents or URL schemes
- [ ] Search for public SDK documentation and sample code

## Integration goals

- Phone-mediated local processing
- User-selected AI model
- Cloud use as an optional fallback rather than a requirement
- Open, documented interfaces
- Minimal data collection
- Replaceable application layer where technically possible

## Open questions

- Is there an official SDK available to retail buyers?
- Does the vendor app communicate with the glasses through BLE, classic Bluetooth, Wi-Fi, or a combination?
- Which functions remain available without an account or internet connection?
- Are related models using the same application protocol?
