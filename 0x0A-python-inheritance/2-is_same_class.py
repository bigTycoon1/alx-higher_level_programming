#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ Function that returns True if obj is an instance,
        Otherwise, False

    Args:
        obj: object
        a_class: class type

    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    return type(obj) is a_class
