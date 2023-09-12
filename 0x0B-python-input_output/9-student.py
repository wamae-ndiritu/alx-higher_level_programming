#!/usr/bin/python3
"""
Defines class Student
"""


class Student:
    """
    class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instatiates first_name last_name and age

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Takes an object (an instance of a class) and initializes
        dictionary description of its attribute
        with sample data structure suitable for JSON serialization

        Returns:
            (dict): description of the class attributes

        """
        serialized_data = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serialized_data[key] = value
        return serialized_data
