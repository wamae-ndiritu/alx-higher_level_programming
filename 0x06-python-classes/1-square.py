#!/usr/bin/python3


"""
Defines a square using class
"""


class Square:
    """
    The Square class defines a square based on the
    provided size.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The private instance attribute for the size
        """

        self.__size = size
