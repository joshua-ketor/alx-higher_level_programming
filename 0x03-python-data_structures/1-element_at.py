#!/usr/bin/python3
def element_at(my_list, idx):
    """This function retrieves an element from a
    a list like in C.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
