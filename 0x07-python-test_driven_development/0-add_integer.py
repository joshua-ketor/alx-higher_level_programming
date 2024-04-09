#!/usr/bin/python3

"""Module with add function"""


def add_integer(a, b=98):
    """Adds two integers
    Args:
        a (int): The first integer
        b (int, optional): The second integer. Defaults to 98

    Returns:
        An integer: the addtion of a and b

    Raises:
        TypeError: if either `a` or `b` is not an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
