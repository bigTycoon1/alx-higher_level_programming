#!/usr/bin/python3


""" Module that contains class Rectangle. """


from models.base import Base


class Rectangle(Base):

    """ Class of Rectangle Base """

    def __init__(self, width, height, x=0, y=0, id=None):

        """ function that initializes instances """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):

        """ function that get width """

        return self.__width

    @width.setter
    def width(self, value):

        """ function to set width """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):

        """ function to get height """

        return self.__height

    @height.setter
    def height(self, value):

        """ fuction to set height """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):

        """function to get x """

        return self.__x

    @x.setter
    def x(self, value):

        """ x setter """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):

        """ y getter """

        return self.__y

    @y.setter
    def y(self, value):

        """ y setter """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):

        """ returns the area of the rectangle object """

        return self.width * self.height

    def display(self):

        """ displays a rectangle """

        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):

        """ str special method """

        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh
