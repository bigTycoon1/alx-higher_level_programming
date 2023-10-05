#!/usr/bin/python3
"""

The class of a Rectangle is defined

"""


class Rectangle:
    """ Class rectangle is defined """

    def __init__(self, width=0, height=0):
        """ instances of a rectangle is initializes.

        Args:
            width: rect width
            height: rectangle height


        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns the value of the width """

        return self.__width

    @width.setter
    def width(self, value):
        """ rectangle width is defined

        Args:
            value: width

        Raise:
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
        """ value of the height is define """

        return self.__height

    @height.setter
    def height(self, value):
        """ defines the height

        Args:
            value: height

        Raise:
            TypeError: if height is not an int
            ValueError: if height is < 0


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates the Rectangle area """

        return self.width * self.height

    def perimeter(self):
        """ calculates the Rectangle perimeter """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ Method that returns the Rectangle str# """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]
