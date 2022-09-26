#!/usr/bin/python3
"""My list Module"""


class MyList(list):
    """Write a class MyList that inherits from list"""
    def print_sorted(self):
        for i in self:
            if type(i) is not int:
                raise TypeError("all the values of the list must be integers")
        print(sorted(self))
