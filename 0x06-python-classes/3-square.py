#!/usr/bin/python3
"""Module with a square class"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        """Instatiation method
        Args:
            self (obj): self reference to instance
            size: size of square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Area of the circle
        Returns:
            The current square area
        """

        return self.__size ** 2
