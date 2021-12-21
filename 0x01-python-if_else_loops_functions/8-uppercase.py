#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in range(0, len(str)):
        print("{}".format(
            chr(ord(str[i]) - 32) if ord(str[i]) >= 97 and ord(
                str[i]) <= 123 else chr(ord(str[i]))), end="")
    print()
