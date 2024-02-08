#!/usr/bin/python3
"""
First read in py
"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as rf:
        print(rf.read())
