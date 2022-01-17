#!/usr/bin/python3
from ast import Return


def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        print()
        return i + 1
    except IndexError:
        print()
        return i
