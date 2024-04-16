#!/usr/bin/python3
"""Module for MyInt"""


class MyInt(int):
    """invert == and !="""
    def __eq__(self, value):
        """Override == with !="""
        return self.real != value

    def __ne__(self, value):
        """invert != for =="""
        return self.real == value
