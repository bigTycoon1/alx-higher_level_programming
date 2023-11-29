#!/usr/bin/python3


"""The module of class that defines a Rectangle."""


class Rectangle:
    """ Class that def a rectangle """

    def __init__(self, width=0, height=0):
        """ Instance to be init.

        Args:
            width: width
            height: height


        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Function that returns the value of the width

        Returns:
            width of the rectangle


        """

        return self.__width

    @width.setter
    def width(self, value):
        """ function that defines the width set.

        Args:
            value: width

        Raises:
            TypeError: if width is not an int
            ValueError: if width is < 0


        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Function that returns the value of the height

        Returns:
            height of the rectangle


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ function that defines the height set.

        Args:
            value: height

        Raises:
            TypeError: if height is not an int
            ValueError: if height is < 0.


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
