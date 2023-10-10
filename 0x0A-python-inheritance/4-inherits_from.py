#!/usr/bin/python3


"""This module return True/False of an obj """


def inherits_from(obj, a_class):
    """ Function that returns True/False if obj is an instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False, if otherwise.
    """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
