# Issue #381 validation fixture

This fixture documents the required Finder behavior for inverse display semantics.

| Canonical `display` | Canonical `no_display` | `No display` filter result |
| --- | --- | --- |
| `unknown` | `unknown` | must not match |
| `yes` | `no` | must not match |
| `no` | `yes` | must match |

The frontend regression guard in `scripts/check_finder_frontend_semantics.py` enforces that `no_display` cannot be inferred from `!display` and that canonical `no_display=unknown` exits as `unknown` before generic alias inference.
