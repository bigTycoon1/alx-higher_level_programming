#!/usr/bin/python3


"""function that defines a name-printing."""


def say_my_name(first_name, last_name=""):
    """def name-printing.

    Args:
        first_name (str): 1st name to print.
        last_name (str):  last name to print.
    Raises:
        TypeError: If first_name and last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
