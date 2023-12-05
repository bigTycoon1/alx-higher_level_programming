#!/usr/bin/python3
"""Defines function of a text file-reading."""


def read_file(filename=""):
    """Function that read a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
