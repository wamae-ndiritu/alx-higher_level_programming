#!/usr/bin/python3
"""
The module defines a function
that returns the JSON representation of an object(string)
"""
import json


def to_json_string(my_obj):
    """
    Represents an obje to JSON obj

    Args:
        my_obj (str): any string object in python

    Returns:
        (json obj): returnns a JSON representation of an object
    """
    return json.dumps(my_obj)
