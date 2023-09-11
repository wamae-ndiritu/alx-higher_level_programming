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
