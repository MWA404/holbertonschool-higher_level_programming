#!/usr/bin/python3
"""
Module for text_indentation function.
Prints text with 2 new lines after . ? and : characters.
"""


def text_indentation(text):
    """Prints text with 2 new lines after each . ? and : character.
    No spaces at the beginning or end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for c in text:
        line += c
        if c in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
