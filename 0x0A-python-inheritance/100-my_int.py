#!/usr/bin/python3


""" Module that write a class MyInt that inherits from int."""


class MyInt(int):

    """ Class that inherits from class int"""

    def __eq__(self, other):

        """ returns != check """

        return int.__ne__(self, other)

    def __ne__(self, other):

        """ func that returns == check """

        return int.__eq__(self, other)
