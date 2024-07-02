from log_parser import LogParser
from report_generator import ReportGenerator

if __name__ == "__main__":
    log_parser = LogParser("games.log")
    log_parser.parse_log()

    report_generator = ReportGenerator(log_parser.get_games())
    report_generator.print_report()
    report_generator.save_report("games_report.json")
