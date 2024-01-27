#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>.

    Args:
        first_name (str): First name.
        last_name (str): Last name.

    Raises:
        TypeError: if first_name and last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
