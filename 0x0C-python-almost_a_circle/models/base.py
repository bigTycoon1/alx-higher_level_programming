#!/usr/bin/python3


"""The module that contain the Base Class"""


import json
import os.path


class Base:

    """ base of the class """

    __nb_objects = 0

    def __init__(self, id=None):

        """ Initialize the  instances """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        """ list dict to JSON string """

        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        """ Save the list object to a file """

        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as file:
            file.write(lists)

    @staticmethod
    def from_json_string(json_string):

        """ from JSON string to dict """

        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """ to create an instance """

        if cls.__name__ == "Rectangle":
            inst = cls(10, 10)
        else:
            inst = cls(10)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):

        """ returns list of instances """

        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as file:
            list_str = file.read()

        list_cls = cls.from_json_string(list_str)
        list_inst = []

        for index in range(len(list_cls)):
            list_inst.append(cls.create(**list_cls[index]))

        return list_inst
