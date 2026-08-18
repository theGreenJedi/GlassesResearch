# Verified Research Alerts delivery canary

This service treats outbound email delivery as a chain that must be proven end to end:

`verified publication -> alerts Worker -> Resend acceptance -> SMTP delivery -> Cloudflare Email Routing -> canary Worker -> D1 receipt`

The canary recipient is isolated on `delivery@canary.glassesresearch.org`, so onboarding it must not replace or modify apex `glassesresearch.org` MX records.

Every dispatch-enabled publication gets one synthetic canary message in addition to any subscriber mail. The message includes the stable publication ID, a UTC sent-at timestamp, and an HMAC signature derived from the existing publisher secret with domain separation. The receiving Email Worker rejects unsigned or invalidly signed mail and records only operational metadata in D1: publication ID, provider/message identifier when available, and received timestamp. It does not persist message bodies or subscriber addresses.

The publication workflow polls the authenticated delivery-proof endpoint after publishing. A publication is not considered end-to-end proven until the matching canary receipt appears. Replays are safe because both publication ingestion and receipt storage are idempotent by publication ID.

The Email Routing subdomain and routing rule are provisioned separately from the public site. Cloudflare management credentials used for that provisioning need the appropriate Worker/D1, Zone Settings, DNS and Email Routing Rules permissions.
