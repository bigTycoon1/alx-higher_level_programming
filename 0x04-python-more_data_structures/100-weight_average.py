#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

   total_num = 0
    total_scr = 0

    for tip in my_list:
        total_num += tip[0] * tip[1]
        total_scr += tip[1]
