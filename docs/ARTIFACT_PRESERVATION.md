# Artifact Preservation Initiative

GlassesResearch treats volatile technical artifacts as part of the historical record of the smart-glasses ecosystem.

The preservation system distinguishes **knowing an artifact existed** from **lawfully redistributing its bytes**. A proprietary firmware image, APK, manual, or regulatory exhibit can still have a complete provenance record even when no local copy is published.

## What PR #42 adds

- a dedicated `artifacts/` archive namespace;
- machine-readable `PA-####` preservation records;
- a preservation manifest schema;
- explicit artifact categories for firmware, SDKs, applications, manuals, regulatory records, tools, hardware files, repositories and documentation;
- SHA-256 verification for every locally preserved original;
- CI rejection of unregistered files, bad hashes, malformed records and invalid preservation states;
- initial records for Frame documentation, Brilliant Labs source repositories, Vuzix Android/iOS SDK routes, the FCC authorization registry, the HeyCyan application target and W610 firmware/update-package research;
- public site navigation to the archive policy and metadata.

## What it does not claim

This initiative does not claim that every firmware image, APK, SDK package, FCC exhibit or manual has already been acquired. Where an artifact has not yet been recovered, the record says so explicitly.

That distinction is intentional: **unknown or unavailable is data**. We do not fabricate version numbers, hashes, package names, firmware architectures, licenses or regulatory identities merely to fill a catalog.

## Preservation workflow

1. Identify the exact artifact and its owner/source.
2. Create or promote a `PA-####` ledger record immediately.
3. Capture title, version/date, canonical URL, retrieval time and redistribution status.
4. If lawful original bytes are acquired, hash them before analysis.
5. Store only originals under `artifacts/files/` and record their exact local path and SHA-256.
6. Keep transformed, extracted or reverse-engineered material separate from the original.
7. Record source disappearance or retrieval failure rather than silently deleting the record.

See the [Artifact Preservation Archive](../artifacts/README.md) and [Primary Artifact Preservation Ledger](../resources/PRIMARY_ARTIFACT_PRESERVATION_LEDGER.md).
