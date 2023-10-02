#!/usr/bin/python3

"""
Class of rectangle should be defined


"""

class Rectangle:
    """ Class rectangle """

    def __init__(self, width=0, height=0):
        """ initializes the instance """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ value of the width to return"""

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width """

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
        """ defines the height value """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
