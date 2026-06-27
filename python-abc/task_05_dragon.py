#!/usr/bin/python3
"""This module defines SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """Mixin that provides swimming ability."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying ability."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class that inherits from SwimMixin and FlyMixin."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
