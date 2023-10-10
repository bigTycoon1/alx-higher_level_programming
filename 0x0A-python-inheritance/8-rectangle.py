#!/usr/bin/python3


""" The module that write class of BaseGeo. """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """ Function that defines a rectangle from BaseGeometry Class """

    def __init__(self, width, height):

        """ Initializes instance """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
