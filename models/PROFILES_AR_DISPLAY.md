# Smart-Glasses Model Profiles — AR, Display, and Enterprise Platforms

These profiles continue the human-readable GlassesResearch catalog. Each paragraph explains what the device really is, why it matters, and the tradeoff that matters most. Structured specifications and Report Cards remain supporting evidence rather than the main reading experience.

## GLS-0055 — Vuzix Blade 2

Vuzix Blade 2 sits in a very different branch from phone-dependent display glasses: it is a **standalone Android wearable computer** with its own application runtime and a manufacturer-supported development stack. Vuzix maintains Android-oriented developer documentation, sample projects, speech and barcode SDKs, HUD resources, haptic APIs and device-interface guidance, which means the glasses can be treated as an application platform rather than merely a remote screen. That makes Blade 2 especially interesting for owner-control research, even though the hardware is visibly more technical and enterprise-oriented than consumer eyewear. Its central tradeoff is straightforward: **far more software agency than fashionable consumer glasses, but with a more conspicuous form factor and older-generation display hardware**.

Sources: [Vuzix Blade 2 developer documentation](https://support.vuzix.com/docs/blade-2), [GlassesResearch — Blade 2](VuzixBlade2/README.md)

## GLS-0056 — Vuzix Z100

The Z100 is almost the architectural inverse of Blade 2. Rather than running a full operating system on the glasses, Vuzix treats it as a lightweight **BLE-connected display peripheral**: the phone or nearby computer performs the application logic while the glasses handle a 640×480 green MicroLED HUD, taps, status and display output. At roughly 38 g with prescription support and multi-day claimed battery life, that separation produces unusually wearable display glasses without forcing compute, heat and battery burden into the frame. More importantly, Vuzix publishes Android and iOS SDKs that let developers send their own text, graphics and application state to the display. The result is one of the strongest examples of **smart glasses as an owner-selectable front end rather than a sealed AI appliance**.

Sources: [Vuzix Z100](https://www.vuzix.com/products/z100-smart-glasses), [GlassesResearch — Z100](VuzixZ100/README.md)

## GLS-0064 — Rokid Glasses

Rokid Glasses tries to combine ordinary-eyewear ambitions with a surprisingly complete computing stack. The approximately 49 g frame carries dual-eye MicroLED waveguides, a 12 MP camera, four microphones, open-ear speakers, Snapdragon AR1 plus RT600 compute, Wi-Fi, Bluetooth and 32 GB of storage. That lets Rokid offer visual AI, translation, captions, navigation prompts and teleprompter functions without turning the product into a large headset. The most interesting part for GlassesResearch is that Rokid also publishes a terminal/glasses SDK covering media capture, voice, recognition, messaging, device state and connectivity. So while the product still relies heavily on Rokid's companion software and services, it is not merely a black box: **there is a documented developer surface underneath the polished consumer experience**.

Sources: [Rokid Glasses](https://global.rokid.com/products/rokid-glasses), [GlassesResearch — Rokid Glasses](RokidGlasses/README.md)

## GLS-0066 — RayNeo X3 Pro

RayNeo X3 Pro is one of the more ambitious attempts to put real binocular AR and AI into something that still resembles glasses. Its full-color MicroLED waveguides, dual-camera system, Snapdragon AR1, 4 GB RAM, 32 GB storage, sensors and AIOS stack make it much closer to a compact standalone spatial computer than to audio-first smart eyewear. Gemini integration, translation, navigation and reminders give it a modern assistant layer, while RayNeo's Creator Mode and public code projects show at least some interest in outside development. The cost of that capability is visible in weight and complexity: at roughly 76 g, X3 Pro is less discreet than minimalist HUD glasses. It is therefore a useful benchmark for the question **how much computer can we put on the face before wearability begins to lose the argument?**

Sources: [RayNeo X3 Pro](https://uk.rayneo.com/products/x3-pro-ai-display-glasses), [GlassesResearch — X3 Pro](RayNeoX3Pro/README.md)

## GLS-0068 — Snap Spectacles (5th Gen, 2024)

Fifth-generation Spectacles are not really a conventional consumer product at all; they are **a wearable AR development platform distributed through Snap's developer program**. Snap exposes camera frames, hand and gesture input, world-query and spatial APIs, networking, controller integration and Spectacles-specific packages through Lens Studio, with public samples and compatibility documentation. That makes these glasses unusually valuable for understanding what an actual spatial-computing platform can expose when the manufacturer expects developers to build new experiences rather than merely consume a finished assistant. Their weakness is equally important: they remain specialized developer hardware rather than ordinary all-day eyewear. Spectacles 5 therefore excel as a laboratory for interaction and AR software, not as the answer to “what glasses should I wear every morning?”

Sources: [Snap Spectacles developer portal](https://developers.snap.com/spectacles/home), [GlassesResearch — Spectacles 5](SnapSpectacles5/README.md)

## GLS-0074 — XREAL One

XREAL One is best understood as **a private spatial monitor worn on your face**, not as autonomous AI glasses. It receives DisplayPort video and power from a connected USB-C host, while its own X1 processor stabilizes and manages spatial display modes. The optical hardware is the star: dual 1080p Micro-OLED panels, up to 120 Hz refresh, roughly 50° field of view, electrochromic dimming and open-ear audio. Because the source computer can be a phone, laptop or other compatible device, the owner has broad freedom over what software and content drive the glasses, and the core experience does not inherently require cloud services. The tradeoff is tethering: **excellent visual output and unusually strong host freedom, but very little independence from the device connected by cable**.

Sources: [XREAL One specifications](https://tutorials.xreal.com/docs/glasses/one-series/spec/), [GlassesResearch — XREAL One](XREALOne/README.md)

## GLS-0098 — Vuzix M400

Vuzix M400 is unapologetically an enterprise wearable computer. It runs applications directly on the glasses, uses standard Android development alongside Vuzix SDKs, and can be managed through Vuzix View for APK installation, display mirroring, screenshots and log retrieval. That makes it far less socially discreet than consumer smart glasses but much more intelligible to developers and IT teams: the architecture resembles a small Android computer attached to the eye rather than a cloud assistant trapped inside fashionable frames. For GlassesResearch, M400 is valuable precisely because it shows what **owner control and operational utility look like when fashion is not the primary design constraint**.

Sources: [Vuzix Developer Resources](https://support.vuzix.com/docs/developer-resources), [GlassesResearch — M400/M4000](VuzixM400/README.md)

## GLS-0099 — Vuzix M4000

M4000 shares the M400's standalone Android and developer architecture but pairs it with a different optical presentation aimed at hands-free enterprise work. Like its sibling, it supports direct application deployment, Wi-Fi and Bluetooth connectivity, standard Android tooling, Vuzix SDKs and Vuzix View debugging/management. The important point is not that M4000 looks like ordinary eyewear—it does not—but that it gives organizations and developers a **self-contained, programmable visual computer** rather than a peripheral dependent on a vendor's cloud assistant. In a catalog dominated by consumer AI glasses, M4000 is a reminder that industrial smart glasses often prioritize deterministic software control, field support and integration over discretion.

Sources: [Vuzix Connectivity SDK](https://github.com/Vuzix/connectivity-sdk), [GlassesResearch — M400/M4000](VuzixM400/README.md)
