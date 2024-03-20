#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """delete keys with s specific value in a dictionary"""
    a_dict = dict(a_dictionary)
    if not value:
        return a_dictionary
    for key in a_dict.keys():
        if a_dict[key] == value:
            del a_dictionary[key]

    return a_dictionary
