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
    '''area of a Rectangle'''
    def area(self):
        return self.__height * self.__width
    '''perimeter of a Rectangle'''
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
    '''print a Rectangle'''
    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            return (('#' * self.__width) + '\n') * (
                self.__height - 1) + ('#' * self.__width)
        else:
            d = ""
            return d
    '''__repr__'''
    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ',' + str(
            self.__height) + ")"
