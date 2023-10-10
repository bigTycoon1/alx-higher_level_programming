#!/usr/bin/python3


""" Module that defines a text file-reading function. """


def read_file(filename=""):

    """ Function that print the contents of a UTF8 text file to stdout."""

    with open(filename, encoding="utf-8") as f:

        print(f.read(), end="")
