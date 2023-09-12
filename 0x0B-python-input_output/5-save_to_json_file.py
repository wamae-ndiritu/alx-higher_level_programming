#!/usr/bin/python3
"""
This module defines function save_to_json_file
that writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Dumps an object to a text file

    Args:
        my_obj (obj): The object to be written to a file
        filename (str): The file to be written

    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
