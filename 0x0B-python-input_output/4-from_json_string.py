#!/usr/bin/python3
"""
This module defines function from_json_string
that returns an object represented by JSON string
"""
import json


def from_json_string(my_str):
    """
    Converts a string to object represented by JSON

    Args:
        my_str (str): The string to be converted

    Returns:
        (obj): Python object represented in JSON

    """
    return json.loads(my_str)
