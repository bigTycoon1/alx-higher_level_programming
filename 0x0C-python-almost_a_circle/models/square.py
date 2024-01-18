#!/usr/bin/python3


<<<<<<< HEAD
""" Module that contains class of Square, frm Rectangle """
=======
""" Module contain the class Square """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927

from models.rectangle import Rectangle


class Square(Rectangle):
<<<<<<< HEAD
    """ Class of Sqr frm Rectangle """
=======
    """ Square class frm Rectangle """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927

    def __init__(self, size, x=0, y=0, id=None):
        """ Instance to initializes """
        super().__init__(size, size, x, y, id)

    def __str__(self):
<<<<<<< HEAD
        """ the  str method (special) """
=======
        """ str  method (special)"""
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh

    @property
    def size(self):
        """ get the size """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size """
        self.width = value
        self.height = value

    def __str__(self):
<<<<<<< HEAD
        """ str method """
=======
        """ str  method """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
<<<<<<< HEAD
        """method to update """
=======
        """ method to update """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
<<<<<<< HEAD
        """ Function to returns a dict with attr """
=======
        """ Function to Returns a dict with attr """
>>>>>>> 88dac1071010022a96e0b707f37f7b844c32b927
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
