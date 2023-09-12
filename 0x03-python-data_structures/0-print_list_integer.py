#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in range(len(my_list)):
        if type(my_list[num]) == int:
            print("{:d}".format(my_list[num]))
