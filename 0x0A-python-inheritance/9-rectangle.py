#!/usr/bin/python3
"""Module for Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle subclass"""

    def __init__(self, width, height):
        """Constructor"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """User representation of object"""
        return "[{}] {}/{}".format("Rectangle", self.__width,
            self.__height)
