#!/usr/bin/python3
"""
This module defines function append_write
that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Append text to a file

    Args:
        filename (str): The file to be appended
        text (str): THe text to be append to the file

    Returns:
        (int): count of characters added

    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added
