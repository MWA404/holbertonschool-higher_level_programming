#!/usr/bin/python3
"""This module defines Animal abstract class and subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that defines an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """A class that defines a dog."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """A class that defines a cat."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
