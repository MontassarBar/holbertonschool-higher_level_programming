#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    a = list((dir(hidden_4)))
    for i in range(1, len(a)):
        if a[i][0] in "abcdefghijklmnopqrstuvwxyz":
            print("{}".format(a[i]))
