#!/usr/bin/python3

""" square class to be defined"""

class Square:
    """square class to be represented"""

    def __init__(self, size=0):
        """initializing a new square by,
        (int) size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
