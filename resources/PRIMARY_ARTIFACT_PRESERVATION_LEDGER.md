# Primary Artifact Preservation Ledger

**Ledger opened:** 2026-08-05

This ledger records primary technical and product sources that are valuable enough to preserve, hash, archive, or monitor. It does not imply permission to redistribute every downloadable file.

## Status vocabulary

- **linked** — canonical source recorded.
- **metadata-preserved** — title, owner, version/date, retrieval date and redistribution status recorded.
- **archive-requested** — an archival capture should be created or checked.
- **artifact-preserved** — lawful copy and hash stored in an approved durable location.
- **restricted** — useful artifact exists, but redistribution is not justified.
- **lost/unavailable** — previously known source cannot currently be retrieved.

## Active records

| Record | Platform | Artifact or source | Owner | Type | Status | Redistribution | Research value | Next action |
|---|---|---|---|---|---|---|---|---|
| PA-0001 | Brilliant Labs Frame | [Frame hardware manual](https://docs.brilliant.xyz/frame/hardware/) | Brilliant Labs | Hardware manual / schematics index | linked | Site terms and repository licenses must be checked per artifact | Documents display, camera, battery, sensors, Bluetooth, mechanical data and schematic routes | Record page revision; inventory linked schematic and mechanical files; preserve licenses and hashes where allowed |
| PA-0002 | Brilliant Labs ecosystem | [Brilliant Labs GitHub organization](https://github.com/brilliantlabsAR) | Brilliant Labs | Source repositories and releases | linked | Per-repository license | Strong primary source for firmware, applications, SDKs and hardware history | Inventory repositories, default branches, releases, tags and licenses; identify Frame versus legacy Monocle material |
| PA-0003 | Brilliant Labs Halo | [Halo product and specification page](https://brilliant.xyz/products/halo) | Brilliant Labs | Product specification / availability record | metadata-preserved | Commercial page; archive rather than mirror | Captures launch claims, prescription route, openness claims, subscription and shipping statements | Archive dated snapshot and compare delivered hardware/source releases against launch claims |
| PA-0004 | Vuzix Z100 | [Official product page](https://www.vuzix.com/products/z100-smart-glasses) | Vuzix | Product specification | metadata-preserved | Commercial page; archive rather than mirror | Records display, BLE, battery, prescription inserts and SDK availability | Archive dated page and downloadable product sheet; hash distributable documents if terms permit |
| PA-0005 | Vuzix Z100 | [Developer overview](https://support.vuzix.com/docs/overview-28) | Vuzix | Developer documentation | linked | Documentation terms must be reviewed | Defines supported phone-to-glasses functions and official SDK model | Preserve documentation index and SDK repository links; record Android/iOS requirements by version |
| PA-0006 | Vuzix Z100 | [Android SDK documentation](https://support.vuzix.com/docs/sdk-for-android) | Vuzix | SDK documentation / repository route | linked | Per SDK repository license | Establishes Android requirements and supported operations | Record exact GitHub repository, latest release/tag, license and dependency on Vuzix Connect |
| PA-0007 | Vuzix Z100 | [iOS SDK documentation](https://support.vuzix.com/docs/sdk-for-ios) | Vuzix | SDK documentation / repository route | linked | Per SDK repository license | Establishes iOS, watchOS and macOS support route | Record repository, release/tag, license and minimum platform versions |
| PA-0008 | Mentra ecosystem | [MentraOS repository](https://github.com/Mentra-Community/MentraOS) | Mentra Community | Source repository / platform | linked | Per repository license | Cross-device application and compatibility platform | Preserve release/tag metadata, supported-device matrix, license, package names and migration history from AugmentOS naming |
| PA-0009 | Open smart-glasses hardware | [OpenSourceSmartGlasses repository](https://github.com/Mentra-Community/OpenSourceSmartGlasses) | Mentra Community | Hardware/software project | linked | Per repository license | BOM, CAD, PCB, firmware and build research potential | Inventory directories and licenses; identify released manufacturing files and reproducible build state |
| PA-0010 | Solos AirGo | [Solos developer page](https://solosglasses.com/pages/developers) | Solos | SDK capability statement | metadata-preserved | Commercial documentation; SDK license separate | Defines model coverage, BLE control and Wi-Fi data differences | Locate canonical SDK downloads/repositories, version history, API docs and license |
| PA-0011 | W610 / HeyCyan | [W610 research portal](../models/W610/resources/RESEARCH_PORTAL.md) | GlassesResearch | Curated source map | repository-native | Project content | Canonical route to volatile seller, app, registry and community sources | Convert each high-value external lead into its own preservation record rather than citing broad searches |
| PA-0012 | W610 / Goodway | [Goodway W610 product page](https://www.goodwaytechs.com/goodway-ai-smart-glasses-with-8mp-camera-real-time-translation-ip65-waterproof-42g-lightweight-w610.html) | Goodway Techs | Supplier specification | archive-requested | Commercial page; archive rather than mirror | One of the clearest W610 supplier and customization claims | Capture dated page, images and downloadable materials; compare claims with other suppliers and hands-on evidence |
| PA-0013 | Smart-glasses regulation | [FCC Equipment Authorization search](https://www.fcc.gov/oet/ea/fccid) | US FCC | Regulatory database | linked | Public record; individual exhibits may have grant-specific confidentiality | Internal photos, labels, reports and applicant identity | Add device-specific records only after an FCC ID/applicant match is established |
| PA-0014 | Bluetooth products | [Bluetooth SIG qualification search](https://launchstudio.bluetooth.com/Listings/Search) | Bluetooth SIG | Qualification database | linked | Database terms apply | Applicant, product and component relationships | Add stable records for exact declarations only; do not infer product identity from chipset qualification alone |

## Minimum record for a downloaded artifact

```yaml
record_id: PA-0000
platforms:
  - canonical-platform-id
title: Exact artifact title
source_owner: Organization or person
canonical_url: https://example.invalid
retrieved_utc: 2026-08-05T00:00:00Z
published_or_version: unknown
filename: original-filename.ext
sha256: lowercase-hex
media_type: application/pdf
license: unknown
redistribution: allowed | restricted | unknown
preservation_status: metadata-preserved | artifact-preserved | restricted
archive_url: unknown
notes: >-
  Explain provenance, relevance, uncertainty and any transformation.
```

## Preservation priorities

1. Volatile W610 supplier pages, manuals, application metadata and support routes.
2. Official SDK repositories, tagged releases and documentation indexes.
3. Open hardware files whose licenses permit durable preservation.
4. Regulatory exhibits tied to a verified model or applicant.
5. End-of-life application, firmware and manual records for discontinued products.

## Legal and quality rules

- Preserve a canonical URL even when a lawful local copy exists.
- Record the license before mirroring source, binaries, CAD or documentation.
- Hash original files before analysis or conversion.
- Never replace an original with a modified copy.
- Do not treat an archived commercial claim as independent verification.
- Record retrieval failures and dead links; disappearance is itself historical evidence.
- Prefer one complete, provenance-rich record over many unexplained downloads.