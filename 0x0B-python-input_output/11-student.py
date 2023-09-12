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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list, optional): A list of attribute names
            to retriev. Defaults to None
        Returns:
            dict: A dictionary representation of the Student instance.
        """

        if attrs is None:
            return self.__dict__

        data = {}
        for attr in attrs:
            if hasattr(self, attr):
                data[attr] = getattr(self, attr)
        return data

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based
        on a dictionary

        Args:
            json (dict): A dictionary conatining attribute names and value
        """

        for key, value in json.items():
            setattr(self, key, value)
