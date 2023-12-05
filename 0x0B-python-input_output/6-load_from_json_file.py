#!/usr/bin/python3
"""Defines function of JSON file-reading."""
import json


def load_from_json_file(filename):
    """write object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
