#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    else:
        s = [None] * (len(my_list) - 1)
        j = 0
        for i in range(0, len(my_list)):
            if i != idx:
                s[j] = my_list[i]
                j += 1
        my_list = s
        return my_list
