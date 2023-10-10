#!/usr/bin/python3


"""This module return True/False. """


def is_kind_of_class(obj, a_class):

    """ Function that returns True if exactly and,
    Fail if otherwise.

    Args:
        obj: the object
        a_class: the class

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
