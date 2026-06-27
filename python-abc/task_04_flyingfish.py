#!/usr/bin/python3
"""This module defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """A class that defines a fish."""

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish habitat."""
        print("The fish lives in water")


class Bird:
    """A class that defines a bird."""

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class that inherits from both Fish and Bird."""

    def fly(self):
        """Print that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
