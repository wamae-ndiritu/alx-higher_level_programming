#!/usr/bin/python3


"""
Defines a square using class
"""


class Square:
    """
    The Square class defines a square based on the
    provided size.
    """

    def __init__(self, size=0):
        """
        Validates size & Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The private instance attribute for the size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
