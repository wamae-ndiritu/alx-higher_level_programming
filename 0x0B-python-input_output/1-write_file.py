#!/usr/bin/python3
"""
This module defines a function to write
a string to a file
"""


def write_file(filename="", text=""):
    """
    Writes the text to the file with filename

    Args:
        filename (str): The file to be written
        text (str): The text to be written in a file
    """

    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
