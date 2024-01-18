#!/usr/bin/python3
<<<<<<< HEAD


""" Module that contain class 0f Rectangle frm Base """

=======
""" Module that create class Rectangle,
and inherits of class Base
"""
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
from models.base import Base


class Rectangle(Base):
<<<<<<< HEAD
    """ Class Base of Rectangle """
=======
    """ Class of Rectangle """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instance to initializes """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
        """ get height """
=======
        """ get the height """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
<<<<<<< HEAD
        """ get the x  """
=======
        """ get x value """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        return self.__x

    @x.setter
    def x(self, value):
<<<<<<< HEAD
        """ set the x """
=======
        """ set the x value """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
<<<<<<< HEAD
        """ get the y """
=======
        """ get y value """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        return self.__y

    @y.setter
    def y(self, value):
<<<<<<< HEAD
        """ set y """
=======
        """ set y value"""
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
<<<<<<< HEAD
        """ function that return the area of the rectangle obj """
=======
        """ returns the area of rectangle """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        return self.width * self.height

    def display(self):
        """ displays a rectangle """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
<<<<<<< HEAD
        """  a str method (special) """
=======
        """ str method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
<<<<<<< HEAD
        """ function method to update """
=======
        """ update method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
<<<<<<< HEAD
        """ method to return a dict with properties """
=======
        """ method to returns a dict with properties """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
