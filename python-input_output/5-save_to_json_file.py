#!/usr/bin/python3
"""
Save json
"""


import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as jf:
        jf.dump(my_obj, jf)
