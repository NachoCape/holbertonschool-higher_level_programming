#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_of_argv = len(sys.argv) - 1
    res = 0
    for i in range(len_of_argv):
        res = res + int(sys.argv[i + 1])
    print("{}".format(res))
