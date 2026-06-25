#!/usr/bin/python3
"""This module defines the inherits_from function."""


def inherits_from(obj, a_class):
    """Check if obj inherited from a_class, not exactly a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
