# Rokid AR Spatial — active system investigation

Rokid AR Spatial is a current commercial spatial-computing package built around **Rokid Max 2 glasses + Rokid Station 2**.

**Technology lineage:** [Rokid](../../lineages/ROKID.md)  
**Identity treatment:** product/system bundle; does **not** create another smart-glasses identity beyond Max 2 (`GLS-0094`)  
**Evidence state:** current first-party manufacturer documentation; hands-on verification pending

## Current first-party definition

Rokid's AR-series comparison, checked 2026-09-05, defines AR Spatial as:

- Max 2 glasses plus Station 2;
- 3DoF spatial computing;
- up to three virtual app windows;
- Station 2 running YodaOS-Master;
- 8 GB RAM and 128 GB storage in the Station 2 compute layer;
- Wi-Fi 6 and Bluetooth 5.2 in Station 2;
- 5000 mAh Station 2 battery with approximately five-hour claimed runtime and 18 W charging;
- keyboard and mouse support;
- ray, touch, voice, and remote-control interaction.

The glasses remain Max 2. Station 2 supplies the dedicated spatial-computing host layer.

## Why GlassesResearch tracks the bundle

The package is commercially meaningful because it changes what the owner can do with Max 2. It introduces a vendor-controlled compute/OS layer, dedicated spatial UI, app behavior, additional wireless radios, storage, battery, and update/service dependencies that are absent when Max 2 is used as a generic tethered display.

That means AR Spatial deserves a dedicated investigation page even though it should not inflate the eyewear model count.

## Investigation queue

1. Verify Station 2 hardware, OS build, boot chain, update mechanism, storage access, and recovery path.
2. Determine app-installation and sideloading options, developer mode, ADB exposure, file-system access, and package restrictions.
3. Measure how much Max 2 functionality remains when Station 2 is absent or unavailable.
4. Test spatial-window behavior, tracking stability, input methods, keyboard/mouse support, and local media handling.
5. Document account, network, telemetry, cloud-service, and regional dependencies.
6. Separate glasses firmware, Station 2 firmware, YodaOS-Master software, and Rokid AR App responsibilities.
7. Compare AR Spatial owner control and service survival against bare Max 2 and Max 2 + original Rokid Station.

## Primary sources

- [Rokid AR Spatial product page](https://global.rokid.com/products/rokid-ar-spatial)
- [Rokid AR Glasses Series comparison](https://global.rokid.com/collections/rokid-ar-glasses-series)
- [Rokid Max 2 spatial-computing FAQ](https://global.rokid.com/blogs/max-2/does-the-rokid-max-2-support-spatial-computing)

## Related GlassesResearch resources

- [Rokid lineage](../../lineages/ROKID.md)
- [Rokid Max 2](../RokidMax2/README.md)
- [Rokid AR Joy 2](../RokidARJoy2/README.md)
- [Rokid populated research record](../../research/populated/ROKID.md)
