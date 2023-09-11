#!/usr/bin/python3
"""
The module defines a function to add
a new attribute to an object if it's possible
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible

    Args:
        obj: The object to which the attribute will be added
        name (str): The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object already has an attribute
        with the same name.
    """

    if not hasattr(obj, name):
        if hasattr(obj, '__dict__') and isinstance(obj.__dict__, dict):
            obj.__dict__[name] = value
        else:
            raise TypeError("can't add new attribute")
    else:
        raise TypeError("can't add new attribute")
