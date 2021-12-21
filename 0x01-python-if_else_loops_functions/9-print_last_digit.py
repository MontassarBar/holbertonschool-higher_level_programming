#!/usr/bin/python3
def print_last_digit(number):
    n = int
    if number >= 0:
        n = number % 10
        print(n, end="")
        return n
    else:
        n = (number * -1) % 10
        print(n, end="")
        return n
