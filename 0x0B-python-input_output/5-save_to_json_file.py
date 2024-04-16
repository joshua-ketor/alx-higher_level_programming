#!/usr/bin/python3
"""Module with save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation"""
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
