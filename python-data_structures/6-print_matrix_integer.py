#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        j = 0
        while j <= len(i)-1:
            # if j == len(i)-1:
            # print("{:d}".format(i[j]), end="$")
            # else:
            print("{:d}".format(i[j]), end=" ")
            j += 1
        print("")
