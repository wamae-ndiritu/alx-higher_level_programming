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
