#!/usr/bin/python3
"""Rectangle Module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Create a Rectangle"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(Rectangle, "width", width)
        BaseGeometry.integer_validator(Rectangle, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
