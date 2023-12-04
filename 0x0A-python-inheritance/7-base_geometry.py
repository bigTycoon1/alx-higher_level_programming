#!/usr/bin/python3
class BaseGeometry:
    """ Class that defines Base of Geometric """

    def area(self):
        """ method that defines the area of a geomtric base """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that recieves the property value

        Args:
            name: object name
            value: property value

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
