#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value.
        Args:
            name: name to validate.
            value: value to validate.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is lessor equal to 0.
        """
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
