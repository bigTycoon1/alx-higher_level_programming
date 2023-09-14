#!/usr/bin/python3
def number_keys(a_dictionary):
    total_num = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        total_num = total_num + 1

    return (total_num)
