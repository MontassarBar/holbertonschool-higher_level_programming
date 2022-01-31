#!/usr/bin/python3
'''a simple class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    width and height must be private. No getter or setter
    width and height must be positive integers, validated by integer_validator
    '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''returns the area of the Rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''returns [Rectangle] <width>/<height>'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
