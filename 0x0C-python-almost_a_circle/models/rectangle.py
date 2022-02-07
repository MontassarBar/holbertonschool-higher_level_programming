#!/usr/bin/python3
'''Rectangle class'''
from ast import arg
from models.base import Base


class Rectangle(Base):
    '''
    - Private instance attributes, each with its own public getter and setter:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''the area of a rectangle'''
        return self.__width * self.__height

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        for x in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for y in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''returns [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        else:
            for key in kwargs.keys():
                if key == "id":
                    self.id = kwargs["id"]
                if key == "height":
                    self.__height = kwargs["height"]
                if key == "width":
                    self.__width = kwargs["width"]
                if key == "x":
                    self.__x = kwargs["x"]
                if key == "y":
                    self.__y = kwargs["y"]
