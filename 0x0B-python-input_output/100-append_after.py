#!/usr/bin/python3
"""
This module defines function append_after
that inserts a line of text to a file, after
each line containing specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific
    string in a file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after lines
        containing the search string
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
