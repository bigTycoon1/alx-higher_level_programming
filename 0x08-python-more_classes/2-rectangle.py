#!/usr/bin/python3


"""The module that def a class of  a Rectangle."""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Instance to be initializes

        Args:
            width: width
            height: height


        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Function that returns value of the width

        Returns:
            width of a rectangle


        """

        return self.__width

    @width.setter
    def width(self, value):
        """ Functon that define the width set.

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
        """ Function that returns value of the height

        Returns:
            height of a rectangle


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Function that defines the height set.

        Args:
            value: height

        Raises:
            TypeError: if height is not an int
            ValueError: if height is < 0


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Function that calc the Rectangle area

        Returns:
            rectangle area


        """

        return self.width * self.height

    def perimeter(self):
        """ Function that calculates the Rectangle perimeter

        Returns:
            rectangle perimeter


        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)
