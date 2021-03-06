#!/usr/bin/python3
'''a square'''


class Square:
    '''Size validation'''
    def __init__(self, size=0):
        self.size = size
    '''property'''
    @property
    def size(self):
        return self.__size
    '''setter'''
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    '''Area of a square'''
    def area(self):
        return self.__size * self.__size
