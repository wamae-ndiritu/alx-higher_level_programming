#!/usr/bin/python3
import json
"""
The module defines a function
that returns the JSON representation of an object(string)
"""


def to_json_string(my_obj):
    """
    Represents an obje to JSON obj

    Args:
        my_obj (str): any string object in python

    Returns:
        (json obj): returnns a JSON representation of an object
    """
    return json.dumps(my_obj)
