# Artifact Preservation Archive

GlassesResearch preserves the **existence, provenance, integrity, and retrieval history** of smart-glasses artifacts even when redistribution is not permitted.

This archive complements [`resources/PRIMARY_ARTIFACT_PRESERVATION_LEDGER.md`](../resources/PRIMARY_ARTIFACT_PRESERVATION_LEDGER.md). The ledger is the human research queue; `artifacts/records/` contains machine-valid preservation records.

## What belongs here

- firmware and firmware-update packages;
- SDKs, API packages, headers, examples, and release archives;
- Android APK metadata and other companion-application packages;
- manuals, quick-start guides, service documentation, safety sheets, and product sheets;
- FCC and other regulatory exhibits tied to an identified device or applicant;
- flashing, recovery, BLE, packet-capture, reverse-engineering, and diagnostic utilities;
- open hardware, CAD, PCB, BOM, and manufacturing files.

## Archive-first rule

A useful artifact should not disappear merely because its original host disappears. Preserve at least its metadata and canonical source immediately. Preserve the bytes only when doing so is lawful and appropriate.

A missing local file does **not** mean an artifact is unimportant. Records may intentionally be `metadata-preserved`, `archive-requested`, or `restricted`.

## Directory model

```text
artifacts/
  README.md
  manifest.schema.json
  records/             # one JSON provenance record per PA identifier
  files/               # lawful preserved originals only
    firmware/
    sdk/
    apps/
    manuals/
    regulatory/
    tools/
    hardware/
```

The repository should never contain unexplained binaries. Every file under `artifacts/files/` must have a matching record containing its original filename, SHA-256, source owner, canonical URL, retrieval timestamp, media type, license/redistribution status, and preservation status.

## Preservation states

- `linked` — canonical source is known.
- `metadata-preserved` — provenance metadata has been captured.
- `archive-requested` — a durable capture should be created or checked.
- `artifact-preserved` — lawful original bytes and SHA-256 are preserved.
- `restricted` — artifact is known but local redistribution is not justified.
- `lost-unavailable` — known artifact/source cannot currently be retrieved.

## Integrity rule

When original bytes are preserved:

1. hash the untouched original first;
2. record SHA-256 in the matching record;
3. never overwrite the original with an analyzed or modified copy;
4. store transformed/extracted material separately and identify its parent artifact.

## Licensing rule

Open-source does not mean every file on a vendor site is redistributable. Record licensing and redistribution status per artifact. When uncertain, preserve metadata and links rather than copying bytes.

## Current seed set

PR #42 seeds records covering official documentation, SDK routes, open-source repositories, the W610 supplier/app investigation routes, and regulatory search infrastructure. It does not claim that every firmware/APK/manual has already been recovered. Unknown binaries remain preservation targets rather than guessed artifacts.
