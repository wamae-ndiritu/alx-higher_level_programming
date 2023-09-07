#!/usr/bin/python3
"""
The module defines a function that prints your name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name
    
    Args:
        first_name (str): The first argument
        last_name (str): The second argument

    Raises:
        TypeError: If first_name or last_name is not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
