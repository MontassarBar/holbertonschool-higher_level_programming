#!/usr/bin/python3
'''a simple class'''


from pyrsistent import v


class BaseGeometry:
    '''BaseGeometry class'''
    def area(self):
        ''' raises an Exception with the message area() is not implemented '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        raise a TypeError exception, with the message <name> must be an integer
        raise a ValueError exception with the message <name> must be greater
         than 0
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
