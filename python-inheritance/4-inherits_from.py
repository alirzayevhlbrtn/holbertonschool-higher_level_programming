#!/usr/bin/python3
"""
Function of checker
"""


def inherits_from(obj, a_class):
    """
    Function checks
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
