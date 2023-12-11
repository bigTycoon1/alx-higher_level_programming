#!/usr/bin/python3
<<<<<<< HEAD
""" Module that create a class Base """
=======


""" Module that contains base of class """
>>>>>>> 44775a1d1336c9aea28adfaec5a9674d363394a3
import json
import csv
import os.path


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
<<<<<<< HEAD
        """ Instance to be initializes """
=======
        """ Instance to Initialize """
>>>>>>> 44775a1d1336c9aea28adfaec5a9674d363394a3
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
<<<<<<< HEAD
        """ Lists of list to JSON str """
=======
        """ List dict to JSON str """
>>>>>>> 44775a1d1336c9aea28adfaec5a9674d363394a3
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
<<<<<<< HEAD
        """ Save to file obj """
=======
        """ List to save object to file """
>>>>>>> 44775a1d1336c9aea28adfaec5a9674d363394a3
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
<<<<<<< HEAD
        """ From JSON str to dict """
=======
        """ JSON str to dict """
>>>>>>> 44775a1d1336c9aea28adfaec5a9674d363394a3
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
<<<<<<< HEAD
        """ Instance that is created """
=======
        """ Create an instance """
>>>>>>> 44775a1d1336c9aea28adfaec5a9674d363394a3
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
<<<<<<< HEAD
        """ Returns an instances lists """
=======
        """ Returns list of an instances """
>>>>>>> 44775a1d1336c9aea28adfaec5a9674d363394a3
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
<<<<<<< HEAD
        """ Method that save ti file_csv """
=======
        """ Method that save a CSV file """
>>>>>>> 44775a1d1336c9aea28adfaec5a9674d363394a3
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
<<<<<<< HEAD
        """ Method that load from csv file """
=======
        """ Method that loads a CSV file """
>>>>>>> 44775a1d1336c9aea28adfaec5a9674d363394a3
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
