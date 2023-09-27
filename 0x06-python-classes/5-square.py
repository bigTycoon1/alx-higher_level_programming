#!/usr/bin/python3
"""class Square to be define"""


class Square:
    """class of a square to be represent"""

    def __init__(self, size):
        """to initialize a new square by,
        (int) size """
        self.size = size

    @property
    def size(self):
        """locate size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area location of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """ square size with the # char to be printed."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
