#!/usr/bin/python3
'''writes a string to a text file (UTF8)
and returns the number of characters written'''


def write_file(filename="", text=""):
    '''
    - the "with" statement will close the file
    - create the file if doesn’t exist
    - overwrite the content of the file if it already exists
    '''
    with open(filename, mode="w", encoding="utf-8") as MyFile:
        MyFile.write(text)
    return len(text)
