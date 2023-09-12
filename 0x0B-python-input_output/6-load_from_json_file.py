#!/usr/bin/python3
"""
This module defines function load_from_json_file
that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Loads an object from a json file

    Args:
        filename (str): The file consisiting the object

    Returns:
        (obj): returns an object from a JSON file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
