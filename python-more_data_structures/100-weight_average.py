#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    div = 0
    if not my_list:
        return 0
    for i in my_list:
        sum += i[0] * i[1]
        div += i[1]
    if div == 0:
        return 0
    return sum / div
