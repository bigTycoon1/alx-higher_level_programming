#!/usr/bin/python3


"""This module inherit list"""


class MyList(list):

    """ Class that inherits list attribute."""

    def print_sorted(self):

        """ Function that prints the sorted list """

        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
