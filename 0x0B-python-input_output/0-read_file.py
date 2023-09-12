#!/usr/bin/python3
"""
This module defines a function that reads a text
file and prints its content to stdout
"""


def read_file(filename=""):
    """
    Opens the file with read mode and prints
    its content to stdout

    Args:
        filename (str): Name of the file to be opened
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
