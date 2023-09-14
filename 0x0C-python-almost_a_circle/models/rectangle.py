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

        Raises:
            TypeError: If the input is not an integer
            ValueError: If width and height is less than or equal to 0
                        If x and y is less than 0
        """
        super().__init__(id)  # assign class id
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

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

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than or equal to 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
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

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than or equal to 0.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
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

        Raises:
            TypeError: If x is not an integer
            ValueError: If x is less than 0.
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the representation of the Rectangle instance to the stdout
        using the character #
        The function also considers the x, and y values of the rectangle
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            str: A string in the format
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        r_id = self.id
        r_x, r_y = self.__x, self.__y
        r_width, r_height = self.__width, self.__height
        return f"[Rectangle] ({r_id}) {r_x}/{r_y} - {r_width}/{r_height}"
