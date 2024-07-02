import json

class ReportGenerator:
    def __init__(self, games):
        self.games = games

    def generate_report(self):
        report = {}
        for game, data in self.games.items():
            report[game] = {
                "total_kills": data["total_kills"],
                "players": list(data["players"]),
                "kills": dict(data["kills"]),
                "kills_by_means": dict(data["kills_by_means"])
            }
        return report

    def print_report(self):
        report = self.generate_report()
        print(json.dumps(report, indent=4))

    def save_report(self, file_path):
        report = self.generate_report()
        with open(file_path, 'w') as file:
            json.dump(report, file, indent=4)
