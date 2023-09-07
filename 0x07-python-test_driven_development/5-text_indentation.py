#!/usr/bin/python3
"""
Defines a function thap performs text indentation
"""


def text_indentation(text):
    """
    Formats text indentation by adding new line where there is
    end of line punctuation

    Args:
        text (str): The text to be formatted

    Raises:
        TypeError: If the text passed is not a str

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = []  # store the current line

    for char in text:
        if char in ".?:":
            line.append(char)
            print("".join(line).strip())
            print()
            line = []
        else:
            line.append(char)
