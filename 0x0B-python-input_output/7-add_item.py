#!/usr/bin/python3
"""
The script adds all arguments to a Python list,
and then save them to a file
"""
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# File path for the JSON file
json_file = os.path.join(os.getcwd(), 'add_item.json')

# Parse command-line arguments and add them to a list
args_list = sys.argv[1:]

# Load existing items from the JSON file if it exists
try:
    existing_items = load_from_json_file(json_file)
except FileNotFoundError:
    existing_items = []

# Add the command-line args to the list
existing_items.extend(args_list)

# Save the updated list to the JSON file
save_to_json_file(existing_items, json_file)
