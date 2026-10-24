"""Regression tests for production Markdown-to-public-route proof mapping."""

import unittest
from pathlib import Path

from scripts.verify_changed_public_pages import REGRESSION_CANARIES, public_output


class PublicProofRouteTests(unittest.TestCase):
    def test_root_readme_is_homepage(self):
        self.assertEqual(public_output("README.md", Path("site")), (Path("site/index.html"), "/"))

    def test_nested_readme_is_directory_index(self):
        self.assertEqual(
            public_output("docs/faq/README.md", Path("site")),
            (Path("site/docs/faq/index.html"), "/docs/faq/"),
        )

    def test_regular_faq_page(self):
        self.assertEqual(
            public_output("docs/faq/01-basics.md", Path("site")),
            (Path("site/docs/faq/01-basics/index.html"), "/docs/faq/01-basics/"),
        )

    def test_index_page(self):
        self.assertEqual(
            public_output("docs/news/index.md", Path("site")),
            (Path("site/docs/news/index.html"), "/docs/news/"),
        )

    def test_practical_answers_are_production_canaries(self):
        self.assertTrue({"docs/faq/README.md", "docs/faq/01-basics.md", "docs/faq/09-development-openness.md"}.issubset(REGRESSION_CANARIES))


if __name__ == "__main__":
    unittest.main()
