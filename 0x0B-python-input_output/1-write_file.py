#!/usr/bin/python3


"""module that defines a file-writing function."""


def write_file(filename="", text=""):

    """Function to write a string to a UTF8 text file.

    Args:
        filename: str
        text (str): text to write inside file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
