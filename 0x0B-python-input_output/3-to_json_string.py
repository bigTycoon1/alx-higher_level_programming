#!/usr/bin/python3


"""Modules that defines a string-to-JSON function."""


import json


def to_json_string(my_obj):

    """return thee JSON rep of a string object. """

    return json.dumps(my_obj)
