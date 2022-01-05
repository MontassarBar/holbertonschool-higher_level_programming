#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    o = set(my_list)
    p = (list(o))
    for i in range(0, len(p)):
        x += p[i]
    return x
