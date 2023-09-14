#!/usr/bin/python3
"""
This module defines class Base
that manages the id attribute in other classes
avoiding duplicating the same code
"""
import json
import os
import csv


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
        if json_string is None:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with all  attributes set

        Args:
            dictionary (tuple): A variable no. of key/value pair
            arguments

        Returns:
            obj: Returns an instance of the cls
        """
        dummy_instance = cls(1, 1, 1)  # creates a dummy instance

        # Update the dummy instance with real values
        dummy_instance.update(**dictionary)

        # Return the updated instance
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Loads JSON list from a file and converts it to Python Object
        and create instances of the class with each of the object

        Returns:
            list of obj: A list of created instances of the class
        """
        filename = cls.__name__ + ".json"

        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                data = cls.from_json_string(file.read())
                list_of_instances = [cls.create(**obj) for obj in data]
                return list_of_instances
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the JSON string representation of list_objs
        to a csv file

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"
        data = [obj.to_dictionary() for obj in list_objs]

        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write the header row
            csv_format = ["id", "width", "height", "x", "y"]
            csv_writer.writerow(csv_format)

            # Write the data row for each of the key using csv_format
            for obj in data:
                data_row = [obj[key] for key in csv_format]
                csv_writer.writerow(data_row)
