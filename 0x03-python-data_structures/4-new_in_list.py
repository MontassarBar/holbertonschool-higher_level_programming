#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ll = my_list
    if idx < 0:
        return ll
    if idx > len(my_list):
        return ll
    ll[idx] = element
    return ll
