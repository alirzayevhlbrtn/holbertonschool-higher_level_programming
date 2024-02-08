#!/usr/bin/python3
"""
Read json
"""


import json


def load_from_json_file(filename):
    """
    function read
    """
    with open(filename, 'r', encoding="utf-8") as jf:
        json.load(jf)
