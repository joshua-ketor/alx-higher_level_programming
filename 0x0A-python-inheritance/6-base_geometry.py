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
