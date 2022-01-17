#!/usr/bin/python3
from multiprocessing.sharedctypes import Value


def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except ValueError:
            j = j - 1
        except TypeError:
            j = j - 1
    print()
    return j + i + 1