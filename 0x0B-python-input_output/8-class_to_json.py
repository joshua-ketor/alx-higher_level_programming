#!/usr/bin/python3
"""Module that contains the class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description of a simple data structure"""
    return obj.__dict__
