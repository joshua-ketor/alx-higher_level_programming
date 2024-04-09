#!/usr/bin/python3
"""Module for text_indentation"""


def text_indentation(text):
    """Prints a text with 2 new lines after each
    of these characters: `.`,`?` and `:`
    Args:
        text (str): text to print

    Raises:
        TypeError: if text is not of type str
    """
    space_on_end = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char in ['.', '?', ':']:
            print(char)
            print()
            space_on_end = True
        elif space_on_end == True and char == ' ':
            space_on_end = False
        else:
            print(char, end='')
