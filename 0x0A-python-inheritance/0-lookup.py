#!/usr/bin/python3
def lookup(obj):
    """ function that returns the list of available attributes
        and methods of an object

    Args:
        obj: class instance

    Returns: a list object
    """

    return dir(obj)
