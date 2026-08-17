# HeyCyan Lineage — Populated Research Fields

This is the first lineage-level population pass using the research frameworks now established across GlassesResearch. It separates lineage-wide facts from W610-specific facts and keeps Anko claims narrower where evidence is weaker.

## Lineage identity

**Confirmed commonality:** HeyCyan software ecosystem.  
**Confirmed canonical members:** W610 (GLS-0039) and Anko Camera Glasses (GLS-0120).  
**Verified W610 market identities:** BooaBei, Zbna W610, Mingtawn W610, ESTG W610; STARK Horizon is a strong W610 market-identity match because STARK itself calls the underlying glasses `STARK W610`.  
**Documented HeyCyan sibling platforms:** W611 Pro, W620, W630, W640, W650 and additional supplier-side W/N-series products. These are not automatically W610 rebrands merely because they share software or some silicon.

Evidence now shows that the low-cost HeyCyan market contains both **true retail rebrands of a common platform** and **distinct sibling platforms that reuse software, silicon families, or naming conventions**. GlassesResearch therefore treats market identity, canonical model identity, software lineage, and OEM/manufacturer identity as separate layers.

## Market identity resolution

A visitor may know only the seller name printed on a box or marketplace order. Verified aliases should therefore remain searchable even when they do not add another canonical model count.

| Market identity | Resolution | Count behavior |
|---|---|---|
| BooaBei | W610 / HeyCyan lineage | Does not add a model; routes to GLS-0039 research. |
| Zbna W610 | W610 / HeyCyan lineage | Does not add a model; routes to GLS-0039 research. |
| Mingtawn W610 | W610 / HeyCyan lineage | Does not add a model; routes to GLS-0039 research. |
| ESTG W610 | W610 / HeyCyan lineage | Does not add a model; routes to GLS-0039 research. |
| STARK Horizon | Strong W610 market identity | Does not add a model while the W610 identity remains the best-supported underlying platform; seller-specific differences are preserved. |

The reusable alias map lives in `data/lineage-aliases.json`. Search surfaces should accept the market name a purchaser actually knows, explain the mapping, and then lead to the canonical model and lineage evidence.

## HeyCyan sibling platforms are not aliases by default

Supplier and manufacturer pages independently document W611 Pro, W620, W630, W640 and W650 as named products. Shared HeyCyan software and even shared JL7018F/V821-family silicon do **not** prove that these are W610 aliases. For example, W640 is documented with a 290 mAh battery, IP66 rating and sport frame, while W650 is documented with a 220 mAh battery and different chassis/power characteristics. These require their own admission/lineage decisions rather than being collapsed into GLS-0039.

This distinction prevents both errors:

1. **over-counting** a seller rename such as BooaBei as a new model; and
2. **under-counting** a materially distinct sibling platform merely because it also uses HeyCyan.

## Connectivity

### W610

- Bluetooth identity `HeyCyan Glasses` has been observed directly by GlassesResearch.
- Public community SDK work documents Bluetooth/BLE interaction for HeyCyan-compatible glasses (EV-0001).
- CyanBridge provides an independent Android companion stack for HeyCyan-compatible hardware (EV-0002, EV-0003).
- Community SDK history documents Bluetooth-to-Wi-Fi media-transfer work, supporting a two-stage connectivity model for at least some compatible devices.

**Confidence:** confirmed for Bluetooth presence and observed identity; strong for community-demonstrated BLE/software interaction; exact service/characteristic coverage remains device/version scoped.

### Anko Camera Glasses

- Contemporary retail reporting identifies HeyCyan as the software platform and describes photo/video transfer and connected audio/assistant functions.
- Direct protocol equivalence with W610 has not yet been demonstrated.

**Confidence:** confirmed ecosystem relationship; protocol-level compatibility provisional.

## Sensing and capture

### W610

- Camera-equipped smart-glasses platform.
- Supplier documentation for W610 describes an 8 MP camera (EV-0008).
- Regulatory records provide device-identity and hardware evidence useful for deeper component confirmation (EV-0006, EV-0007).
- Microphone/audio capability is supported by community SDK functionality and product behavior, but exact microphone count and sensor inventory should remain field-specific until tied to stronger documentation.

### Anko Camera Glasses

- Still-image and HD-video capture documented by contemporary retail reporting.
- Audio/call functions documented through the HeyCyan software environment.
- No claim is made yet for exact camera sensor, IMU, microphone count, or other internal sensors.

## AI capability

### W610 / HeyCyan-compatible ecosystem

- Community software demonstrates third-party assistant integration and local/alternative companion work (EV-0002 through EV-0005).
- This establishes that the ecosystem can support owner-selected assistant pathways through independent companion software.
- It does **not** establish that all inference runs on the glasses; current evidence points to the glasses functioning primarily as capture/audio interface with companion-device and/or service-side processing.

### Anko Camera Glasses

- Retail reporting describes an AI-assistant function through HeyCyan.
- Exact model provider, endpoint control, local processing, and third-party assistant compatibility have not yet been verified on the Anko hardware.

## Owner control and openness

### W610

The W610 currently has unusually strong owner-control evidence for a low-cost consumer platform:

