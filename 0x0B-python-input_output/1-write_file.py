#!/usr/bin/python3
"""Defines a functtion of file-writing."""


def write_file(filename="", text=""):
    """Write a str to a UTF8 text file.

    Args:
        filename (str): name of the file to write.
        text (str): text to write to the file.
    Returns:
        the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
