# Institutional Collections

This page is the public map of the GlassesResearch research institution. It identifies the collections already present, the material they preserve, and the next substantive additions required.

## 1. Global Device Database

**Current canonical sources**

- [`models/THE_LIST.md`](../models/THE_LIST.md) — purchaser-history ledger of smart-glasses models and generations.
- [`models/CATALOG.md`](../models/CATALOG.md) — broader cross-ecosystem registry.
- [`models/`](../models/README.md) — model chapters and dossier entry points.

**Research fields**

Stable ID, manufacturer, brand, aliases, release year, availability, form factor, display type, camera, audio, sensors, processor, operating system, companion app, SDK/API status, connectivity, battery, openness, hackability, evidence status, preservation status, and primary sources.

**Immediate institutional objective**

Convert catalog entries into comparable structured records while retaining readable model dossiers.

## 2. Manufacturer and Brand Library

Tracks manufacturers, brands, original design manufacturers, rebrands, acquisitions, product families, discontinued lines, and relationships between apparently separate products.

Initial source material exists in The List, the ecosystem catalog, model genealogy notes, official product pages, regulatory filings, and community research.

## 3. Firmware, SDK, API, and Application Archive

**Current canonical sources**

- [`docs/Firmware.md`](Firmware.md)
- [`docs/SDK.md`](SDK.md)
- [`resources/ECOSYSTEM_RESOURCE_CATALOG.md`](../resources/ECOSYSTEM_RESOURCE_CATALOG.md)
- model-specific firmware and application directories.

The collection records versions, release dates, download origins, hashes where lawful files are preserved, compatibility, update behavior, known risks, recovery procedures, and archive status.

## 4. BLE and Protocol Knowledge Base

**Current canonical sources**

- [`docs/BLE.md`](BLE.md)
- model-specific BLE investigations and packet-capture notes.

This collection should preserve service UUIDs, characteristics, advertising behavior, pairing flows, command formats, response formats, packet captures, experimental conditions, and confidence labels.

## 5. Hardware, Optics, Displays, Audio, and Repair Library

**Current canonical sources**

- [`docs/Hardware.md`](Hardware.md)
- model evidence directories
- teardown, lens, prescription, and repair notes inside model chapters.

The collection should connect components and measurements to the models that use them, including frame dimensions, lens geometry, optical engines, speakers, microphones, cameras, batteries, charging systems, sensors, PCB markings, chipsets, and repairability.

## 6. AI Capability Database

Tracks on-device, phone-assisted, and cloud-assisted AI functions; supported models and providers; local-first options; wake and capture flows; translation, OCR, visual question answering, memory, accessibility, and privacy behavior.

Every capability entry should distinguish marketed claims from observed behavior.

## 7. Research Paper, Patent, and Standards Library

The collection should organize primary literature by topic:

- optics and display systems;
- human-computer interaction;
- accessibility and assistive use;
- computer vision and sensing;
- privacy, security, and social acceptance;
- ergonomics, heat, weight, and power;
- AI assistants and memory systems;
- wireless protocols and interoperability.

Each record should include citation, date, authors or issuing body, topic tags, models or technologies discussed, access location, and a short evidence-aware abstract.

## 8. Industry Timeline and Historical Archive

The timeline connects major products, research programs, standards, acquisitions, platform launches, discontinuations, and community milestones. Historical devices are treated as research subjects rather than discarded as obsolete.

See [`docs/INDUSTRY_TIMELINE.md`](INDUSTRY_TIMELINE.md).

## 9. Community and Developer Directory

**Current canonical sources**

- [`resources/ECOSYSTEM_RESOURCE_CATALOG.md`](../resources/ECOSYSTEM_RESOURCE_CATALOG.md)
- model research portals
- glossary entities.

The directory should document GitHub projects, forums, Discords, Telegram groups, Reddit communities, blogs, video channels, independent researchers, repair resources, and archival risks. Links should include annotations explaining why each source matters.

## 10. Preservation Vault

The vault is an evidence and metadata system, not an indiscriminate file mirror.

See [`docs/PRESERVATION_PROGRAM.md`](PRESERVATION_PROGRAM.md).

## 11. Comparison and Discovery Layer

The discovery layer should support:

- model-to-model comparison;
- manufacturer indexes;
- display, camera, audio, AI, and developer-support indexes;
- historical and discontinued-device indexes;
- openness and preservation-status filters;
- glossary and relationship links.

Comparison data must cite the same underlying records used by the model dossiers so the site does not develop conflicting facts.

## 12. Glossary and Knowledge Graph

**Current canonical source**

- [`glossary/README.md`](../glossary/README.md)

The glossary provides canonical homes for recurring entities. The knowledge graph is the relationship layer connecting those entities to models, firmware, applications, companies, communities, papers, standards, and evidence.

## Collection rule

A new collection must ship with substantive records, source links, or an explicit migration of existing knowledge. Empty directories and blank templates do not satisfy the institutional mission.
