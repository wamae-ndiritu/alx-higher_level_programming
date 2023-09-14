#!/usr/bin/python3
"""
Defines class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiates self and parent attributes

        Args:
            size (int): Size of the square
            x (int): x value of the rectangle. Defaults to 0.
            y (int): y value of the rectangle. Defaults to 0.
            id (id): id of the class. Default to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overides the __str__ method of the parent to
        represent a square

        Returns:
            str: A string of the format
                [Square] (<id>) <x>/<y> - <size>
        """
        s_id, s_width = self.id, self.width
        x, y = self.x, self.y
        return f"[Square] ({s_id}) {x}/{y} - {s_width}"

    @property
    def size(self):
        """
        Gets the size of the square

        Returns:
            int: The size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Sets the size of the square

        Args:
            size (int): The size of the square
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Updates attributes

        Args:
            *args (list): A list of non-keyworded arguments
            **kwargs (tuple): A list of keyworded arguments
        """
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = args[0]
            self.size = args[1] if len(args) > 1 else self.size
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.y
