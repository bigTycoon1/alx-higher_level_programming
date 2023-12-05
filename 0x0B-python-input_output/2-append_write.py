#!/usr/bin/python3
"""Defines a function of file-appending."""


def append_write(filename="", text=""):
    """Appends a str at the end of a UTF8 text file.

    Args:
        filename (str): name of the file to append to.
        text (str): str to append to the file.
    Returns:
        number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
