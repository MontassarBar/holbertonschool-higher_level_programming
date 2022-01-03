#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        ll = [None] * len(my_list)
        for i in range(0, len(my_list)):
            ll[i] = my_list[i]
        ll[idx] = element
        return ll
