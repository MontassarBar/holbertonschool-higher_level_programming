#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nl = [None] * len(my_list)
    for i in range(0, len(my_list)):
        nl[i] = my_list[i]
        if nl[i] == search:
            nl[i] = replace
    return nl
