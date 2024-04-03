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

    @property
    def size(self):
        """A getter function for size
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        Returns:
            The value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """A setter function for size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the circle
        Returns:
            The current square area
        """

        return self.__size ** 2
