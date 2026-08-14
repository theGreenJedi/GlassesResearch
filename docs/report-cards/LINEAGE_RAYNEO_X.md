# RayNeo X lineage — evidence and Report Cards

This packet begins the lineage with the first generation for which the repository now has a complete primary-source grading basis. X2 and X3 Pro remain separate hardware generations; no specification or score is inherited across them.

## GLS-0065 — RayNeo X2

**Evidence lane:** vendor-primary documentation. No GlassesResearch hands-on claims are made.

RayNeo documents X2 as a self-contained Android-class AR computer: Snapdragon XR2, 6 GB RAM, 128 GB storage, a 590 mAh battery, binocular full-color MicroLED waveguides, a 16 MP camera, three microphones, onboard sensors, Wi-Fi, Bluetooth and GPS. It supports prescription fitting and combines visual navigation, translation, capture, notifications and voice interaction in an untethered frame.

The ownership story is unusually consequential. RayNeo officially documents ADB installation of third-party APKs, the setting required to re-enable installs on newer firmware, `scrcpy` mirroring, microphone-routing parameters and developer thermal guidance. That does not make X2 open firmware, but it does make it substantially more owner-programmable than a companion-app-only consumer product. Some headline AI functions still depend on Microsoft Azure and GPT-4 with Vision, so cloud independence does not equal its strong local-application control.

| Dimension | Score | Judgment |
|---|---:|---|
| Hardware | 8.5 | Standalone XR2 compute, 6/128 GB memory, camera, sensors, audio, wireless connectivity and binocular MicroLED optics form a broad first-generation AR package. |
| Wearability | 6.5 | It is untethered and prescription-adaptable, but its standalone compute, battery and optical system make it substantially less ordinary than everyday eyewear. |
| Visual AI | 7.5 | The 16 MP first-person camera supports environment recognition and cloud-assisted visual workflows, though the AI stack is less mature and owner-substitutable than current leaders. |
| Software | 7.5 | Navigation, translation, capture, notifications, assistant functions and Android application support create a capable platform with visible first-generation friction. |
| Display / HUD | 8.0 | Binocular full-color MicroLED waveguides and high-contrast see-through output provide genuine AR rather than a simple notification light. |
| Openness | 7.5 | A developer portal, documented APK deployment, ADB, microphone routing and debugging guidance expose a meaningful supported surface without opening firmware or hardware. |
| Owner Control | 8.0 | Owners can sideload Android applications and use standard debugging/mirroring tools instead of remaining confined to RayNeo's companion app. |
| Cloud Independence | 6.5 | Locally installed applications and device functions can survive independently, while headline translation and multimodal-assistant features use external services. |
| Hackability | 8.0 | Official ADB/APK instructions, `scrcpy` support and low-level audio parameters provide unusually concrete experimentation paths. |
| Value | Not yet graded | The documented $499 route is currently out of stock; a durable score requires a live acquisition comparison. |

Sources: [RayNeo X2 product page](https://www.rayneo.com/products/tcl-rayneo-x2), [RayNeo X2 FAQ and assisted development](https://www.rayneo.com/pages/faq-x2), [evidence packet](../../evidence/EV-0055-RayNeo-X2-primary-platform-surface.md).

