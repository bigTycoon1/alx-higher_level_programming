#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that defines a BaseGeometry rectangle class """

    def __init__(self, width, height):
        """ Initializes an instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
