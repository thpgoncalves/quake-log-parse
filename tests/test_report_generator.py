import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from report_generator import ReportGenerator
import unittest

class TestReportGenerator(unittest.TestCase):
    def test_generate_report(self):
        games = {
            "game_1": {
                "total_kills": 2,
                "players": {"Isgalamido", "Dono da Bola"},
                "kills": {"Isgalamido": 1, "Dono da Bola": 0},
                "kills_by_means": {"MOD_RAILGUN": 1, "MOD_TRIGGER_HURT": 1}
            }
        }
        report_generator = ReportGenerator(games)
        report = report_generator.generate_report()
        self.assertEqual(report["game_1"]["total_kills"], 2)
        self.assertCountEqual(report["game_1"]["players"], ["Isgalamido", "Dono da Bola"])

if __name__ == "__main__":
    unittest.main()