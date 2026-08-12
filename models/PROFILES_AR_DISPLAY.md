# Smart-Glasses Model Profiles — AR, Display, and Enterprise Platforms

These profiles continue the human-readable GlassesResearch catalog. Each paragraph explains what the device really is, why it matters, and the tradeoff that matters most. Structured specifications and Report Cards remain supporting evidence rather than the main reading experience.

## GLS-0055 — Vuzix Blade 2

Vuzix Blade 2 is a useful reminder that **owner control often comes from ordinary computing architecture rather than exotic hardware**. It is a standalone Android wearable computer with a full-color monocular HUD, camera, microphones, speakers, Wi-Fi and Bluetooth, and Vuzix supports normal Android application development alongside its own SDKs. That gives Blade 2 strong Software, Openness, Owner Control, Cloud Independence and Hackability scores: developers can deploy real applications instead of merely scripting a vendor assistant. The compromise is physical and generational. The 480×480, 20° display is now modest beside newer binocular AR systems, and the glasses remain visibly technical rather than socially invisible. Blade 2 therefore makes more sense as **a programmable computer you wear** than as fashionable consumer eyewear—and that distinction is precisely why it remains valuable to researchers and developers.

Sources: [Vuzix Blade 2 developer documentation](https://support.vuzix.com/docs/blade-2), [GlassesResearch — Blade 2](VuzixBlade2/README.md), [Report Card Batch 01](../docs/report-cards/BATCH_01.md)

## GLS-0056 — Vuzix Z100

The Z100 is almost the architectural inverse of Blade 2. Rather than running a full operating system on the glasses, Vuzix treats it as a lightweight **BLE-connected display peripheral**: the phone or nearby computer performs the application logic while the glasses handle a 640×480 green MicroLED HUD, taps, status and display output. At roughly 38 g with prescription support and multi-day claimed battery life, that separation produces unusually wearable display glasses without forcing compute, heat and battery burden into the frame. More importantly, Vuzix publishes Android and iOS SDKs that let developers send their own text, graphics and application state to the display. The result is one of the strongest examples of **smart glasses as an owner-selectable front end rather than a sealed AI appliance**.

Sources: [Vuzix Z100](https://www.vuzix.com/products/z100-smart-glasses), [GlassesResearch — Z100](VuzixZ100/README.md)

## GLS-0064 — Rokid Glasses

Rokid Glasses are one of the more convincing attempts to combine a genuinely wearable frame with a broad AI-and-HUD feature set. At about 49 g, they integrate dual-eye MicroLED waveguides, a 12 MP first-person camera, four microphones, open-ear speakers, Snapdragon AR1-class compute, Wi-Fi, Bluetooth and local storage. That hardware earns strong marks for Hardware, Wearability, Visual AI and Display/HUD: these are glasses that can actually see, listen and put useful information in front of both eyes without becoming a bulky headset. The tradeoff appears lower in the stack. Rokid exposes a meaningful developer ecosystem, but owner control, cloud independence and hackability remain well below open-hardware benchmarks because many headline AI functions still live inside Rokid's software and connected-service world. **Rokid gets remarkably close to the consumer ideal on the face; it is less independent underneath it.**

Sources: [Rokid Glasses](https://global.rokid.com/products/rokid-glasses), [GlassesResearch — Rokid Glasses](RokidGlasses/README.md), [Report Card Batch 02](../docs/report-cards/BATCH_02.md)

## GLS-0066 — RayNeo X3 Pro

RayNeo X3 Pro pushes harder toward true binocular AR than most glasses-shaped devices in the catalog. Its full-color MicroLED waveguides, Snapdragon AR1 platform, 12 MP imaging, spatial camera, 4 GB RAM and 32 GB storage produce one of our strongest current Hardware, Visual AI and Display/HUD report cards. In practical terms, this is closer to **a compact spatial computer** than an audio accessory with a camera: navigation, translation, Gemini-powered assistance and a spatial interface are central to the product. RayNeo also provides Creator Mode, so the glasses are not completely sealed to outside experimentation. But capability has a cost. At roughly 76 g they are much harder to forget than ordinary eyewear, and the flagship AI experience remains materially cloud-dependent. X3 Pro therefore illustrates the present frontier clearly: **we can now put an impressive amount of AR computer on the face, but weight, platform control and cloud reliance still determine whether that computer truly feels like glasses.**

Sources: [RayNeo X3 Pro](https://www.rayneo.com/collections/ai-smart-glasses/products/x3-pro-ai-display-glasses), [GlassesResearch — X3 Pro](RayNeoX3Pro/README.md), [Report Card Batch 02](../docs/report-cards/BATCH_02.md)

## GLS-0068 — Snap Spectacles (5th Gen, 2024)

Fifth-generation Spectacles are among the most capable AR development glasses in the catalog—and among the least convincing as ordinary eyewear. The report card makes that split unusually clear: Hardware, Visual AI, Software and Display/HUD all score 9/10 thanks to stereo see-through displays, multiple color and infrared cameras, 6DoF tracking, hand tracking, microphones, dual Snapdragon compute and Snap's mature Lens Studio/Snap OS development stack. Yet Wearability falls to 4.5/10 because roughly 226 g of hardware and about 45 minutes of continuous runtime make them a developer computer worn on the face, not something most people would choose for an ordinary day. Their significance is therefore not consumer polish but **how much spatial-computing capability Snap exposes to developers**. Spectacles 5 are a laboratory for the future of interaction—and a vivid demonstration that technical capability can outrun the physical limits of glasses.

Sources: [Snap Spectacles developer portal](https://developers.snap.com/spectacles/home), [GlassesResearch — Spectacles 5](SnapSpectacles5/README.md), [Report Card Batch 01](../docs/report-cards/BATCH_01.md)

## GLS-0074 — XREAL One

XREAL One is best understood as **a private spatial monitor worn on your face**, not as autonomous AI glasses. It receives DisplayPort video and power from a connected USB-C host, while its own X1 processor stabilizes and manages spatial display modes. The optical hardware is the star: dual 1080p Micro-OLED panels, up to 120 Hz refresh, roughly 50° field of view, electrochromic dimming and open-ear audio. Because the source computer can be a phone, laptop or other compatible device, the owner has broad freedom over what software and content drive the glasses, and the core experience does not inherently require cloud services. The tradeoff is tethering: **excellent visual output and unusually strong host freedom, but very little independence from the device connected by cable**.

Sources: [XREAL One specifications](https://tutorials.xreal.com/docs/glasses/one-series/spec/), [GlassesResearch — XREAL One](XREALOne/README.md)

## GLS-0098 — Vuzix M400

Vuzix M400 is what smart glasses look like when **operational control matters more than looking like glasses**. It is a rugged standalone Android wearable computer with camera, sensors and connectivity, and Vuzix explicitly supports standard Android development for camera, Bluetooth/BLE, databases and other system functions alongside device-specific SDKs. That architecture earns the M400 9/10 scores for Software, Owner Control and Cloud Independence: organizations can deploy their own applications and workflows locally rather than funneling every task through a companion app or vendor AI service. Its weak point is Wearability, not programmability. The M400 is a visible, task-oriented industrial device meant for shifts, inspections and hands-free work rather than social invisibility. In a consumer-heavy catalog, it is a useful corrective: **sometimes the best smart glasses are the ones that surrender fashion in order to give the operator reliable control.**

Sources: [Vuzix Developer Resources](https://support.vuzix.com/docs/developer-resources), [GlassesResearch — M400/M4000](VuzixM400/README.md), [Report Card Batch 02](../docs/report-cards/BATCH_02.md)

## GLS-0099 — Vuzix M4000

M4000 carries the same owner-friendly Android philosophy as the M400 but strengthens the visual side of the enterprise equation. It remains a self-contained wearable computer with standard Android APIs, Vuzix SDKs, Bluetooth/BLE and local application deployment, which is why its Software, Owner Control and Cloud Independence scores all reach 9/10. The M4000's optics make the HUD proposition somewhat stronger than the M400, but it still lives firmly in the industrial world: this is monocular, task-centric hardware designed to put instructions and information into a worker's field of view, not to disappear into a dinner-table conversation. Its value is architectural. **The M4000 shows that a manufacturer can build a tightly integrated wearable while still letting organizations own the software workflow running on it.** That makes it more open in practice than many prettier consumer glasses whose intelligence stops working the moment the vendor ecosystem is removed.

Sources: [Vuzix M400/M4000 technical details](https://support.vuzix.com/docs/m400-m4000-technical-details), [GlassesResearch — M400/M4000](VuzixM400/README.md), [Report Card Batch 02](../docs/report-cards/BATCH_02.md)
