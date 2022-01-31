#!/usr/bin/python3
''' a simple class '''


class MyList(list):
    '''inheritance'''

    def print_sorted(self):
        print(sorted(self))
