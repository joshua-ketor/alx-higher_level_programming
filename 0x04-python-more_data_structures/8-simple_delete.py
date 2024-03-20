#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ delete a key in a dictionary """
    if key in list(a_dictionary):
        del a_dictionary[key]
    return a_dictionary
