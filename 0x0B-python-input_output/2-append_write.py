#!/usr/bin/python3
'''appends a string at the end of a text file (UTF8)
and returns the number of characters added'''


def append_write(filename="", text=""):
    '''
    - the "with" statement will close the file
    - create the file if doesn't exist
    '''
    with open(filename, mode="a", encoding="utf-8") as MyFile:
        MyFile.write(text)
    return len(text)
