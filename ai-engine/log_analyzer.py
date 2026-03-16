import os
import json
import logging
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogAnalyzer:
    def __init__(self, log_path="/var/log/application.log"):
        self.log_path = log_path
        self.error_patterns = ["Exception", "Error", "Timeout", "Failed"]
        self.stats = defaultdict(int)

    def analyze(self):
        logging.info(f"Starting analysis of {self.log_path}...")
        try:
            with open(self.log_path, 'r') as f:
                for line in f:
                    self._parse_line(line)
            return self.stats
        except FileNotFoundError:
            logging.error(f"Log file {self.log_path} not found.")
            return None

    def _parse_line(self, line):
        for pattern in self.error_patterns:
            if pattern.lower() in line.lower():
                self.stats[pattern] += 1

if __name__ == "__main__":
    analyzer = LogAnalyzer()
    stats = analyzer.analyze()
    print(f"Analysis Results: {json.dumps(stats, indent=2)}")
