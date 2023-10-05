#!/usr/bin/python3
"""

class that defines a Rectangle


"""


class Rectangle:
    """ Class of rectangle to be defined """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ function that initializes the instance

        Args:
            width: rectangle width
            height: rectangle height


        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """function that def the value of the width """

        return self.__width

    @width.setter
    def width(self, value):
        """ function that defines the width

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
        """ functions that returns the value of the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """ fuction that defines the height

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
        """ function that calculates the Rectangle area """

        return self.width * self.height

    def perimeter(self):
        """ functions that calculates the perimeter of Rectangle """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ functions that returns the Rectangle str# """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ function that returns the str represantion of the instance """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ functions that prints a message when the instance is deleted """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
