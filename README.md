# qa-engineer-test
## Instructions
This repository already contains the finished program and the final file named "games_report.json".

Run pip "pip install -r requirements.txt" in the terminal before using the code.

I had problems with 1 of the 3 tests I created which I couldn't solve, but the file is running perfectly and generating the expected results. To run the tests and understand the problem, just type "pytest" in the terminal.

I created the logic in separate files to make it easier to maintain and debug if necessary. 

The log that was used to generate the information was named "games.log".

To run the file and create "games_report.json", just run "main.py" in the terminal or in vscode.

## Test Requirements
*Log parser:*
- Read the log file (Done)
- Group the game data of each match (Done)
- Collect kill data (Done)

*Report:*
- Create a script that prints a report (grouped information) for each match and a player ranking (Done)

*Plus:*
- Generate a report of deaths grouped by death cause for each match. (Done in the same file as the report)
