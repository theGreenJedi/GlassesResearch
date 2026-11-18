import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import agentic_discovery as a

class TestAgentic(unittest.TestCase):
    def test_distinct_platforms_and_lower_bound(self):
        data = {"cloudflare_web_analytics": {"available": True, "rolling_7d": {"referrers": [
            {"referrer": "chatgpt.com", "pageviews": 3},
            {"referrer": "www.perplexity.ai", "pageviews": 2},
            {"referrer": "notchatgpt.com", "pageviews": 99}]}}}
        r = a.browser_referrals(data)
        self.assertEqual(r["status"], "partial")
        self.assertEqual(r["platform_pageviews"]["ChatGPT"], 3)
        self.assertEqual(r["platform_pageviews"]["Perplexity"], 2)
    def test_missing_is_not_zero(self):
        self.assertIsNone(a.browser_referrals({})["platform_pageviews"])
        self.assertIsNone(a.export_metrics(None)["bing_ai"]["total"])
    def test_export_window_and_units(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "exports.json"
            p.write_text(json.dumps({"bing_ai": {"start": "2026-11-01", "end": "2026-11-07", "total": 0}}))
            r = a.export_metrics(p)
            self.assertEqual(r["bing_ai"]["total"], 0)
            self.assertEqual(r["bing_ai"]["unit"], "citation appearances")
            self.assertIsNone(r["google_ai"]["total"])
    def test_unavailable_api(self):
        with patch.dict("os.environ", {"CLOUDFLARE_API_TOKEN": "", "CLOUDFLARE_ZONE_ID": ""}):
            self.assertIsNone(a.edge_metrics("start", "end")["crawler_requests"]["counts"])
    def test_graphql_error_not_zero(self):
        with patch.object(a.requests, "post") as post:
            post.return_value.ok = True
            post.return_value.json.return_value = {"errors": [{"message": "access denied"}]}
            self.assertIsNone(a.cloudflare_query("token", "zone", "start", "end", ["x"])["counts"])

if __name__ == "__main__":
    unittest.main()
