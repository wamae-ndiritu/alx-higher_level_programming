#!/usr/bin/python3
"""
Defines class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle

    Attributes:
        width (int): Private instance attribute
        height (int): Private instance attribute
        x (int): Private instance attribute
        y (int): Private instance attribute
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiates private instance attributes

        Args:
            width (int): Width Size of the rectangle
            height (int): Height size of the rectangle
            x (int): Attribute x. Defaults to 0
            y (int): Attribute y. Defaults to 0
        """
        super().__init__(id)  # assign class id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Gets the value of private instance attribute width

        Returns:
            (int): The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width of the rectangle

        Args:
            width (int): The value to be set to width of the rectangle
        """
        self.__width = width

    @property
    def height(self):
        """
        Retrieves the private instance attribute height

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the private instance attribute height

        Args:
            (int): The value to be set as the height of the rectangle
        """
        self.__height = height

    @property
    def x(self):
        """
        Retrieves the private instance attribute x

        Returns:
            int: x value of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, x=0):
        """
        Sets the private instance attribute x

        Args:
            (int): The value to be set as x of the rectangle.
            Defaults to 0
        """
        self.__x = x

    @property
    def y(self):
        """
        Retrieves the private instance attribute y

        Returns:
            int: y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, y=0):
        """
        Sets the private instance attribute y

        Args:
            (int): The value to be set as y of the rectangle.
            Defaults to 0.
        """
        self.__y = y
