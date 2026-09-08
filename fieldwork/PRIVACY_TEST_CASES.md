# Fieldwork serial-privacy test cases

Production clients and intake services must prove these cases before accepting real submissions.

1. Enter a serial, submit, and inspect durable client storage: the raw serial is absent.
2. Inspect application logs, crash reports, analytics payloads, network diagnostics, and server logs: the raw serial is absent.
3. Inspect the persisted submission: only the one-way `device_fingerprint` may remain.
4. Repeat with the same normalized model + serial: duplicate detection returns the same device identity result expected by the chosen cryptographic construction.
5. Submit without a serial: the contribution remains valid and no synthetic fingerprint is invented.
6. Change attribution from public to anonymous: device duplicate handling is unchanged and no contributor identity is inferred from the fingerprint.
7. Export a contribution: raw serial and private device fingerprint are absent from public/exported research views unless an explicitly private moderator export is separately defined.
8. Error during fingerprint generation: fail closed by omitting the fingerprint; never fall back to persisting the raw serial.

The final fingerprint algorithm requires separate cryptographic/privacy review. These tests describe the invariant independent of implementation.
