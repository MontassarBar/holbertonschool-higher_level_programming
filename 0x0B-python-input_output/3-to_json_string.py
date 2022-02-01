#!/usr/bin/python3
'''returns the JSON representation of an object (string)'''


import json


def to_json_string(my_obj):
    '''JSON'''
    new_string = json.dumps(my_obj)
    return new_string
