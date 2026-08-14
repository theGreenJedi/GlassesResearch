# EV-0046 — Even G1/G2 service-survival and developer-path boundary

**Verified:** 2026-08-14  
**Evidence class:** Even Realities support documentation and official GitHub repositories  
**Scope:** G1 and G2; G2 has the stronger documented developer path

## Finding

Even's glasses are phone-hosted HUD peripherals rather than autonomous computers. That architecture leaves some recoverable display value, especially on G2, but the first-party experience is still materially tied to the Even App, an Even account and network services.

## Function matrix

| Function | Local/phone-hosted evidence | Service dependency | Survival assessment |
|---|---|---|---|
| Passive prescription eyewear | Physical lenses/frame remain | None for passive optics | Survives |
| First pairing | Even instructs users to open the app, log in and pair over Bluetooth | Even App and account are part of the documented first-pair flow | Activation risk |
| Basic display transport | Official G2 demo publishes dual-BLE commands for text, images, touch and microphone streams | A compatible phone host is required; firmware compatibility remains | Recoverable with preserved host software |
| Even Hub plugins | Official MIT-licensed templates and tooling expose display, touch, microphone/ASR and image/text app patterns | Plugins run in the Even phone-app/WebView environment; store/portal and host lifecycle can remain dependencies | Meaningful but host-mediated survival |
| Teleprompt/manual display | Content is loaded and controlled through the app; manual/automatic modes reduce AI dependence | Requires the compatible app/transport; initial account gate remains | Plausible phone-local value |
| Notifications/dashboard | Phone notifications are relayed to the display | Requires app permissions, Bluetooth and maintained host compatibility | Recoverable while host software survives |
| QuickNote | G1 documentation says offline voice input is temporarily stored and processed after reconnection | AI organization/processing waits for network | Capture residue survives temporarily; completed feature is service-dependent |
| Conversate | G2 support explicitly says unavailable when Bluetooth is disconnected or the phone is offline | Internet, phone/app connection and microphone permission are required | Cloud/service-essential |
| Translation/navigation/AI | Even's privacy and product documentation identify cloud/third-party processing for translation, navigation, ASR, weather and AI services | Network and maintained service providers | Service-dependent |
| Firmware/settings | Support routes firmware version and updates through the Even App | No owner firmware/bootloader path is established | Vendor-dependent |

## Developer-path significance

Even Realities now publishes:

- the official `EvenDemoApp`, including dual-BLE command examples for display, touch and microphone data;
- MIT-licensed Even Hub starter templates; and
- an official `everything-evenhub` developer repository.

This is stronger preservation evidence than a closed consumer integration. It shows that a future compatible phone application could preserve meaningful G2 HUD interaction. It does **not** establish open firmware, independent first activation, schematics, bootloader access or operation without Even's app environment.

## G1 versus G2

G1's public record supports offline buffering for QuickNote but has a narrower public development surface. G2's official demo and Even Hub repositories provide a clearer recoverability path. Conclusions must not be copied backward from G2 protocol examples to G1.

## Correct label

- **G1:** dependent with narrow offline buffering.
- **G2:** recoverable phone-hosted HUD potential; first-party AI remains service-dependent.

## Remaining empirical tests

1. Pair once, block internet and inventory dashboard, teleprompt, notifications and plugin behavior.
2. Sign out without unpairing and repeat.
3. Preserve an Even Hub package and test whether it can be installed/launched without the portal.
4. Test a minimal local plugin that sends static text and images with all non-LAN endpoints blocked.
5. Preserve app, firmware, plugin runtime and phone OS versions.
6. Determine whether the official demo can connect to retail G2 hardware without an Even account.
7. Test QuickNote offline retention duration and deletion behavior.

## Sources

- [Even G2 pairing](https://support.evenrealities.com/hc/en-us/articles/13754897068559-How-to-Pair)
- [Even G2 Conversate requirements](https://support.evenrealities.com/hc/en-us/articles/14273795154319-Conversate)
- [Even G1 user guide and offline QuickNote behavior](https://support.evenrealities.com/hc/en-us/articles/14301335051023-User-guide)
- [Even device/app privacy and service-provider boundary](https://support.evenrealities.com/hc/en-us/articles/14270525749519-Privacy-Policy-Device-APP)
- [Official EvenDemoApp](https://github.com/even-realities/EvenDemoApp)
- [Official Even Hub templates](https://github.com/even-realities/evenhub-templates)
- [Official Even Hub developer repository](https://github.com/even-realities/everything-evenhub)

## Confidence

High for documented login/pairing flow, Conversate's internet requirement, G1 offline QuickNote buffering and the existence/content of official G2 development repositories. Medium for long-term independent G2 recoverability because account-free connection and portal-free plugin installation have not yet been demonstrated.
