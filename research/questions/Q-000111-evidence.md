---
description: Claim-level evidence and publication limits for original observed Q-000111.
---

# Q-000111 — How can a Vuzix Blade client trust a HTTPS or WSS test server certificate without modifying system CA files?

**Original observed question:** I'm having difficulty installing the certificate on the Vuzix Blade, are you able to elaborate on how you implemented it?

**Original observation:** [Source](https://github.com/Vuzix/M300_Vuzix_WebRTC_Demo_Server_and_Application/issues/1) (preserved in canonical registry; reviewed October 31, 2026). The observation is not itself device verification.

## Claim-level provenance

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Original Blade system CA write failure | [Source](https://github.com/Vuzix/M300_Vuzix_WebRTC_Demo_Server_and_Application/issues/1) | Unresolved developer report, not a device-wide impossibility |
| Vuzix demo's TLS/WSS path not implemented as shipped | [Source](https://github.com/Vuzix/M300_Vuzix_WebRTC_Demo_Server_and_Application) | Maintainer README, not a runtime test |
| App-scoped custom/debug CA configuration; Android API 24+ default trust | [Source](https://developer.android.com/privacy-and-security/security-config) | Android platform guidance; library-specific TLS trust needs verification |
| Browser media APIs require secure context | [Source](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) | Does not establish embedded client TLS or WebRTC behavior |

## Uncertainty and publication gate

Canonical proposed FAQ: `docs/faq/09-development-openness.md#how-can-a-vuzix-blade-client-trust-a-https-or-wss-test-server-certificate-without-modifying-system-ca-files`. Existing single directory: `docs/faq/README.md`. The answer separates manufacturer/project assertions, independent technical studies, and community observations. **No GlassesResearch device bench test, guaranteed compatibility, or comparative performance measurement is claimed.**

**State: refreshed research and publication pending.** Do not credit the original registry ID until this publication PR passes editorial, strict links/fragments and all CI checks, merges, the existing main Pages deployment succeeds, and the production-content-proof workflow fetches exact FAQ, directory and evidence pages. Reconcile the original registry row in a follow-up PR with canonical answer_url, publication_verified_at and claim-specific proof. Related Q IDs must not inflate the distinct URL count.
