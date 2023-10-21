#!/usr/bin/python3


"""To define a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print names.

    Args:
        first_name (str): The 1st name
        last_name (str): The last name
    Raises:
        TypeError: Only if either the  first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
