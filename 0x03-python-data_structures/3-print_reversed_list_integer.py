def print_reversed_list_integer(my_list=[]):
    for num in range(len(my_list) - 1, -1, -1):
        if isinstance(my_list[num], int):
            print("{:d}".format(my_list[num]))
