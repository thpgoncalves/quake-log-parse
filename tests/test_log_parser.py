import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from log_parser import LogParser
import unittest

class TestLogParser(unittest.TestCase):
    def setUp(self):
        with open("test_log.log", "w") as f:
            f.write(" 0:00 InitGame:\n")
            f.write(" 1:00 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT\n")
            f.write(" 2:00 Kill: 2 3 10: Isgalamido killed Dono da Bola by MOD_RAILGUN\n")
            f.write(" 3:00 ShutdownGame:\n")

        self.log_parser = LogParser("test_log.log")
        self.log_parser.parse_log()

    def test_total_kills(self):
        games = self.log_parser.get_games()
        print(games)
        self.assertEqual(games["game_1"]["total_kills"], 2)

    def test_player_kills(self):
        games = self.log_parser.get_games()
        print(games)
        self.assertEqual(games["game_1"]["kills"]["Isgalamido"], 1)
        self.assertEqual(games["game_1"]["kills"]["Dono da Bola"], 0)

    def tearDown(self):
        os.remove("test_log.log")

if __name__ == "__main__":
    unittest.main()