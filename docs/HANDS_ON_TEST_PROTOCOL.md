# GlassesResearch Standard Hands-On Test Protocol

The report card is only as useful as the evidence beneath it. This protocol defines a repeatable baseline for hands-on smart-glasses testing so that results can be compared across models and generations.

The protocol is designed to separate **manufacturer claims**, **independent observations**, and **hands-on verified results**.

## 1. Identify the exact device

Record:

- retail brand and model name;
- model number and hardware revision where visible;
- region/carrier variant where relevant;
- firmware version;
- companion-app version;
- purchase source and date;
- included accessories;
- physical markings, regulatory identifiers, and pairing name;
- whether the sample appears to be retail, prototype, rebrand, or developer hardware.

Never generalize a result to an entire family unless the evidence supports that scope.

## 2. Physical inspection

Measure or record:

- total weight;
- frame width, bridge width, temple length, and approximate lens dimensions where practical;
- hinge construction;
- charging method;
- button and touch-control placement;
- camera, microphone, speaker, sensor, LED, and vent locations;
- visible asymmetry between temples;
- prescription-lens or insert path;
- apparent repair access such as screws, removable covers, replaceable temples, or modular parts.

Photograph the device from front, rear, top, bottom, both temples, hinges, charging interface, and any labels before disassembly or modification.

## 3. First-use and onboarding

Record the complete first-use path:

- whether the glasses power on without an app;
- Bluetooth advertising/pairing name;
- whether pairing works through ordinary OS Bluetooth settings;
- whether a vendor app is mandatory;
- account requirement;
- permissions requested;
- internet requirement;
- firmware update presented during setup;
- whether basic functions work before login or update.

This section directly informs Owner Control and Cloud Independence.

## 4. Offline behavior

With the device already set up, test normal user-visible behavior with internet access unavailable.

Record whether the device can still:

- boot;
- reconnect to the host;
- play or receive audio;
- take photos or video where applicable;
- access previously captured media;
- display local content where applicable;
- accept controls;
- use local transcription or AI features if advertised;
- retain settings.

Do not assume that a feature is local merely because it feels instantaneous.

## 5. Battery and charging

Record ambient conditions and starting firmware/app state. At minimum test:

- idle connected time;
- one hour of representative mixed use;
- sustained audio playback where relevant;
- repeated camera/AI interactions where relevant;
- HUD/display use where relevant;
- charging time from a documented low state to full;
- case or external battery contribution where included.

Report the workload, not just the number of hours. Manufacturer battery claims and GlassesResearch observations must remain clearly separated.

## 6. Thermal behavior

During representative and sustained use, record:

- where heat is felt;
- whether heat is asymmetric;
- whether performance changes under sustained workload;
- whether charging and use can occur simultaneously;
- any automatic shutdown, warning, dimming, or feature limitation.

Avoid unsafe stress testing. The purpose is to document normal and sustained consumer use, not force a failure.

## 7. Camera and visual AI

Where applicable, test:

- capture resolution and aspect ratio;
- indoor daylight, outdoor daylight, low light, and backlit scenes;
- shutter/capture latency;
- stabilization behavior;
- recording indicator visibility;
- media transfer time;
- OCR;
- object/scene description;
- repeated questions about the same scene;
- whether the AI can reason over a live or recently captured view;
- what happens without network access.

A camera score and a Visual AI score should remain separate.

## 8. Audio and microphones

Test:

- quiet-room speech;
- street or fan noise;
- wind exposure under ordinary outdoor use;
- music/podcast intelligibility;
- call quality where supported;
- sound leakage at normal listening volume;
- voice-command pickup at different speaking levels.

Record hearing limitations or test constraints when they could affect interpretation.

## 9. Display / HUD

Where a display exists, test:

- indoor readability;
- outdoor shade;
- direct bright daylight where safe and practical;
- perceived sharpness;
- color or monochrome behavior;
- eyebox tolerance;
- alignment sensitivity;
- visible ghosting or reflections;
- comfort during at least 30 minutes of continuous use;
- prescription or insert effect where applicable;
- latency for host-driven content.

If no HUD/display exists, the report-card HUD entry is **N/A**, not zero.

## 10. Wearability

Use the glasses for an ordinary extended session and record:

- temple pressure;
- nose pressure;
- slipping;
- weight balance;
- interference with hats, hearing protection, helmets, or headphones where relevant;
- social conspicuousness, including prominent external branding and visible optical elements;
- ease of putting on/removing;
- comfort after one hour and, where feasible, several hours.

Wearability should reflect actual use, not merely appearance in product photography.

### Discreetness observation (separate Core Report Card dimension)

Before assigning a Discreetness score, examine the glasses **as worn** from the viewpoint of another person, where practical:

