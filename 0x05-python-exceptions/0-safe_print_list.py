#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        j = 0
        while i < x:
            print("{}".format(my_list[i]), end="")
            i += 1
            j + 1
        print()
        return j + 1
    except IndexError:
        print()
        return j