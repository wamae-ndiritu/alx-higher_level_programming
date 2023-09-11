#!/usr/bin/python3
"""
Defines a function that check if an object is an
instance of, or if the object is an instance of a class
that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if is instance of a class or the base (inherited class)

    Args:
        obj (object): any item to be checked
        a_class (class): a specified class to check with

    Return:
        True: If the object is an instance of,
        or if the object is an instance of a
        class that inherited from, the specified class
        False: otherwise

    """

    return isinstance(obj, a_class)
