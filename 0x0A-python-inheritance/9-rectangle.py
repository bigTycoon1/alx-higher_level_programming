#!/usr/bin/python3


"""Module that write the class that inhetits BaseGeo. """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Function that defines a rectangle from BaseGeometry Class """

    def __init__(self, width, height):

        """ Initialize instance """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):

        """ Method that returns the area of the instance"""

        return self.__width * self.__height

    def __str__(self):

        """ Special method that returns the printable string """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
