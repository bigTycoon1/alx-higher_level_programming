#!/usr/bin/python3
"""

The class of rectangle is written.

"""


class Rectangle:
    """ Classof rectangle is defined """

    def __init__(self, width=0, height=0):
        """ instance to be initializes.

        Args:
            width: rect width
            height: rect height

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ value of the width to be def """

        return self.__width

    @width.setter
    def width(self, value):
        """ defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is < 0


        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ value of the height """

        return self.__height

    @height.setter
    def height(self, value):
        """ defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is > 0


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates the area of Rectangle """

        return self.width * self.height

    def perimeter(self):
        """ calculates perimeter of Rectangle """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ function that returns the Rectangle str#  """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ the string represantion """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)
