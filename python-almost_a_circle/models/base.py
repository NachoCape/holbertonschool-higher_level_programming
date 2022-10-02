#!/usr/bin/python3
"""Class Base Module"""

import json


class Base:
    """This class will be the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        lis = []
        if list_objs:
            for i in list_objs:
                lis.append(i.to_dictionary())
        with open(filename, "w") as f:
            f.write(Base.to_json_string(lis))
