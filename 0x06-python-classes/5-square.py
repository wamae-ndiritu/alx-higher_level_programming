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

        self.__size = size

    @property
    def size(self):
        """
        Retrives the size of the square (Getter)

        Returns:
            int: The size of the square
        """

        return self.__size

    @size.setter
    def size(self, size):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(size, int):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Gets the area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
