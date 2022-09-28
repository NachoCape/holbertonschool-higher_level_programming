#!/usr/bin/python3
"""Student to JSON with filter Module"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if type(attrs) is list:
            attr = {}
            for i in attrs:
                if hasattr(self, i):
                    attr[i] = getattr(self, i)
            return attr
