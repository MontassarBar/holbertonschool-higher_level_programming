#!/usr/bin/python3
'''a simple module '''


def is_kind_of_class(obj, a_class):
    ''' returns True if the object is an instance of,
     or if the object is an instance of a class that inherited from,
      the specified class otherwise False'''
    result = isinstance(obj, a_class)
    return result
