#!/usr/bin/python3
"""
Write in python
"""


def write_file(filename="", text=""):
    """
    Function of write
    """
    with open(filename, 'w', encoding="utf-8") as wf:
        nw = wf.write(str(text))

    return nw
