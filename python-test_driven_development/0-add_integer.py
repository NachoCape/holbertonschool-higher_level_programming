#!/usr/bin/python3
"""Write a function that adds 2 integers
    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    You are not allowed to import any module
        """


def add_integer(a, b=98):
    """add 2 integers"""
    if isinstance(a, int) or isinstance(a, float):
        a = round(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, int) or isinstance(b, float):
        b = round(b)
    else:
        raise TypeError("b must be an integer")
    return a + b
