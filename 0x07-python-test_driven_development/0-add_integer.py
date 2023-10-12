#!/usr/bin/python3


"""this module write a function that add an int."""


def add_integer(a, b=98):

    """function that define integer addition of a and b.

    Float arguments are typecasted to integer,
    before the addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
