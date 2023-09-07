#!/usr/bin/python3


"""
Module to add two integers
"""


def add_integer(a, b=98):
    """
    Add two integers

    Args:
        a (int, float): The first integer
        b (int, float): The second integer

    Raises:
        TypeError: If a or b is either not an int or a float

    Return: returns the sum of the two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
