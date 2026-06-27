#!/usr/bin/python3
"""This module defines the BaseGeometry class."""


class BaseGeometry:
    """A class that defines base geometry."""

    def area(self):
        """Raise an Exception for unimplemented area."""
        raise Exception("area() is not implemented")
