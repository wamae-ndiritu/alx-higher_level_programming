#!/usr/bin/python3
"""
This module defines class Rectangle that extends BaseGeometry
Rectangle inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that extends class BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiates width and height

        Args:
            width (int): the value to width
            height (int): the value to height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle

        Return:
            (int): the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            str: A string in the format [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
