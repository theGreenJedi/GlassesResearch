"""Regression tests for date-grouped Search Console history and reconciliation."""
import json
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import analytics_history as history


class AnalyticsHistoryTests(unittest.TestCase):
    def test_date_grouping_never_invents_zeros(self):
        start, end = date(2026, 10, 1), date(2026, 10, 3)
        rows = [
            {"keys": ["2026-10-01"], "impressions": 11, "clicks": 1, "position": 12},
            {"keys": ["2026-10-03"], "impressions": 6, "clicks": 0, "position": 9},
        ]
        result = history.normalized_gsc_days(rows, start, end)
        self.assertEqual(set(result), {"2026-10-01", "2026-10-03"})
        self.assertEqual(result["2026-10-01"]["ctr"], 1 / 11)
        self.assertNotIn("2026-10-02", result)

    def test_malformed_date_and_duplicate_are_rejected(self):
        with self.assertRaises(ValueError):
            history.normalized_gsc_days([{"keys": ["bad"], "impressions": 1}], date(2026, 10, 1), date(2026, 10, 3))
        duplicate = [{"keys": ["2026-10-01"], "impressions": 1}, {"keys": ["2026-10-01"], "impressions": 2}]
        with self.assertRaises(ValueError):
            history.normalized_gsc_days(duplicate, date(2026, 10, 1), date(2026, 10, 3))

    def test_backfill_replaces_false_zeros_and_preserves_details(self):
        with tempfile.TemporaryDirectory() as tmp:
            series = Path(tmp) / "analytics" / "series"
            series.mkdir(parents=True)
            old = {
                "schema_version": 1, "month": "2026-10", "updated_at": None,
                "cloudflare": {"days": {}, "summary": {}},
                "cloudflare_web_analytics": {"days": {}, "summary": {}},
                "google_search_console": {
                    "days": {
                        "2026-10-01": {"date": "2026-10-01", "impressions": 0, "clicks": 0, "position": 0, "top_queries": [], "top_pages": []},
                        "2026-10-02": {"date": "2026-10-02", "impressions": 4, "clicks": 1, "position": 15, "top_queries": [{"query": "hello"}], "top_pages": []},
                    }, "summary": {},
                },
            }
            (series / "2026-10.json").write_text(json.dumps(old))
            rows = history.normalized_gsc_days([
                {"keys": ["2026-10-02"], "clicks": 2, "impressions": 20, "position": 10},
                {"keys": ["2026-10-03"], "clicks": 0, "impressions": 8, "position": 8},
            ], date(2026, 10, 1), date(2026, 10, 3))
            with patch.object(history, "SERIES", series):
                changed = history.replace_gsc_days(rows, date(2026, 10, 1), date(2026, 10, 3))
            saved = json.loads((series / "2026-10.json").read_text())["google_search_console"]
            self.assertGreaterEqual(changed, 2)
            self.assertNotIn("2026-10-01", saved["days"])
            self.assertEqual(saved["days"]["2026-10-02"]["impressions"], 20)
            self.assertEqual(saved["days"]["2026-10-02"]["top_queries"], [{"query": "hello"}])
            self.assertEqual(saved["days"]["2026-10-03"]["top_queries"], [])
            self.assertEqual(saved["summary"]["impressions"], 28)
            self.assertEqual(saved["summary"]["clicks"], 2)

    def test_reconciliation_flags_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            series = Path(tmp) / "analytics" / "series"
            series.mkdir(parents=True)
            (series.parent / "latest.json").write_text(json.dumps({
                "google_search_console": {"available": True, "rolling_28d": {
                    "start": "2026-10-01", "end": "2026-10-28", "impressions": 31, "clicks": 2,
                }}
            }))
            with patch.object(history, "SERIES", series):
                actual = history.reconcile_gsc({"2026-10-02": {"impressions": 20, "clicks": 2}})
                self.assertEqual(actual["status"], "mismatch")
                self.assertEqual(actual["daily_impressions"], 20)
                expected = history.reconcile_gsc({"2026-10-02": {"impressions": 31, "clicks": 2}})
                self.assertEqual(expected["status"], "match")


if __name__ == "__main__":
    unittest.main()
