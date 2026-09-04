# GREP-42 — NDI / Controlled Inspection

Status: design specification
Purpose: produce a defensible Report Card from non-destructive or limited-access examination while making untested areas obvious.

## Form header

Record form revision; specimen ID; canonical GLS ID if known; maker/brand/model/claimed model number; acquisition source and status (owned/borrowed/return-window/sample); date/time; examiner; package condition; firmware/app version only if observed without exceeding test scope; and permitted test boundary.

Before testing, mark capability modules present/claimed/unknown: camera, display, audio, microphone, Bluetooth, Wi-Fi, USB data, onboard storage, sensors, prescription accommodation, standalone compute, other.

## Section 42-A — Identity and provenance (`ID`)

- `ID-01` Exact visible brand/model markings — OBSERVED / NONE; transcription + photo ID.
- `ID-02` Packaging model/SKU/serial/regulatory identifiers — OBSERVED / NONE.
- `ID-03` Device/packaging identity agreement — PASS / FAIL / UNKNOWN.
- `ID-04` Claimed manufacturer/OEM identity — source lane + evidence ID; no inference promoted as fact.
- `ID-05` Acquisition route and price paid/observed.
- `ID-06` Included accessories and documentation.
- `ID-07` Prior-use/condition indicators.

Report Card relevance: Hardware, Value, provenance confidence; establishes which physical specimen was actually tested.

## Section 42-B — Physical metrology (`HW`)

Use calibrated/identified instruments where practical and record instrument ID.

- `HW-01` Mass, glasses only (g).
- `HW-02` Overall width (mm).
- `HW-03` Overall depth/temple length (mm).
- `HW-04` Overall folded dimensions (mm).
- `HW-05` Lens width/height and bridge width (mm), where meaningful.
- `HW-06` Left/right temple maximum thickness (mm).
- `HW-07` Visible camera/sensor apertures and positions.
- `HW-08` Buttons/touch surfaces/switches: count, location, tactile behavior.
- `HW-09` Charging/data connector type and location.
- `HW-10` Hinges, adjustment points, removable components.
- `HW-11` Construction/material observations; claims remain claims unless established.
- `HW-12` Visible status/recording indicators and their positions.

Report Card relevance: Hardware, Wearability, Serviceability.

## Section 42-C — Power and charging (`PW`)

- `PW-01` Device arrives powered/off/depleted — OBSERVED.
- `PW-02` Charging method physically verified.
- `PW-03` USB/charger negotiation observed where permitted.
- `PW-04` Charge indicator behavior.
- `PW-05` Time from observed starting state to indicated full, if tested.
- `PW-06` Battery capacity: MEASURED / PRIMARY CLAIM / COMMERCIAL CLAIM / UNKNOWN; never conflate.
- `PW-07` Operates while charging — PASS / FAIL / NOT TESTED.
- `PW-08` Abnormal heat, odor, swelling, charging interruption — OBSERVED / NONE OBSERVED.

Report Card relevance: Hardware, Wearability, Value. NDI runtime is optional; absence stays NOT TESTED.

## Section 42-D — Interfaces and passive discovery (`IF`)

- `IF-01` USB enumeration without vendor software; record VID/PID, descriptors/classes if exposed.
- `IF-02` USB storage/media exposure.
- `IF-03` Bluetooth advertising name/address type and observable services within approved passive scope.
- `IF-04` Wi-Fi emissions/SSID behavior observed without forcing vendor-app setup.
- `IF-05` NFC/other radio evidence if observable.
- `IF-06` Physical data path distinguishable from charge-only — PASS / FAIL / UNKNOWN.
- `IF-07` Radio/interface behavior before and after user control actions, if tested.

Report Card relevance: Hardware, Openness, Owner Control, Cloud Independence, Hackability.

## Section 42-E — Basic functionality (`FN`)

For every claimed major function, record one of PASS / FAIL / NOT TESTED / BLOCKED / N/A and the test method. The form must include blank rows so unexpected functions are not lost.

Core rows when applicable: power on/off; pairing; controls; camera still; video; microphone; speakers; calls; local media retrieval; display activation; touch/gesture; wear detection; translation; assistant invocation; notifications.

A PASS means only that the defined test passed under recorded conditions, not that the feature is good.

## Section 42-F — Capability modules

### Camera / visual AI (`VA`)
Record advertised and observed camera count; maximum mode actually tested; capture initiation path; file retrieval path; visible recording indication; close-text legibility sample; normal-room sample; outdoor sample if permitted. Do not score image quality from one uncontrolled sample.

### Display / optics (`DP`)
Record monocular/binocular; display active/passive; prescription configuration; basic content visibility; whether display function was exercised; obvious artifacts; and why deeper optical tests were not performed under NDI where applicable.

### Audio (`AU`)
Record channel configuration observed; playback/call function tested; microphone function; obvious leakage observation under stated conditions. Formal acoustic characterization is outside baseline GREP-42 unless explicitly authorized.

## Section 42-G — Software boundary (`SW/OC/CI`)

- Was vendor software installed? YES / NO.
- Was account creation required for any tested function? YES / NO / UNKNOWN / NOT TESTED.
- Could any media/data be retrieved without vendor software?
- Could core hardware functions be invoked without cloud connectivity?
- Were permissions/network behaviors examined? If not, NOT TESTED.

This section is intentionally conservative. Do not install software merely to fill blanks if NDI scope excludes it.

## Section 42-H — Wear/fit snapshot (`WR`)

Short-duration only. Record evaluator correction configuration; prescription insert/lens state; PD/IPD if known and relevant; initial fit; temple/nose pressure observations; immediate slippage; gross balance; obstruction of peripheral vision; and maximum continuous wear duration actually observed. Do not infer all-day comfort.

## Section 42-I — Serviceability and acquisition (`SV/VL`)

Record replaceable/removable parts visible without disassembly; proprietary charging dependency; apparent lens replaceability; documentation/support availability observed; current acquisition route; tested unit price; included accessories. Do not infer repairability from screws alone.

## Section 42-J — Completion and handoff

Record tests applicable, completed, not tested, blocked, N/A; evidence artifacts count; unresolved identity questions; anomalies; damage/change to specimen (baseline expectation: none); and examiner sign/date.

The handoff explicitly identifies which Report Card categories have hands-on support and which remain documentation-only or unknown. GREP-42 may support a complete published Report Card, but its coverage disclosure must make clear that NDI limitations remain.