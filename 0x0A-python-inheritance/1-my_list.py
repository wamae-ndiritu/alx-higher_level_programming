#!/usr/bin/python3
"""
Defines a class MyList that inherits from list
"""


class MyList(list):
    """
    MyList class inherits from list
    """

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        sorted_list = sorted(self)
        print(sorted_list)
