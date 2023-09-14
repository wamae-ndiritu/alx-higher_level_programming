#!/usr/bin/python3
"""
This module defines class Base
that manages the id attribute in other classes
avoiding duplicating the same code
"""
import json


class Base:
    """
    class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiates Base attributes

        Args:
            id (int): Value for Public instance attribute id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to JSON string representation

        Args:
            list_dictionaries (list(dict)): A list of dictionaries

        Returns:
            JSON: A JSON string representation of list_dictionaries
        """
        return json.dumps(list_dictionaries)
