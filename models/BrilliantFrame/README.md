# Brilliant Labs Frame — GLS-0051

Open/developer-oriented smart glasses from Brilliant Labs with a color display, camera, microphone and unusually extensive public hardware/software documentation.

## Hardware

Brilliant Labs publishes primary hardware documentation describing:

- color OLED display, 640 × 400, approximately 20° field of view;
- 720p low-power color camera;
- TDK ICS-41351 MEMS microphone;
- Nordic nRF52840 Bluetooth MCU;
- Lattice CrossLink-NX FPGA;
- 210 mAh battery;
- accelerometer and e-compass;
- prescription-lens support through a prescription clip.

The public hardware manual includes block diagrams, schematics, mechanical information and firmware-development details rather than only marketing specifications.

## Developer access

Frame supports a documented SDK ecosystem including Python, Flutter, Lua, direct Bluetooth development and public firmware source. Brilliant Labs documents the BLE protocol and publishes source repositories through GitHub.

The official hardware documentation also describes access to the physical SWD debug interface for lower-level MCU work, although reaching it requires disassembly.

## Primary sources

- [Frame hardware manual](https://docs.brilliant.xyz/frame/hardware/)
- [Frame SDK](https://docs.brilliant.xyz/frame/frame-sdk/)
- [Frame Bluetooth specification](https://docs.brilliant.xyz/frame/frame-sdk-bluetooth-specs)
- [Frame Python SDK](https://github.com/brilliantlabsAR/frame-sdk-python)
- [Frame firmware codebase](https://github.com/brilliantlabsAR/frame-codebase)

## Related GlassesResearch resources

- [Comparison engine](../../docs/COMPARISON_ENGINE.md)
- [Developer resources](../../hacking/README.md)
- [Artifact ledger](../../resources/PRIMARY_ARTIFACT_PRESERVATION_LEDGER.md)