- Document logos, etched/printed lettering, or other markings visible on each exterior temple; record contrast and ordinary viewing distance.
- Look for rectangular display/waveguide structures, tinted or colored reflections, unusual lens shapes, or optical artifacts **with the device off**, then again during ordinary powered use.
- Check side/front views and everyday lighting, including indirect indoor light and brighter illumination. Record distance and angle; do not assume close-up artifacts will be noticeable socially.
- Record obvious hardware bulges, cables, camera/sensor modules, controls, or audible behaviors that differentiate the device from regular glasses.
- If a second person is available and consents, ask what they notice without prompting them to look for electronics. Do not record people without consent.
- Document visible camera/recording indicators as part of the outward appearance, while recognizing that privacy-appropriate indicators are desirable safeguards, not inherently a flaw.

Separate **owner impression**, **photographically observed characteristics**, and **independent observer findings**. If only the owner's bench inspection is available, report that limitation and leave social detectability unverified. Refer to [Report Card Method](REPORT_CARD_METHOD.md) for the core Discreetness rubric; do not replace its score with the broader Wearability rating.

## 11. Software quality

Record:

- app stability;
- pairing/reconnection reliability;
- update behavior;
- media synchronization;
- settings clarity;
- error messages;
- unwanted prompts;
- region restrictions;
- subscription prompts;
- whether major functions are understandable without undocumented workarounds.

### Cross-cutting task evaluation: complexity versus friction

**Complexity is not automatically a problem; friction is not a proxy for feature count.** A basic device may be effortless or frustrating, and an ambitious device may be either. Evaluate *the work the wearer is trying to do* rather than rewarding simplicity or penalizing sophistication.

For each important supported task (for example, take a call, start a hands-free conversation, read a HUD notification, translate speech, or recover after Bluetooth disconnects), document:

- **Task and intended outcome:** What was the wearer trying to achieve? Note whether the device actually offers that capability; an absent feature cannot earn a low-friction success for that task.
- **First use versus repeated use:** Setup, learning, accounts, permissions, and required phone interaction; then the steps required once familiar.
- **Interaction burden:** Taps, gestures, delays, attention shifts, reach-for-phone events, re-pairing, unclear feedback, or accidental triggers, including whether hands-free operation remains hands-free.
- **Recovery burden:** What the user must do after ordinary interruptions such as phone calls, disconnects, lock-screen changes, or companion-app restarts.
- **Physical and social burden:** Comfort, visible display or branding, audibility to bystanders, and whether use is practical in the intended environment.
- **Dependability over time:** Record separately a successful first test, repeatable short-term behavior, and long-term reliability. Do not infer durability from a smooth afternoon.

Describe the friction **relative to the particular task and tester**, with host OS, app/firmware state and environmental conditions when known. Separate unfamiliarity with controls from a demonstrated design defect. If useful, record a simple/complex × low/high friction comparison, but do not translate it into an unexplained overall score or claim that different-function products are direct substitutes.

Include observed task friction within the relevant existing Report Card evidence (especially Android Compatibility, Discreetness, Software, Wearability, Owner Control or their extended ratings). Do not add a seventh Core dimension merely to capture the idea. Preserve useful subjective findings as *personally observed* rather than generalizing to every owner.

The [first-use KWENRUN audio-glasses field note](research/kwenrun-audio-first-use-fieldwork-2026-10-31.md) illustrates how modest capabilities can work with little initial friction while endurance, optics and long-term reliability remain unverified.

## 12. Developer and owner-control verification

Where official developer documentation exists, record what the vendor documents for display, camera, audio, sensors, transport, and supported host platforms. Where no official path exists, record only independently demonstrated behavior and label it accordingly.

Do not award openness based on marketing language alone.

## 13. Survival check

Record which parts of the product depend on:

- a vendor account;
- a companion application;
- a firmware service;
- a hosted AI service;
- a subscription;
- proprietary accessories;
- a specific phone operating system.

Then summarize what useful functions would remain if each dependency disappeared.

## 14. Evidence package

A completed hands-on review should preserve, where appropriate and legally distributable:

- photographs;
- model/revision identifiers;
- firmware/app versions;
- manufacturer documentation links;
- timestamps and test conditions;
- battery logs;
- screenshots of user-visible behavior;
- short notes for failed or inconclusive tests.

Failed tests are evidence. Unknowns should remain unknown rather than being filled by assumption.

## 15. Report-card publication

Only after the evidence package is complete should the standard report card be finalized:

**Hardware · Wearability · Visual AI · Software · HUD · Openness · Owner Control · Cloud Independence · Hackability · Value**

Use **N/A** where a dimension genuinely does not apply. Scores should be calibrated against the same standard across every model; a 10 means the same thing regardless of brand, price, age, or popularity.
