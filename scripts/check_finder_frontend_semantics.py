#!/usr/bin/env python3
"""Guard the single generated Finder capability contract across public Finder surfaces."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FULL = ROOT / "docs" / "javascripts" / "glasses-finder-v3.js"
HOME = ROOT / "docs" / "javascripts" / "homepage-finder.js"


def main():
    full = FULL.read_text(encoding="utf-8")
    home = HOME.read_text(encoding="utf-8")
    errors = []

    required_full = [
        "const capabilityState = (r, field) => r.capabilityFacts?.[field]?.value || 'unknown';",
        "if (canonical === 'yes') return 'yes';",
        "return 'unknown';",
        "const filterMatches = (r, filter) => filterState(r, filter) === 'yes';",
    ]
    for snippet in required_full:
        if snippet not in full:
            errors.append(f"full Finder is missing canonical capability guard: {snippet}")

    forbidden_full = [
        "const aliases = {",
        "'inferred-yes'",
        "fn ? Boolean(fn(r))",
    ]
    for snippet in forbidden_full:
        if snippet in full:
            errors.append(f"full Finder still contains presentation-layer capability inference: {snippet}")

    required_home = [
        "data/finder-capabilities.json",
        "capabilities.get(device.id)?.[filter.capability]?.value === 'yes'",
    ]
    for snippet in required_home:
        if snippet not in home:
            errors.append(f"homepage Finder is not using the canonical capability matrix: {snippet}")

    if errors:
        print("Finder frontend semantic regression FAILED:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Finder frontend semantic regression OK: homepage and full Finder consume canonical yes/no/unknown/na capability states without UI inference.")


if __name__ == "__main__":
    main()
