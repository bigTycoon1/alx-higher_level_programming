#!/usr/bin/python3


"""This modeule return True/False. """


def is_same_class(obj, a_class):

    """ Function that returns True if obj is exactly,
    and False if otherwise.

    Args:
        obj: the object
        a_class: the class type

    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    return type(obj) is a_class
