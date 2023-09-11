#!/usr/bin/python3
"""
This module defines class Square
that inherits from class REctangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that extends class Rectangle
    """

    def __init__(self, size):
        """
        Instantiates size

        Args:
            size (int): the value to size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square

        Return:
            (int): the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square

        Returns:
            str: A string in the format [Square] <size>/<size>
        """
        return f"[Square] {self.__size}/{self.__size}"
