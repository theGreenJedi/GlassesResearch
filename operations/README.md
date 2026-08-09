# Operations

Maintainer-facing operational documentation for GlassesResearch.

> **OPSEC policy:** This public repository documents architecture, service roles, health checks, and recovery procedures. Provider-specific identifiers, account metadata, credentials, API tokens, recovery codes, assigned nameservers, private dashboard screenshots, billing details, and other operational secrets are intentionally omitted.

- [Control Room](CONTROL_ROOM.md) — architecture, health checks, recovery steps, service status, and operational metrics.
- [Traffic & Operations Snapshots](TRAFFIC_SNAPSHOTS.md) — periodic analytics/search/repository baselines and trend notes.

This directory is intentionally separate from public research navigation. Its purpose is to preserve how the site is operated and measured so infrastructure knowledge does not depend on individual memory or chat history.

Sensitive maintainer-only notes should live outside the public repository. If a local `operations-private/` directory is used, it is excluded by `.gitignore` and must never contain credentials that are not also protected by an appropriate password manager or secrets store.
