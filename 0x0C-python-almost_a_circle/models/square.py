#!/usr/bin/python3
'''Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' super class with id, x, y, width and height'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __Str__(self):
        '''return [Square] (<id>) <x>/<y> - <size>'''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.height)
