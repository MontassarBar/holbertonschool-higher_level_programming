#!/usr/bin/python3
'''a square'''


class Square:
    '''Size validation'''
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple\
            or len(position) != 2 or type(position[0]) is not int\
                or type(position[1]) is not int or position[0] < 0\
                or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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
    '''property'''
    @property
    def position(self):
        return self.__position
    '''setter'''
    @position.setter
    def position(self, position):
        if len(position) != 2\
             or type(position[0]) is not int or type(position[1]) is not int\
                or position[0] < 0 or position[1] < 0 or\
                type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
    '''Area of a square'''
    def area(self):
        return self.__size * self.__size
    '''print a square'''
    def my_print(self):
        if self.__size != 0:
            for x in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for y in range(0, self.__position[0]):
                    print("{}".format(" "), end="")
                for j in range(0, self.__size):
                    print("{}".format("#"), end="")
                print()
        else:
            print()
