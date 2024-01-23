#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize the square with size=0"""
        self.__size = size
        self.validate_size()
        def validate_size(self):
            """"Validate that size is an integer and >= 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
