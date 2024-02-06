#!/usr/bin/python3
"""
Contains the write_file function
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written."""
    with open(filename) as f:
        count = len(f.readlines())
    return count
