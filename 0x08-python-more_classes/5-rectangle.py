#!/usr/bin/python3


""" The Module that defines a class Rectangle."""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """Instance to initializes

        Args:
            width: rectangle width
            height: rectangle height


        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Function that returns value of the width

        Returns:
            rectangle width


        """

        return self.__width

    @width.setter
    def width(self, value):
        """ Function that defines the width

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
        """ Functionthat returns the value of the height

        Returns:
            rectangle height


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Function that defines the height

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
        """Function that calc the Rectangle perimeter

        Returns:
            rectangle perimeter


        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """Function that returns the Rectangle #

        Returns:
            str of the rectangle

        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ function that return str repr of the instance

        Returns:
            str repr of the object

        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ funtion that prints a messg when the instance is del


        """

        print("Bye rectangle...")
