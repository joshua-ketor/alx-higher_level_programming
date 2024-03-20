#!/usr/bin/python3
def best_score(a_dictionary):
    """ return a key with the biggest integer value """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max_num = 0
    for key in list(a_dictionary):
        if a_dictionary[key] > max_num:
            max_num = a_dictionary[key]
            max_key = key
    return max_key
