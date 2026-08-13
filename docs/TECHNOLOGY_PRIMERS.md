# Smart-Glasses Technology Primers

This page explains the technologies that sit underneath product names. The goal is to make GlassesResearch useful even when a reader has never heard of a particular model.

## Display architectures

### Waveguides

Waveguides route light from a display engine through a thin transparent optical element and toward the eye. They can support relatively normal-looking glasses because the image does not require a large opaque screen directly in front of the wearer. Important variables include field of view, eyebox size, brightness, color uniformity, efficiency, ghosting, and how well the system remains readable outdoors.

Waveguide is not a quality grade. Two waveguide products can differ dramatically in brightness, color, viewing comfort, efficiency, and manufacturing consistency.

### Birdbath optics

Birdbath systems use partially reflective optical elements to combine a display image with the real world. They are common in display-oriented glasses because they can deliver strong image quality at lower cost than some waveguide systems, but they usually require more optical volume and therefore bulkier frames.

### MicroOLED

MicroOLED places an OLED display on a silicon backplane. It can provide very high pixel density and strong contrast in a compact display engine. It is common in near-eye displays where image quality matters more than extreme transparency or all-day eyewear form factor.

### MicroLED

MicroLED uses microscopic light-emitting diodes and is attractive for transparent near-eye systems because of its potential brightness and efficiency. In smart glasses, the practical result depends on the complete optical system, not the display panel alone.

### LCOS

Liquid Crystal on Silicon is a reflective microdisplay technology used in some near-eye display architectures. It can provide high resolution, but the surrounding illumination and optical system affect size, efficiency, contrast, and overall frame design.

## Geometry that matters

### Field of view

Field of view describes how much of the wearer's visual field the display occupies. A larger number can enable more immersive or information-dense experiences, but it may also increase optical complexity, weight, power demand, and alignment sensitivity.

### Eyebox

The eyebox is the region in which the eye can move while still seeing the intended image. A tiny eyebox can make a technically impressive display frustrating in normal use. Fit, prescription geometry, interpupillary distance, nose position, and frame movement all influence the real experience.

### Eye relief

Eye relief is the distance between the optical system and the eye at which the display remains usable. This matters for facial geometry, prescription inserts, eyelashes, and comfort.

## Sensing and tracking

### IMU

An inertial measurement unit typically combines accelerometers and gyroscopes, sometimes with a magnetometer. It allows a device to estimate motion and orientation. IMU data is useful for head tracking, gesture interpretation, stabilization, and contextual sensing.

### SLAM

Simultaneous Localization and Mapping combines sensor data to estimate device position while building or updating a representation of the surrounding environment. It is central to spatial computing, but full SLAM requires more sensing, processing, calibration, and power than simple head-orientation tracking.

### Eye tracking

Eye tracking estimates where the wearer is looking. It can support interface control, attention-aware systems, foveated rendering, accessibility, and research. Its presence does not automatically mean third-party developers can access gaze data.

### Hand tracking

Hand tracking uses cameras or other sensors to estimate hand position and gestures. It can replace physical controllers in some spatial systems, but accuracy, latency, field of view, lighting, and compute requirements vary substantially.

## Cameras and computer vision

A camera-equipped pair of glasses can serve several very different roles: photography, video capture, visual AI, navigation, remote assistance, object recognition, OCR, or spatial mapping. Resolution alone does not determine usefulness. Field of view, stabilization, exposure behavior, low-light performance, sensor access, latency, and whether video is available continuously to software are often more important.

## Audio architectures

### Open-ear speakers

Many smart glasses use directional speakers positioned near the ear. They preserve environmental awareness and avoid an in-ear device, but privacy, bass response, wind performance, leakage, and maximum volume vary considerably.

### Beamforming microphones

Multiple microphones can be combined to emphasize sound from a desired direction and reduce noise. The practical result depends on microphone placement, signal processing, wind handling, and software—not microphone count alone.

### Bone-conduction systems

Bone-conduction audio transmits vibration through the skull rather than relying entirely on air-conducted sound. It can preserve ear-canal openness, but comfort and fidelity differ from open-ear speaker designs.

## Compute architecture

### On-glasses compute

Processing on the glasses can reduce latency and dependence on a host, but heat, battery, weight, and frame volume constrain how much compute can reasonably be worn all day.

### Phone-tethered compute

The glasses provide sensing, audio, display, or control while a phone performs much of the processing. This can improve battery life and reduce frame bulk while preserving access to powerful mobile processors and networking.

### Local companion compute

A phone, laptop, pocket computer, or nearby workstation can run perception, memory, and AI locally while the glasses remain the sensor/interface layer. This architecture can reduce cloud dependence and is especially relevant to owner-controlled wearable systems.

### Cloud compute

Cloud services can provide extremely capable AI with minimal on-device compute, but they introduce connectivity, account, privacy, latency, subscription, and long-term service-dependence questions.

## The rule GlassesResearch uses

Never infer the whole product from one component. A microLED display does not guarantee a good HUD. A camera does not guarantee visual AI. Bluetooth does not guarantee developer access. An SDK does not guarantee owner control. "AI" does not explain whether inference is local, phone-based, or cloud-based.

The useful unit of analysis is the complete system: **hardware + optics + software + host + cloud + ownership model + physical wearability.**
