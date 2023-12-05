#!/usr/bin/python3
"""Function that defines a Python class-to-JSON python."""


def class_to_json(obj):
    """Return the dictionary repr of a simple data structure."""
    return obj.__dict__
