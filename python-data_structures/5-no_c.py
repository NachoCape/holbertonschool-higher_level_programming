#!/usr/bin/python3
def no_c(my_string):
    arr = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            arr = arr + i
    return arr
