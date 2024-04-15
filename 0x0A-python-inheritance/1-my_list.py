#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """MyList class that inherits from list class"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
