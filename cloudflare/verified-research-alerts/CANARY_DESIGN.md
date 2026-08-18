# Verified Research Alerts delivery canary

GlassesResearch treats outbound alert delivery as a chain that must be proven end to end:

`verified publication -> alerts Worker -> mail provider acceptance -> SMTP delivery -> Cloudflare Email Routing -> canary Email Worker -> D1 receipt`

The synthetic recipient is `delivery@canary.glassesresearch.org`. It is intentionally isolated on a mail subdomain so provisioning the witness does not replace or modify apex `glassesresearch.org` mail records.

Every dispatch-enabled verified publication produces one canary message in addition to subscriber delivery. The canary message uses the same sender and mail-provider path as subscriber mail and carries three operational headers: a stable publication ID, a UTC sent-at timestamp, and an HMAC signature. The signature key is derived from the existing publisher secret with domain separation; the secret itself never enters a message.

The receiving Email Worker rejects mail whose recipient, publication ID, timestamp, or signature is invalid. It records only the publication ID, receive timestamp, and Message-ID when present. It does not persist message bodies, subscriber addresses, subscription filters, or tokens.

The authenticated `/delivery-proof` endpoint exposes non-PII state for a publication: whether a canary send was attempted, whether the provider accepted it, provider message ID if returned, whether the receiving Worker observed it, and the receipt timestamp. The publication workflow polls this proof and fails closed unless the exact canary receipt is present.

Publication ingestion and canary receipts are idempotent by publication ID, so rerunning a publication is safe.
