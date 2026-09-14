# Zetronix Lark / zShades-2K identity and architecture — 2026-09-14

**Status:** resolved for canonical catalog admission  
**Conclusion:** Zetronix **Lark** is the marketed product identity; **zShades-2K** is the SKU / support-document identity for the same product, not a second model.  
**Evidence lanes:** primary-source product page and primary-source manual; architecture characterization is explicitly labeled as inference.

## Identity and purchaser-history evidence

Zetronix currently sells **Lark - SuperHD WIFI Video Recording Sports Camera Sunglasses** through its own store. The product page is in stock, exposes an Add to Cart path, and identifies the SKU as **zShades-2K**.

Source: https://www.zetronix.com/lark-superhd-wifi-video-recording-sports-camera-sunglasses.html

Zetronix's support center separately indexes **zShades-2K** and labels its associated image/product as **Lark - SuperHD WIFI Video Recording Sports Camera Sunglasses**. The support article is dated November 17, 2021, establishing that this Lark / zShades-2K identity was documented by Zetronix by that date.

Sources:

- https://help.zetronix.com/hc/en-us/articles/4413822403341-zShades-2K
- https://help.zetronix.com/hc/en-us/categories/360004273352-Product-User-Manuals

## Documented-versus-marketing discrepancy

The current sales page markets the Lark as **"2.7K SuperHD 2560 x 1440 at up to 60fps."** Zetronix's linked zShades-2K user manual instead specifies **2K (2560 x 1440) at 30 fps**, with 1080p and 720p modes at 60 fps.

Manual: https://help.zetronix.com/hc/article_attachments/4417200367117

These statements remain side by side as a provenance-aware discrepancy. GlassesResearch does not silently promote the current 60 fps marketing statement to independently verified hardware capability, and does not erase the older/manual 30 fps specification.

## Local recording and owner-control architecture

The manual documents hardware-button recording, removable microSD storage up to 128 GB, USB storage mode, and direct file access from a computer. It also documents a separately switched Wi-Fi function used for smartphone live view, control and media transfer.

**Inference:** this is reasonably characterized as a **local-first capture architecture** because core recording and storage do not require the phone app or a cloud service in the documented workflow. That label is an architectural inference from the manual, not a GlassesResearch bench verification and not a claim that every software path is cloud-independent.

## Wi-Fi / default-credential note

The manual publishes a default Wi-Fi network name and a shared default password for the glasses' local Wi-Fi connection. GlassesResearch preserves the existence of that documented default credential as an owner-control/security note without reproducing the password in the public model summary. The available documentation does not establish per-device credential uniqueness or mandatory credential rotation.

## Other documented hardware facts

The manual describes:

- 46 g physical weight;
- 135-degree camera field of view;
- H.265 recording;
- removable microSD storage up to 128 GB;
- USB-C / USB 2.0 interface;
- approximately 1.5 hours documented power duration;
- recording while externally powered;
- visible LED and vibration state indications;
- interchangeable lenses, with the manual describing ANSI Z87.1-related lens claims.

These remain **manufacturer-documented claims**, not independently reproduced lab measurements.

## Canonical decision

- Admit one canonical model as **Zetronix Lark**.
- Preserve **zShades-2K** as SKU / alias evidence attached to Lark rather than minting a second canonical row.
- Preserve the 2021 support/manual evidence as lineage history while retaining the current first-party purchase state.
- Preserve the 30 fps manual versus up-to-60 fps current-marketing discrepancy explicitly.
- Preserve local recording / removable storage / optional Wi-Fi behavior as documented architecture, with any broader owner-control conclusion labeled as inference until bench-tested.

## Evidence boundary

This resolution establishes identity, documented architecture and a current first-party acquisition path. It does not independently verify image quality, frame rate, battery runtime, lens certification, durability, privacy behavior, app behavior, security properties or cloud independence.
