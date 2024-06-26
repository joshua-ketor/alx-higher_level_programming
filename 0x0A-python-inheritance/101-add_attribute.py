#!/usr/bin/python3
"""Module for add_attribute"""


def add_attribute(obj, att, value):
    """Add attribute to object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
