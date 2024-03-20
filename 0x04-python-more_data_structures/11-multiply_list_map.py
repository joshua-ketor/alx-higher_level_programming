#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """ return a list with all values multiplied by a number
    without using any loops.
    """
    values = list(map(lambda x: x * number, my_list))
    return values
