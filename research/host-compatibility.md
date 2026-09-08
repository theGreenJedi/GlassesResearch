# Host Compatibility Research

Smart-glasses compatibility questions often look simple—"will these work with my phone/laptop/console?"—but the answer depends on transport, power, operating-system support, adapters, vendor software and the exact glasses generation.

GlasssesResearch records those relationships as structured evidence rather than producing one-off search-targeted articles.

Machine-readable records: [`data/host-compatibility.json`](../data/host-compatibility.json)

## What must be separated

For every model/host relationship, distinguish:

- **physical connector** — USB-C, HDMI path, proprietary connector, Bluetooth, Wi-Fi or another transport;
- **video/data protocol** — for example DisplayPort Alt Mode rather than assuming all USB-C ports carry video;
- **power source** — whether the host powers the glasses or a powered adapter/battery is required;
- **direct versus adapted connection** — and the exact adapter class when one is required;
- **supported operating mode** — basic mirrored display, 3DoF/spatial mode, application-specific control, audio, camera/data access or another capability;
- **software dependency** — vendor app, driver, SDK, companion device, account or cloud service;
- **evidence state** — manufacturer-primary, GlassesResearch verified, attributed community report, or unknown;
- **last verification date** — because phone firmware, console software and vendor applications change.

## Evidence rules

1. A USB-C connector does **not** prove DisplayPort Alt Mode.
2. A family-level capability does not automatically prove every device/adapter combination.
3. "Works" must identify what works. Mirrored video is different from spatial tracking, audio, camera/data access or vendor-app integration.
4. A community report may establish an attributed compatibility observation but does not become a universal specification.
5. Missing data stays **unknown** rather than being converted into an unsupported "no."
6. Compatibility pages should be generated from evidence records when useful; search demand may reveal a question worth answering, but it does not determine the answer.

## Initial verified records

The initial dataset starts conservatively with XREAL One-family transport behavior because XREAL's current documentation explicitly describes compatible hosts as providing video through USB-C DisplayPort Alt Mode and supplying power to the glasses.

That establishes the **transport rule**, not universal support for every phone, handheld, laptop or console. Named host combinations should be added only when primary documentation, GlassesResearch testing or reproducible attributed community evidence establishes them.

Primary source: https://tutorials.xreal.com/docs/glasses/one-series/first-use/connect-device/

## Research backlog

Priority expansions:

- current XREAL, VITURE, RayNeo and Rokid display-glasses host matrices;
- handheld/console paths where adapters or docks are required;
- Apple and Android phone video-output distinctions;
- power-injection requirements and failure modes;
- spatial-mode versus basic-display differences;
- firmware/application changes that break previously working host combinations;
- owner-controlled generic display paths that survive after vendor applications disappear.

This framework exists to make GlassesResearch more useful without turning compatibility into keyword-driven content.
