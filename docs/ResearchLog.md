# Research Log

This is the chronological engineering notebook for GlassesResearch. Add one dated entry per work session so observations, experiments, evidence, and unanswered questions remain connected.

## Entry format

```markdown
## YYYY-MM-DD — Short session title

### Objective
What was being investigated?

### Device and environment
- Device or retail variant:
- Phone/computer:
- Operating system:
- App or tool versions:
- Relevant settings:

### Observations
- Directly observed fact
- Directly observed fact

### Experiments
1. Procedure
2. Result
3. Reproduction notes

### Evidence added
- `images/YYYY-MM-DD-topic/filename.jpg` — what it shows

### Interpretation
Clearly label analysis or inference that goes beyond direct observation.

### Open questions
- Question requiring further investigation

### Next actions
- Specific follow-up task
```

## 2026-08-03 — Initial W610 receipt and baseline inspection

### Objective
Preserve the initial purchase context and begin a baseline record of the received W610-family smart glasses before modification.

### Device and environment
- Retail listing name: **W610 Smart AI Glasses with Camera and Translation**
- Marketplace: Amazon
- Observed listing price: **$48.99**
- Bluetooth device name observed during setup: **HeyCyan Glasses**

### Observations
- The right arm houses the primary electronics.
- Two physical buttons are present on the right arm.
- An indicator LED is located near the hinge.
- A power-button press produces a tone and a brief LED indication.
- The included printed instructions contain only a small amount of English-language material.

### Evidence planned
The initial evidence set should include:

- Amazon listing image
- Packaging exterior and labels
- Glasses front view
- Left-arm exterior
- Right-arm exterior
- Buttons and indicator LED
- Charging connector and supplied cable
- Lens and frame details
- Manual pages and QR codes

See [`../images/2026-08-03-unboxing/README.md`](../images/2026-08-03-unboxing/README.md) for the evidence catalog.

### Interpretation
The device appears to belong to the HeyCyan W610/W6xx ecosystem, but model-family relationships and internal hardware should remain labeled as provisional until independently verified.

### Open questions
- Which BLE services and characteristics are exposed?
- How does the device transfer photos, audio, and other data?
- Is Wi-Fi used directly by the glasses, through the phone, or only as marketing language?
- What firmware version is installed?
- How are firmware updates delivered and authenticated?
- Which camera and system-on-chip components are present?

### Next actions
- Add the original photos to the dated evidence folder.
- Record complete Bluetooth discovery results.
- Preserve the manual and QR-code destinations.
- Establish a repeatable power, pairing, and charging baseline.
