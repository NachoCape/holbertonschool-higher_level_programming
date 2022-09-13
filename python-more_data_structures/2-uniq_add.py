#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    res = 0
    if len(my_list) == 2 and my_list[0] != my_list[1]:
        return my_list[0] + my_list[1]
    elif len(my_list) == 1:
        return my_list[0]
    else:
        for i in my_list:
            if i not in new_list:
                new_list.append(i)
        for j in new_list:
            res += j
        return res
