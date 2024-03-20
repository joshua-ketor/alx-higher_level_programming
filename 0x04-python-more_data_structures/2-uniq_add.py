#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ add all unique integers in a list (only once for each integer) """
    set_list = set(my_list)
    sum = 0
    for num in set_list:
        sum += num

    return sum
