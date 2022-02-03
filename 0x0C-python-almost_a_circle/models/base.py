#!/usr/bin/python3
'''Base class'''


class Base:
    '''
    - private class attribute: nb_objects
    - public instance attribute: id
    - if id is not None, assign id with this argument value
    - otherwise, increment __nb_objects and assign the new value to id
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
