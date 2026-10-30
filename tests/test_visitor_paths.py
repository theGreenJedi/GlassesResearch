"""Audience-path summaries must never masquerade as visitor funnels."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from analytics_report import visitor_path_counts


class VisitorPathsTests(unittest.TestCase):
    def test_observed_pageviews_group_by_known_routes(self):
        paths = [
            {"path": "/docs/faq/08-accessibility-fit/", "pageviews": 8},
            {"path": "/guides/smart-glasses-without-cameras/", "pageviews": 4},
            {"path": "/models/catalog/gls-0047/", "pageviews": 3},
            {"path": "/docs/COMPARISON_ENGINE/", "pageviews": 2},
            {"path": "/docs/FEEDS/", "pageviews": 1},
            {"path": "/docs/RESEARCH_NEWS/", "pageviews": 1},
            {"path": "/", "pageviews": 300},
        ]
        self.assertEqual(visitor_path_counts(paths), {
            "Practical Answers": 8, "Buying and use-case guides": 4,
            "Model research": 3, "Find & Compare": 2, "Follow verified work": 2,
        })

    def test_no_paths_is_not_a_visit(self):
        self.assertTrue(all(x == 0 for x in visitor_path_counts([]).values()))


if __name__ == "__main__":
    unittest.main()
