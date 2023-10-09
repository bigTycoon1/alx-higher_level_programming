#!/usr/bin/python3
class MyList(list):
    """ Class that inherits list attribute.

    Args:
        list: list of the class

    """

    def print_sorted(self):
        """ Function that prints the sorted list """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
