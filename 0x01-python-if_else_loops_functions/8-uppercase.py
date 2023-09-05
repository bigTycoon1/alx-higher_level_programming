#!/usr/bin/python3
def uppercase(str):
    for results in range(len(str)):
        if ord(str[results]) >= 97 and ord(str[results]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[results]) - num), end='')
    print()
