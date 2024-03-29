#!/usr/bin/python3
"""
Load Add Save
"""

import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


fname = "add_item.json"

if os.path.isfile(fname):
    ls = load_from_json_file(fname)
else:
    ls = []

ls.extend(sys.argv[1:])
save_to_json_file(ls, fname)
