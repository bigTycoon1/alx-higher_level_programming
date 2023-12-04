#!/usr/bin/python3
class MyList(list):
    """ class MyList that inherits from list:

    Args:
        list: a class list

    """

    def print_sorted(self):
        """ Method that prints a list but sorted """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
