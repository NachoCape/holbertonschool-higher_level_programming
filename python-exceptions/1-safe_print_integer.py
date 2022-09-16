#!/usr/bin/python
from operator import truediv


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    return True
