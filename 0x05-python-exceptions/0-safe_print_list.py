#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for el in my_list:
        try:
            print(el, end='')
            n += 1
        except IndexError:
            break
    print()
    return n
