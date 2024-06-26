#!/usr/bin/python3
"""Module for square class"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Child class square and parent class Rectangle"""
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Square Description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
