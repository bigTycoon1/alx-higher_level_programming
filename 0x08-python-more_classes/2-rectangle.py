#!/usr/bin/python3
"""


class that defines a Rectangle


"""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ initializes the instance """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ defines the value of the width """

        return self.__width

    @width.setter
    def width(self, value):
        """ defines the width """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ define value of the height """

        return self.__height

    @height.setter
    def height(self, value):
        """ defines the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ define the rectangle area """

        return self.width * self.height

    def perimeter(self):
        """ define Rectangle perimeter """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)
