#!/usr/bin/python3

"""Define a class rectangle"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the current width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

    @property
    def heigth(self):
        """Get/set the current heigth of the rectangle."""
        return (self.__heigth)

    @heigth.setter
    def heigth(self, value):
        if not isinstance(heigth, int):
            raise TypeError("heigth must be an integer")
        elif width < 0:
            raise ValueError("heigth must be >= 0")
