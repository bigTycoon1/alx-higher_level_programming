#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class
[2;2R[>77;30604;0c]10;rgb:bfbf/bfbf/bfbf]11;rgb:0000/0000/0000
a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

