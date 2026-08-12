# Smart-Glasses Model Profiles — Foundations and Early Platforms

These profiles continue the human-readable GlassesResearch catalog. Each paragraph explains what the device really is, why it matters, and the tradeoff that matters most. Structured specifications and Report Cards remain supporting evidence rather than the main reading experience.

## GLS-0009 — Amazon Echo Frames (1st Gen)

The original Echo Frames were Amazon's first serious attempt to make Alexa disappear into ordinary prescription-ready eyewear. Introduced through the 2019 Day 1 Editions program, they deliberately omitted both camera and display and instead used open-ear audio, microphones, touch controls and phone connectivity to make Alexa available without pulling out a handset. That restraint is what made them interesting: **the product treated smart glasses as ambient voice access rather than a miniature headset**. The first generation was also explicitly experimental—invite-only, Android-only at launch, and shaped by customer feedback—so its historical importance is less about raw capability than proving that a mainstream company could put an assistant into glasses while keeping the visual design close to normal eyewear.

Source: [Amazon — Echo Frames Day 1 Edition](https://press.aboutamazon.com/2019/9/amazon-introduces-8-new-echo-devices)

## GLS-0010 — Amazon Echo Frames (2nd Gen)

Second-generation Echo Frames show what happens when an experiment becomes a consumer product. Amazon kept the same basic no-camera, no-display philosophy but improved battery life, materials, splash resistance, color choices and everyday usability, while expanding support beyond the initial invite-only launch. The result was less technologically dramatic than many AR glasses but arguably more realistic about what people would actually wear: **open-ear audio and Alexa were added without turning the frame into visible computing equipment**. Their main limitation is architectural rather than physical—the intelligence remains tied to Alexa and the paired-phone ecosystem, with little owner programmability—but as wearable design they helped establish that subtlety can be a feature in its own right.

Source: [Amazon — Echo Frames available to everyone](https://www.aboutamazon.com/news/devices/echo-frames-are-now-available-to-everyone)

## GLS-0011 — Amazon Echo Frames (3rd Gen)

The 2023 Echo Frames generation is Amazon's clearest attempt to make smart audio glasses feel like ordinary eyewear first and electronics second. Amazon slimmed the temples, expanded style and lens choices, redesigned the open-ear audio system, improved speech recognition in noisy environments, added multipoint pairing and pushed battery life to roughly six hours of continuous media or calls. There is still no camera or HUD, which keeps the glasses socially simple but also limits them to **audio, notifications and Alexa-mediated intelligence rather than visual computing**. Their strongest lesson is that mature smart glasses do not necessarily need more sensors; sometimes the meaningful progress is better fit, better sound, longer endurance and less visible technology.

Source: [Amazon — next-generation Echo Frames](https://press.aboutamazon.com/2023/9/amazon-unveils-next-generation-echo-show-8-all-new-echo-hub-and-new-echo-frames)

## GLS-0012 — Carrera Smart Glasses with Alexa

Carrera Smart Glasses take the third-generation Echo Frames electronics and package them through an established fashion-eyewear brand. That collaboration matters because it shifts part of the design authority away from a technology company and toward a company whose core product is already something people choose to wear on their face. The glasses offer the same Alexa-first, open-ear, no-camera and no-display model as Echo Frames, but the Carrera Cruiser and Sprinter styles make **brand identity and normal eyewear aesthetics part of the computing platform**. Technically they remain closed consumer accessories rather than developer hardware, but culturally they are evidence that smart-glasses adoption may depend as much on eyewear design and retail familiarity as on AI capability.

Source: [Amazon — Carrera Smart Glasses with Alexa](https://www.aboutamazon.com/news/devices/introducing-next-generation-echo-frames-carrera-smart-glasses-with-alexa)

## GLS-0043 — Google Glass Explorer Edition

Google Glass Explorer Edition is the model that made modern smart glasses culturally unavoidable. Its monocular display, camera, microphone, touchpad and Android-based software created a real wearable-computing platform years before today's AI-glasses boom, and Google exposed a Glass Developer Kit so software could run directly on the device. That openness to application development made Glass far more than a camera accessory, but its social footprint became equally important: the visible hardware and always-available camera triggered privacy backlash and taught the entire industry that **technical possibility and social acceptability are separate engineering problems**. Explorer Edition's greatest legacy may therefore be both positive and cautionary—it proved the category could exist and demonstrated exactly how quickly public trust can become part of the product specification.

Source: [Google for Developers — Glass Explorer Edition](https://developers.google.com/glass)

## GLS-0044 — Google Glass Enterprise Edition

Glass Enterprise Edition was Google's answer to the lesson that a wearable computer does not need to win over everyone if it solves a valuable job extremely well. The enterprise version shifted the product away from consumer lifestyle ambitions and toward hands-free work, where glanceable instructions, camera capture, voice interaction and purpose-built applications could justify the visible hardware. In that environment, Glass's weaknesses as fashion eyewear became less important than **repeatable workflow, safety, training and access to information without occupying the user's hands**. The move also established a pattern still visible across Vuzix and other industrial devices: enterprise smart glasses often become more useful when they stop trying to look invisible and instead optimize for the task.

Source: [Google for Developers — Glass Enterprise Edition](https://developers.google.com/glass/distribute/glass-enterprise)

## GLS-0045 — Google Glass Enterprise Edition 2

Glass Enterprise Edition 2 is one of the strongest historical examples of owner-programmable smart glasses because Google treated it as a real Android computer rather than a sealed accessory. It runs AOSP-based Android Oreo 8.1, supports standard Android APIs, APK installation over ADB, fastboot access, system images and developer samples for camera, voice, gestures, QR scanning and WebRTC. It lacks Google Mobile Services, which is a constraint for some applications but also reinforces how directly developers can interact with the underlying platform. Google ended sales in March 2023 and support in September 2023, yet existing devices and software remain usable. That makes EE2 a useful benchmark for **what smart-glasses ownership looks like when the vendor provides ordinary development tools instead of forcing all capability through a companion app or cloud assistant**.

Sources: [Google — Glass EE2 developer guide](https://developers.google.com/glass-enterprise/guides/get-started), [Google — Glass Enterprise Edition announcement FAQ](https://support.google.com/glass-enterprise/customer/answer/13417888)

## GLS-0050 — Brilliant Labs Monocle

Brilliant Labs Monocle is not the most wearable device in the catalog, but it is currently one of the clearest examples of what true owner control looks like. The tiny clip-on module combines a 640×400 color OLED, 5 MP camera, microphone, touch input, Bluetooth and FPGA acceleration with MicroPython, custom firmware support, custom FPGA images, published schematics, mechanical files and documented SWD/JTAG access. That combination is why its Report Card sets the present **10/10 benchmark for Openness and Hackability**: the owner is not merely given an SDK, but meaningful access to the software, hardware design and low-level programming path. The tradeoff is equally clear. Monocle is asymmetrical, visibly technical and constrained by a very small battery, so it is a poor model for invisible everyday eyewear. But as a research and development platform, it asks a more important question than most polished consumer products: **what can smart glasses become when the person who buys the hardware is actually allowed to own the machine?**

Sources: [Brilliant Labs — Monocle documentation](https://docs.brilliant.xyz/monocle/monocle/), [Brilliant Labs — Monocle hardware](https://docs.brilliant.xyz/monocle/hardware/), [GlassesResearch Report Card Batch 01](../docs/report-cards/BATCH_01.md)
