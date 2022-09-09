#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_of_argv = len(sys.argv) - 1
    if len_of_argv == 0:
        print("0 arguments.")
    elif len_of_argv == 1:
        print("1 argument:")
        print("1: {:d}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len_of_argv))
        for i in range(len_of_argv):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
