#!/usr/bin/python3
"""Module containing print_square function"""


def print_square(size):
    """Print a square with the character `#`
    Args:
        size (int): a square with side `size`

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
        TypeError: if size is a float and less than zero
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
