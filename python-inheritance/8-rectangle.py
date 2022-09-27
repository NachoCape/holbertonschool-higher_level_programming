#!/usr/bin/python3
"""Write an empty class BaseGeometry"""


class BaseGeometry():
    """class BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Create a Rectangle"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(Rectangle, "width", width)
        BaseGeometry.integer_validator(Rectangle, "height", height)
        self.__width = width
        self.__height = height
