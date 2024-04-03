#!/usr/bin/python3
"""Module with a square class"""


class Square:
    """A square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Instatiation method
        Args:
            self (obj): self reference to instance
            size: size of square
            position: a tuple

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
            TypeError: if position is not a tuple of 2 positive integers
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if not (position[0] >= 0 and position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        Args:
            value: the value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """A getter function for position

        Returns:
            The position tuple
        """
        return self.__position

    @position.setter
    def positoin(self, value):
        """A setter for position
        Args:
            value (tuple): the value to set to position
        """
        if not(self.__position[0] >= 0 and self.__position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or (not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of the circle
        Returns:
            The current square area
        """

        return self.__size ** 2

    def my_print(self):
        """Print to stdout the square with the character #
        if size is equal to 0, print an empty line
        """
        i = 0
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):

                    print("#", end="")
                print()
