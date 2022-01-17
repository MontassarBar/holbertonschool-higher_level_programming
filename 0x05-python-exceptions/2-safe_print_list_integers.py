#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    q = 0
    while j < x:
        try:
            print("{:d}".format(my_list[j]), end="")
            j += 1
            q += 1
        except ValueError:
            j += 1
        except TypeError:
            j += 1
    print()
    return q
