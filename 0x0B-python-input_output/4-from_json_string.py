#!/usr/bin/python3


"""Modules that defines a JSON-to-object function."""


import json


def from_json_string(my_str):

    """Return the object that rep a JSON string."""

    return json.loads(my_str)
