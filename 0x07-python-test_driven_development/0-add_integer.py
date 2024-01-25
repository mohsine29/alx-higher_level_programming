#!/usr/bin/python3
def add_integer(a, b=98):
    """Returns the sum of 2 integers.

    Args:
        a(int): first integer to be added.
        b(int): second integer to be added.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    for val in (a, b):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{val} must be an integer")
    return int(a) + int(b)
