#!/usr/bin/python3
"""Defines function of JSON-to-object."""
import json


def from_json_string(my_str):
    """Return an object(python data structure) repr by JSON str."""
    return json.loads(my_str)
