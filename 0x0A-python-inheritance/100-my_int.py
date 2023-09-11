#!/usr/bin/python3
"""
This module defines class MyInt that
inherits from python built-in class int
"""


class MyInt(int):
    """
    class MyInt that inherits from int with
    inverted == and != operators
    """

    def __eq__(self, other):
        """
        Overide the == operator to return opposite results

        Args:
            other (int or MyInt): The value to compare.

        Returns:
            bool: True if values are not equal, otherwise False
        """

        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to return inverted result.

        Args:

            other (int or MyInt): The other value to compare.

        Returns:
            bool: True if values are equal, False otherwise
        """

        return super().__eq__(other)
