#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    total_num = 0

    for i in uniq_list:
        total_num = total_num + i

    return (total_num)
