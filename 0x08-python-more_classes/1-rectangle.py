#!/usr/bin/python3
'''a simple class'''


class Rectangle:
    '''a simple Rectangle'''
    def __init__(self, width=0, height=0):
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
    '''property'''
    @property
    def height(self):
        return self.__height
    '''setter'''
    @height.setter
    def height(self, value):
        self.__height = value
    '''property'''
    @property
    def width(self):
        return self.__width
    '''setter'''
    @width.setter
    def width(self, value):
        self.__width = value
