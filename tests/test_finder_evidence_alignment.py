"""Regression checks: manufacturer evidence drives canonical capability answers."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_finder_capabilities as finder


class EvidenceAlignmentTests(unittest.TestCase):
    def test_even_g1_camera_absence_from_primary_source(self):
        data = json.loads((ROOT / "comparisons/data/GLS-0047.json").read_text())
        self.assertEqual(finder.explicit_from_comparison(data, "camera")[0], "no")
        self.assertEqual(finder.explicit_from_comparison(data, "no_camera")[0], "yes")

    def test_even_g2_offline_camera_speakers_match_primary_specs(self):
        data = json.loads((ROOT / "comparisons/data/GLS-0048.json").read_text())
        self.assertEqual(finder.explicit_from_comparison(data, "camera")[0], "no")
        self.assertEqual(finder.explicit_from_comparison(data, "no_camera")[0], "yes")
        self.assertEqual(finder.explicit_from_comparison(data, "offline_operation")[0], "no")
        self.assertEqual(finder.explicit_from_comparison(data, "speakers")[0], "no")

    def test_unresolved_language_does_not_invent_a_negative(self):
        item = {"fields": {"offline_operation": {"value": "Some functions need a phone", "evidence": "primary"}}}
        self.assertEqual(finder.explicit_from_comparison(item, "offline_operation"), (None, None))
        item["fields"]["offline_operation"] = {"value": "Not supported; unconfirmed", "evidence": "unknown"}
        self.assertEqual(finder.explicit_from_comparison(item, "offline_operation"), (None, None))


if __name__ == "__main__":
    unittest.main()
