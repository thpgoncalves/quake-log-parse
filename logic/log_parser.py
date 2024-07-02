import re
from collections import defaultdict

class LogParser:
    def __init__(self, log_file):
        self.log_file = log_file
        self.games = defaultdict(lambda: {
            "total_kills": 0,
            "players": set(),
            "kills": defaultdict(int),
            "kills_by_means": defaultdict(int)
        })
        self.current_game = None

    def parse_log(self):
        with open(self.log_file, 'r') as file:
            for line in file:
                self.parse_line(line)

    def parse_line(self, line):
        if "InitGame" in line:
            self.current_game = f"game_{len(self.games) + 1}"
        elif "ShutdownGame" in line:
            self.current_game = None
        elif "Kill:" in line and self.current_game:
            self.process_kill_line(line)

    def process_kill_line(self, line):
        match = re.search(r'Kill: \d+ \d+ \d+: (.*) killed (.*) by (.*)', line)
        if match:
            killer, killed, means = match.groups()
            killer = killer.strip()
            killed = killed.strip()
            means = means.strip()
            print(f"Processing kill line: killer={killer}, killed={killed}, means={means}")
            game_data = self.games[self.current_game]

            print(f"Before update: {game_data}")

            game_data["total_kills"] += 1
            game_data["kills_by_means"][means] += 1

            if killer != "<world>":
                game_data["players"].add(killer)
                game_data["kills"][killer] += 1
            else:
                game_data["kills"][killed] -= 1

            game_data["players"].add(killed)

            print(f"After update: {game_data}")

    def get_games(self):
        return self.games
