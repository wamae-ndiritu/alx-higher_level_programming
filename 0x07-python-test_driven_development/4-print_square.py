#!/usr/bin/python3
"""
Defines a function to print squares
"""


def print_square(size):
    """
    Prints a square of size dimensions

    Args:
        size (int): The dimensions of the square

    Raises:
        TypeError: If size is not an int or it is a float and less than 0
        ValueError: If size is less than 0

    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#'*size)
