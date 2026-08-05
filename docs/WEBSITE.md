# GlassesResearch Website

The public website is a reading layer over the same Markdown that powers the GitHub repository.

## Public address

After GitHub Pages is enabled with **GitHub Actions** as its source, the site is expected at:

- [https://thegreenjedi.github.io/GlassesResearch/](https://thegreenjedi.github.io/GlassesResearch/)

## One source of truth

The website does not maintain a second copy of the research. `scripts/prepare_site.py` stages the existing repository content into a temporary build directory:

- `README.md` becomes the site home page.
- `WHY.md` remains the mission page.
- `docs/`, `models/`, `glossary/`, and `images/` are copied without rewriting their content.
- `mkdocs.yml` supplies the public navigation and presentation layer.

The temporary `.site-src/` directory and generated `site/` directory are build products, not canonical content.

## Publishing workflow

`.github/workflows/pages.yml` runs when changes reach `main` or when manually dispatched. It:

1. Checks out the repository.
2. Installs the pinned documentation dependency set.
3. Stages the repository Markdown.
4. Builds the site in strict mode so broken navigation or links fail visibly.
5. Uploads the static artifact.
6. Deploys it through GitHub Pages.

## Initial navigation

The first release exposes:

- Project mission and purpose
- W610 question-led chapter
- Timeline and genealogy
- Community Map and Research Portal
- Hardware, BLE, firmware, software, manufacturing, diagnostics, and engineering sections
- Canonical glossary entries
- Project vision, repository laws, evidence standard, and investigation workflow

## Local preview

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements-docs.txt
python scripts/prepare_site.py
mkdocs serve
```

Then open `http://127.0.0.1:8000/`.

## GitHub setting required

In the repository, open **Settings → Pages** and set **Source** to **GitHub Actions**. The workflow can build immediately after merge, but GitHub will not publish the site until Pages is configured to accept Actions deployments.

## Future improvements

Future investigations may add custom visual identity, diagrams, tags, richer search, archived-resource indicators, and a custom domain. Those additions should continue to use the repository Markdown as the canonical source.
