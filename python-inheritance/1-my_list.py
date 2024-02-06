#!/usr/bin/python3
"""
Sorting list with inheritence
"""


class MyList(list):
    """
    Class of list
    """

    def print_sorted(self):
        n_list = self[:]
        return n_list.sort()
