#!/usr/bin/python3
def remove_char_at(str, n):
    node = ""
    for x in range(len(str)):
        if x != n:
            node += str[x]
    return (node)
