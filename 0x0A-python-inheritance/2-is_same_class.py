#!/usr/bin/python3
"""
Defines the is_same_class that checks
whether the object is exactly an instance of
the specified class
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: Represent the object to check
        a_class: a specified class
    Return:
        True: If obj is an instance of class a_class
        False: If obj is not an instance of a_class
    """

    return isinstance(obj, a_class) and a_class is not object
