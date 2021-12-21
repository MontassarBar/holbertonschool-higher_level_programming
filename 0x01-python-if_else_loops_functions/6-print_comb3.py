#!/usr/bin/python3
for i in range(0, 9):
    for f in range(0, 10):
        if i < f and (i + f) < 17:
            print("{}".format(i), end="")
            print("{}, ".format(f), end="")
        elif i < f and (i + f) == 17:
            print("{}".format(i), end="")
            print("{}".format(f))
