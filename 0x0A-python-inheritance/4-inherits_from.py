#!/usr/bin/python3
"""
Defines a function to check whether an object is a an instance
of only the sub class of the specified class
"""


def inherits_from(obj, a_class):
    """
    Check if is instance of only sub class of a specified class

    Args:
        obj (object): any item to be checked
        a_class (class): a specified class to check with

    Return:
        True: If the object is an instance of a class that
        inherited (directly or indirectly) from the specified class
        False: otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
