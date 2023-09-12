#!/usr/bin/python3
"""
The module defines a function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Takes an object (an instance of a class) and initializes a
    dictionary description of its attributes
    with sample data structure suitable for JSON serialization

    Args:
        obj (obj): An instance of a class to be converted to json

    Returns:
        (dict): description of the class attributes
    """
    serialized_data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_data[key] = value
    return serialized_data
