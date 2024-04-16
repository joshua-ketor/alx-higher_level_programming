#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Area of a geometry
        Raise:
            Exception: when area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator that validates value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
