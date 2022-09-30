#!/usr/bin/python3
"""Rectangle Module"""
from .base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def get_width(self):
        return self.__width

    @property
    def get_height(self):
        return self.__height

    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y

    @get_width.setter
    def get_width(self, value):
        self.__width = value

    @get_height.setter
    def get_height(self, value):
        self.__height = value

    @get_x.setter
    def get_x(self, value):
        self.__x = value

    @get_y.setter
    def get_y(self, value):
        self.__y = value
