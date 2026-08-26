#!/usr/bin/env python3
"""Guard frontend Finder semantics that must never collapse unknown into a negative."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FINDER = ROOT / "docs" / "javascripts" / "glasses-finder-v3.js"


def main():
    text = FINDER.read_text(encoding="utf-8")
    errors = []

    unsafe_inverse = "no_display: (r) => !aliases.display(r)"
    if unsafe_inverse in text:
        errors.append("no_display still infers a verified absence from missing positive display evidence")

    canonical_guard = "if (filter.field === 'no_display') return 'unknown';"
    if canonical_guard not in text:
        errors.append("no_display does not stop at canonical unknown before frontend inference")

    if errors:
        print("Finder frontend semantic regression FAILED:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Finder frontend semantic regression OK: canonical no_display=unknown remains unknown.")


if __name__ == "__main__":
    main()
