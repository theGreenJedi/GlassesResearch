# Privacy, security, and social acceptability

Face-worn cameras and microphones affect people beyond the owner. Technical legality is only one part of responsible use.

**Information reviewed:** 2026-08-05. Product availability, software, prices, and advertised battery life can change. Unless explicitly marked hands-on, statements below are sourced from manufacturers, project documentation, or attributed community material.

## 61. Are smart glasses legal to wear?

Generally, wearing electronics is legal, but recording laws, workplace rules, private-property policies, driving restrictions, and sensitive-location rules vary by jurisdiction. Audio recording can be more restricted than photography. This repository is not legal advice: check the laws and policies where you will actually use the device.

## 62. Is it legal to record people with smart glasses?

It depends on location, whether audio is captured, reasonable expectations of privacy, consent rules, and the setting. Bathrooms, healthcare spaces, workplaces, schools, and private businesses may prohibit recording regardless of public-space law. Ask before recording, respect visible objections, and stop when consent is unclear.

## 63. How can people tell when camera glasses are recording?

Responsible products use a visible capture indicator, but indicators differ in brightness and placement and may be hard to see. Never cover, disable, or obscure it. Because bystanders may not recognize the signal, verbal consent is better than relying on an LED alone.

## 64. Are camera-free smart glasses better for privacy?

They remove the risk of first-person photo/video capture by the glasses, which materially improves bystander privacy. They may still contain microphones, transmit text, use cloud AI, collect telemetry, or display sensitive information. Even G2 has no camera or speakers but includes four microphones and Bluetooth, so camera-free does not mean data-free. Source: [Even G2 specifications](https://support.evenrealities.com/hc/en-us/articles/13499229138959-Specs).

## 65. Do AI glasses send photos and audio to the cloud?

Many AI features do, directly or through a phone, but the exact path varies by feature and provider. Read the current privacy policy, permissions, retention rules, training-use terms, subprocessors, and deletion controls. Open source makes inspection possible but does not automatically prove that a deployment is private.

## 66. Are open-source smart glasses automatically secure?

No. Open source enables audit, modification, and independent review; it does not guarantee good defaults, timely patches, secure cloud services, or safe third-party apps. MentraOS’s MIT-licensed source and disclosure program are positive research signals, but each deployment still needs threat modeling and update discipline. Sources: [MentraOS repository](https://github.com/Mentra-Community/MentraOS), [Mentra privacy policy](https://mentraglass.com/privacy-policy).

## 67. What data should be erased before selling smart glasses?

Import anything you want to keep, then remove accounts, pairings, captures, Wi-Fi credentials, and app data using the manufacturer’s factory-reset process. Ray-Ban states that a reset removes captures and the Meta-account association and is required before another account can use the glasses. Also unpair from the phone and revoke connected-app access. Source: [Ray-Ban Meta FAQ](https://www.ray-ban.com/usa/c/frequently-asked-questions-ray-ban-meta-smart-glasses).

## 68. Can an employer require smart glasses at work?

Employers may deploy wearables subject to local labor, privacy, safety, disability, and recording rules, but a technically possible deployment can still be coercive or unsafe. A responsible program defines purpose, data collection, access, retention, bystander handling, accommodations, device hygiene, and a non-retaliatory reporting path.

## 69. Should smart glasses be used in healthcare?

Only with explicit institutional approval, patient consent, appropriate security, and a defined clinical workflow. Consumer cloud services may not meet healthcare privacy or retention requirements. Enterprise products such as Vuzix M400 target healthcare and remote assistance, but hardware marketing does not establish regulatory or organizational compliance. Source: [Vuzix smart glasses](https://www.vuzix.com/pages/smart-glasses).

## 70. How can smart-glasses privacy be evaluated before purchase?

List every sensor, required permission, account, cloud endpoint, retention rule, training-use term, export/delete control, indicator, and offline function. Then test network-denied behavior and factory reset. Favor vendors with clear policies, update histories, security contacts, and a useful device even when optional cloud features are disabled.
