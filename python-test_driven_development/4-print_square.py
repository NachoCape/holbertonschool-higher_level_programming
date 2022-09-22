#!/usr/bin/python3
"""print_square module"""


def print_square(size):
    """Write a function that prints a square with the character #"""
    if type(size) is int or type(size) is float:
        size = round(size)
    else:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end="")
    else:
        for i in range(0, size):
            for j in range(0, size):
                if j == size - 1:
                    print("#")
                else:
                    print("#", end="")
