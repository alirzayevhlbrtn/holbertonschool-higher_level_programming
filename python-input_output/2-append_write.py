#!/usr/bin/python3
"""
Write in python
"""


def append_write(filename="", text=""):
    """
    Function of write
    """
    with open(filename, 'a', encoding="utf-8") as af:
        nw = af.write(str(text))

    return nw
