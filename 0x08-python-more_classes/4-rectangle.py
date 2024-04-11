#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Constructor
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter
        Returns: the rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter
        Returns: the rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle area method
        Returns: the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Rectangle perimeter method
        Returns: the perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print a rectangle with character #"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            if i != self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """String representation of the rectangle object to recreate"""

        return "Rectangle({}, {})".format(self.__width, self.__height)
