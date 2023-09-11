#!/usr/bin/python3
"""
This module defines class BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """

    def area(self):
        """
        Raises:
            Exception: raises by default since no area implementation
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates integer

        Args:
            name (str): name of the variable
            value (int): value of the name

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
