#!/bin/usr/python3
def add_integer(a, b=98):
    if isinstance(a, int) or isinstance(a, float):
        a = round(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, int) or isinstance(b, float):
        b = round(b)
    else:
        raise TypeError("b must be an integer")
    return a + b
