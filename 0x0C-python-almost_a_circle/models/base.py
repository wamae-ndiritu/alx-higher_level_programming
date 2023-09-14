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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to JSON string representation

        Args:
            list_dictionaries (list(dict)): A list of dictionaries

        Returns:
            JSON: A JSON string representation of list_dictionaries
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
                      [obj.to_dictionary() for obj in list_objs])

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts to a list of JSON string representation

        Args:
            json_string (str): A string representing a
            list of dictionaries

        Returns:
            list: A list represented by json_string
        """
        return json.loads(json_string)
