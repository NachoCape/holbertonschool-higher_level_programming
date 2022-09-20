#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """init method"""
        if isinstance(size, int):
            self.size = size

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the new size"""
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance area"""
        return self.__size ** 2
