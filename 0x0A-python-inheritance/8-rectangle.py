#!/usr/bin/python3
"""Module for BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Subclass rectangle that inherits from base class BaseGeometry"""
    def __init__(self, width, height):
        """Constructor
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
