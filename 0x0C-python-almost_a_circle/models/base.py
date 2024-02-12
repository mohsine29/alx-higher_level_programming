#!/usr/bin/python3
"""Base.py"""
import json
import csv
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objectts += 1
            self.id = self.__nb_objects
