#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)

    if length == 0:
        return (None)

    max_int = my_list[0]

    for x in range(1, length):
        if my_list[x] > max_int:
            max_int = my_list[x]

    return (max_int)
