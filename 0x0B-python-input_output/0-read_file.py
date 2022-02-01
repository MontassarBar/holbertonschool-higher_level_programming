#!/usr/bin/python3
'''reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    '''
    the "with" statement will close the file
    '''
    with open(filename, encoding="utf-8") as MyFile:
        print(MyFile.read())
