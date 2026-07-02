#!/usr/bin/python3
"""This module defines CountedIterator class."""


class CountedIterator:
    """An iterator that keeps track of how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and a counter."""
        self.iterator = iter(iterable)
        self.__count = 0

    def get_count(self):
        """Return the number of items iterated."""
        return self.__count

    def __next__(self):
        """Fetch next item and increment counter."""
        try:
            item = next(self.iterator)
            self.__count += 1
            return item
        except StopIteration:
            raise

    def __iter__(self):
        """Return self as the iterator."""
        return self
