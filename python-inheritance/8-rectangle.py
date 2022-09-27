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
