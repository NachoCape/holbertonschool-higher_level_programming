#!/usr/bin/python3
"""
    Load, add, save Module
    adds all arguments to a Python list, and then save them to a file
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list = []
filename = "add_item.json"
list = load_from_json_file(filename)
for i in range(1, len(sys.argv) - 1):
    list = save_to_json_file(i, filename)
