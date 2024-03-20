#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ return a new dictionary with all values multiplied by 2 """
    new_dict = dict(a_dictionary)
    for key in list(new_dict):
        new_dict[key] *= 2

    return new_dict
