#!/usr/bin/python3


"""
Defines a square using class
"""


class Square:
    """
    The Square class defines a square based on the
    provided size.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Validates size & Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The private instance attribute for the size
            __position (tuple): The private instance attr for
            position of the square
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        position Getter

        Returns:
            tuple: The position of the square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square

        Args:
            value (tuple): The new position for the square

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints the square with the character #
        """

        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
