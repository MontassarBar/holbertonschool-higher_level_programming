#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ff = [None] * len(my_list)
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            ff[i] = True
        else:
            ff[i] = False
    return ff
