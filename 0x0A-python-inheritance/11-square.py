#!/usr/bin/python3
''' a simple class '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    size must be private. No getter or setter
    size must be a positive integer, validated by integer_validator
    '''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''return the area of the square'''
        return self.__size ** 2

    def __str__(self):
        '''returns [Square] <width>/<height>'''
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
