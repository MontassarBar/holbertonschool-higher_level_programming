#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except ValueError:
            j += 1
        except TypeError:
            j += 1
    print()
    if j >= 0:
        return (i + 1) - j
    else:
        return 0
