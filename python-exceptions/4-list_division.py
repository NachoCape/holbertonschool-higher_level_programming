#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
                div = my_list_1[i] / my_list_2[i]
                res.append(div)
        except ZeroDivisionError:
            res.append(0)
            print("division by 0")
            continue
        except TypeError:
            res.append(0)
            print("wrong type")
            continue
        except IndexError:
            res.append(0)
            print("out of range")
            continue
        finally:
            pass
    return res
