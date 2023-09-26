#!/usr/bin/python3
""" class square to be define"""


class Square:
    """square class to be represented"""

    def __init__(self, size=0):
        """initialing a latest square,
        (int) size """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        """return the new located area"""
        return (self.__size * self.__size)
