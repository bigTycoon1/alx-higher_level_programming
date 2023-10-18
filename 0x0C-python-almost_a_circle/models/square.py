#!/usr/bin/python3


""" Module that contains class of Square """


from models.rectangle import Rectangle


class Square(Rectangle):

    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):

        """ Initializing the instances """

        super().__init__(size, size, x, y, id)

    def __str__(self):

        """ string method """

        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh

    @property
    def size(self):

        """ Get size """

        return self.width

    @size.setter
    def size(self, value):

        """ Set size """

        self.width = value
        self.height = value

    def __str__(self):

        """ string  method """

        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size

    def update(self, *args, **kwargs):

        """ updating method """

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

        """ returns a dictionary and the value """

        list_atr = ['id', 'size', 'x', 'y']
        dict_result = {}

        for key in list_atr:
            if key == 'size':
                dict_result[key] = getattr(self, 'width')
            else:
                dict_result[key] = getattr(self, key)

        return dict_result
