"""Rewrite repository-only research citations before MkDocs link validation.

The public site intentionally stages selected documentation, model, and lineage
content rather than the entire repository. Those public pages may still cite
source research under ``research/``. Relative links to that non-staged tree
would make ``mkdocs build --strict`` fail even though the evidence exists in
the repository.

Keep the research tree repository-only and turn only those relative citations
into canonical GitHub source links. All other links remain untouched so strict
MkDocs validation continues to catch real public-site link errors.
"""
from __future__ import annotations

import re

REPOSITORY_BLOB_ROOT = "https://github.com/theGreenJedi/GlassesResearch/blob/main/"
_REPOSITORY_RESEARCH_LINK = re.compile(
    r"\]\((?P<target>(?:\.\./)+research/[^)\s]+)\)"
)


def on_page_markdown(markdown: str, **_kwargs) -> str:
    """Rewrite relative links into repository-only ``research/`` sources."""

    def replace(match: re.Match[str]) -> str:
        target = match.group("target")
        while target.startswith("../"):
            target = target[3:]
        return f"]({REPOSITORY_BLOB_ROOT}{target})"

    return _REPOSITORY_RESEARCH_LINK.sub(replace, markdown)
