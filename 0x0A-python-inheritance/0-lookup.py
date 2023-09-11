#!usr/bin/python3
"""
Defines a function that returns a list of
available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns list of available attributes and methods of obj
    """
    return dir(obj)
