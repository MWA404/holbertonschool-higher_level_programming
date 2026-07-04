#!/usr/bin/python3
"""This module defines CSV to JSON conversion function."""
import csv
import json


def convert_csv_to_json(csv_file):
    """Convert CSV file to JSON and save to data.json."""
    try:
        with open(csv_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        return True
    except FileNotFoundError:
        return False
