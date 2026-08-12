# Lineage Research — DAQRI Professional AR

**Research date:** 2026-08-12

This packet follows the lineage-first protocol and treats DAQRI's professional augmented-reality hardware as a family before deciding which devices belong on which form-factor shelf. The evidence supports a clear relationship among the DAQRI Smart Helmet, DAQRI Smart Glasses, and DAQRI Smart HUD ecosystem, but they should not be collapsed into one model type.

## Family boundary

### DAQRI Smart Helmet — adjacent head-worn industrial AR

The Smart Helmet predates the Smart Glasses and represents DAQRI's earlier industrial wearable-computing platform. DAQRI described it as a production-ready industrial AR helmet rather than a concept. First-party material documents a 6th-generation Intel Core m7-6Y75 processor, Intel RealSense depth sensing, wide-angle tracking, RGB imaging, thermal imaging, Wi-Fi, integrated audio, see-through AR display, and an open API/developer-tool story.

It belongs in the broader wearable-HCI catalog under **head-worn industrial AR / smart helmet**, not in the canonical smart-glasses count.

### DAQRI Smart Glasses — admit to smart-glasses ledger

DAQRI announced the Smart Glasses at CES 2017 and began worldwide customer shipments on 2017-11-07. DAQRI's own shipment announcement states that the device was available for direct purchase through DAQRI and selected channel partners for **$4,995**.

The glasses used a 6th-generation Intel Core m7 processor and Intel RealSense LR200 depth camera, and DAQRI documented a 44-degree diagonal field of view, bright transparent stereoscopic displays, wide-angle tracking camera, HD color camera, Wi-Fi/Bluetooth connectivity, SLAM/sparse-mapping position tracking, and enterprise workflows including remote expert, guided work and 3D-content visualization.

The Smart Glasses were therefore a real commercial enterprise AR product rather than an announced prototype.

### DAQRI Smart HUD — adjacent vehicle/display platform

DAQRI also marketed Smart HUD as part of the same Visual Operating System ecosystem, but it is a vehicle/head-up-display technology rather than wearable eyewear. It should remain in the research registry or a future **vehicle/ambient display** shelf, not the smart-glasses ledger.

## Report cards

The same catalog-wide ruler is used where dimensions apply.

| Model | Form factor | Hardware | Wearability | Visual AI | Software | Openness | Owner Control | Cloud Independence | Hackability | Display/HUD | Value |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| DAQRI Smart Glasses | enterprise binocular AR glasses | 8.0 | 4.5 | 4.0 | 7.5 | 6.0 | 7.0 | 8.0 | 6.0 | 8.0 | 4.0 |
| DAQRI Smart Helmet | industrial AR helmet | 8.5 | 2.5 | 5.0 | 7.5 | 6.5 | 7.0 | 8.0 | 6.5 | 8.0 | 3.0 |

### DAQRI Smart Glasses rationale

- **Hardware 8.0:** strong standalone enterprise compute, stereo transparent display, depth sensing, tracking and multiple cameras made this one of the more capable enterprise AR systems of its generation; bulk and externalized power/compute ergonomics keep it below the modern ceiling.
- **Wearability 4.5:** much lighter and more practical than the Smart Helmet, but still a conspicuous professional headset rather than ordinary eyewear.
- **Visual AI 4.0:** depth, SLAM and computer-vision tracking materially understood the environment, but this predates modern multimodal visual assistants and does not justify a high current Visual-AI score.
- **Software 7.5:** DAQRI's Visual Operating System / Worksense ecosystem, remote expert, guided work, model visualization and developer tooling were substantial for enterprise AR.
- **Openness 6.0:** DAQRI promoted developer-friendly tools and APIs, but hardware, firmware and core platform remained proprietary and far below the Brilliant Labs 10-level benchmark.
- **Owner Control 7.0:** enterprise developers could build and integrate applications, but users were still operating inside DAQRI's proprietary platform stack.
- **Cloud Independence 8.0:** core local rendering, tracking and sensor operation were device-side; collaborative/remote workflows could rely on network services but basic AR did not inherently require a vendor cloud.
- **Hackability 6.0:** meaningful SDK/API access and PC-class compute create an experimentation surface, but closed firmware/hardware and the vendor's disappearance materially reduce practical hackability today.
- **Display/HUD 8.0:** 44-degree transparent stereoscopic AR and persistent spatial tracking were strong for the period, though far below current best-in-catalog optics.
- **Value 4.0:** $4,995 bought serious professional capability, but the acquisition cost was extremely high and the platform's later abandonment further weakens lifetime value.

### DAQRI Smart Helmet rationale

The helmet scores separately because its thermal camera, safety integration, larger industrial sensor package and hardened use case are real hardware strengths, while its size, mass and form factor impose a severe wearability penalty. It remains valuable lineage context but does not count as smart glasses.

## Evidence family

Primary / first-party or manufacturer-partner evidence used for this packet:

- DAQRI company account, **DAQRI SMART GLASSES SHIP TO CUSTOMERS**, 2017-11-07: https://medium.com/@DAQRI/daqri-smart-glasses-ship-to-customers-cd7dc4ea281b
- DAQRI company account, **Introducing DAQRI Smart Glasses**, 2017-10-12: https://medium.com/@DAQRI/introducing-daqri-smart-glasses-874c1581b422
- DAQRI company account, **DAQRI Smart Helmet: A Deep Dive**, 2016-12-15: https://medium.com/@DAQRI_Media/daqri-smart-helmet-a-deep-dive-b384f5997537
- Flex / DAQRI manufacturing announcement, 2017-06-27, confirming production of Smart Glasses and Intel Core m7 / RealSense LR200 platform: https://www.prnewswire.com/news-releases/daqri-partners-with-flex-for-production-of-augmented-reality-headsets-300480078.html
- DAQRI Worksense announcement, 2018, documenting the software suite and Smart Glasses subscription/package: https://medium.com/@DAQRI/announcing-daqri-worksense-the-productivity-suite-for-ar-5676d9dc8c10

## Lineage conclusion

The lineage-first pass reveals a useful form-factor split rather than three interchangeable DAQRI products:

**Smart Helmet** = adjacent industrial head-worn AR  
**Smart Glasses** = canonical smart-glasses product  
**Smart HUD** = non-wearable/vehicle display platform

This is exactly why the wearable-HCI taxonomy should sit above the individual model shelves: the same company and software platform can span multiple human-computer interface forms without corrupting the smart-glasses count.