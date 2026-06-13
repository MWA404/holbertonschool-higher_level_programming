#!/usr/bin/python3
"""
Module for print_square function.
Prints a square with # characters.
"""


def print_square(size):
    """Prints a square of a given size using # characters.
    Size must be a non-negative integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
