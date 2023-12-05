#!/usr/bin/python3
"""Defines function of a string-to-JSON."""
import json


def to_json_string(my_obj):
    """Return the JSON repr of a str object."""
    return json.dumps(my_obj)
