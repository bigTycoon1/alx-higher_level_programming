#!/usr/bin/python3
"""square class to be define"""

class Square:
    """square class to be represnted"""

    def __init__(self, size=0):
        """to initialize the new square,
        (int) size"""

        self.size = size

    @property
    def size(self):
        """the new located size of the square."""

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return location of curent size"""

        return (self.__size * self.__size)
