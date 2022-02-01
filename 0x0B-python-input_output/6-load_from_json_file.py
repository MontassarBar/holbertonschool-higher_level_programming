#!/usr/bin/python3
'''creates an Object from a “JSON file”'''


import json


def load_from_json_file(filename):
    '''JSON'''
    with open(filename) as MyFile:
        return json.loads(MyFile.read())