- public community SDK (EV-0001);
- independent companion application and SDK (EV-0002);
- versioned alternative-app releases (EV-0003);
- documented third-party assistant integrations in community releases/discussions (EV-0004, EV-0005);
- BLE interaction outside the vendor application;
- GlassesResearch hands-on work began without installing the vendor application.

This supports strong Openness, Owner Control, and Hackability relative to closed consumer smart-glasses platforms. It does not imply open firmware or a known-unlocked boot chain.

### Anko Camera Glasses

The software-platform relationship makes the same community ecosystem relevant, but direct compatibility with independent tooling should remain **provisional** until tested on the retail unit.

## Cloud and service dependence

### W610

- Basic device startup and Bluetooth discovery have been observed without relying on the vendor application.
- Independent companion software materially reduces dependence on the original vendor app.
- Community projects demonstrate alternative assistant and media workflows.
- Exact offline boundaries for capture, transfer, calls, AI queries, configuration, and firmware remain to be normalized through the service-dependence test framework.

**Current interpretation:** the hardware is not wholly vendor-cloud dependent, but individual AI and transfer functions may require a host device, network connection, or external service.

### Anko Camera Glasses

Cloud/service survival has not yet been hands-on verified. The HeyCyan ecosystem suggests possible alternative-companion paths, but this is not yet established for the Anko device.

## Manufacturer and OEM relationships

### W610

- FCC records identify W610-linked regulatory evidence (EV-0006).
- A SANVNET regulatory manual references W610 (EV-0007).
- Goodway publishes a W610 specification/customization page (EV-0008).
- Current retail/manual evidence also exposes multiple branded W610 market identities, including Zbna, Mingtawn and ESTG.

These are meaningful supply-chain clues but do not justify collapsing Goodway, SANVNET, every W610 seller, and HeyCyan into one manufacturer identity. Brand, software platform, applicant, supplier, ODM and retail-market identity remain distinct until directly evidenced.

### Anko Camera Glasses

- Retail brand: Anko / Kmart Australia.
- Software platform: HeyCyan.
- Underlying ODM/manufacturer: not yet established.

## Silicon genealogy

No lineage-wide chipset claim is promoted. W610 and W640 supplier documentation both expose JL7018F + Allwinner V821-family architecture, but shared silicon does not establish product identity. W650 documentation materially differs in battery and chassis details even while remaining in the HeyCyan ecosystem.

## Prescription and optical serviceability

### W610

EV-0008's Goodway W610 page claims removable lenses and customizable prescription options under B2B OEM/ODM customization. The project-owned specimen supplies a concrete hands-on test surface, but its exact retention method, lens geometry, correction range and compatibility with the advertised configuration have not yet been documented. No source currently establishes replacement parts, an authorized optical channel, or acceptance by an ordinary independent optician.

**State:** prescription-compatible supplier claim; ordinary optical service unverified. See [EV-0068](../evidence/EV-0068-W610-optical-serviceability-boundary.md).

### Anko Camera Glasses

No adequate evidence currently establishes direct prescription glazing, inserts, supported range, or independent optical serviceability.

**State:** unknown.

## Battery normalization

Battery claims should not be compared until workload is explicit. EV-0008 provides supplier-side W610 battery information, but normalized GlassesResearch measurements are still needed for idle-connected, audio, capture, transfer, AI-query, and mixed use.

**State:** manufacturer/supplier claims available; normalized hands-on result pending.

## Failure, aging, and serviceability

No credible failure-rate estimate exists for the lineage. Future population should separate:

- hinge/mechanical aging;
- battery degradation;
- charging/contact failures;
- camera/microphone/control failures;
- application/account/service abandonment;
- firmware/update breakage;
- independent repair or donor-part compatibility.

Anecdotal reports must retain sample scope and must not be converted into percentages without a credible denominator.

## Regional/version variance

W610 appears through marketplace/OEM channels and may exist in multiple branded or customized variants. Anko represents a distinct Australian retail route. Findings must therefore preserve exact model, seller/brand, region, firmware, and date where material. W610 evidence should not be copied automatically onto Anko merely because both use HeyCyan.

## Report-card implications

### W610

- **Openness:** supported strongly by public community tooling and documented BLE work.
- **Owner Control:** supported strongly by independent companion software and third-party assistant paths.
- **Cloud Independence:** meaningful partial independence is evidenced, but function-by-function testing remains incomplete.
- **Hackability:** strong relative position because working public tooling exists; firmware-level openness remains unresolved.
- **Visual AI:** capability exists through the ecosystem, but processing location and exact feature set must remain version/service specific.

### Anko Camera Glasses

The HeyCyan relationship makes Anko a high-priority test target because a mass-market $89 AUD retail device may inherit unusually strong community-development potential. Until tested, however, W610 report-card scores must not simply be copied to Anko.

## Next evidence actions

1. Expand the market-identity resolver as additional verified seller names are discovered.
2. Reconcile W611 Pro, W620, W630, W640 and W650 against the canonical ledger as distinct candidate platforms rather than W610 aliases.
3. Mine supplier documentation into exact silicon and power fields without treating shared parts as identity proof.
4. Convert the existing W610 hands-on observations into dated GlassesResearch-verified evidence records.
5. Run the normalized offline/service-dependence and battery tests on W610.
6. Execute the EV-0068 specimen measurement, lens-tracing and independent-optician closure protocol.
7. Test CyanBridge/community-SDK compatibility on Anko when hardware becomes available.
