#!/usr/bin/python3
"""Module for max_integer unittest"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unittest"""

    def test_ordered_list(self):
        """Method to test ordered list"""
        olist = [1, 2, 3, 4]
        self.assertEqual(max_integer(olist), 4)

    def test_empty_list(self):
        """Method to test method with no parameters"""
        self.assertEqual(max_integer(), None)

    def test_more_than_one_param(self):
        """Method to test multiple params"""
        self.assertRaises(TypeError, max_integer, 2, 3, 4)

    def test_int(self):
        """Method to test argument of type int"""
        self.assertRaises(TypeError, max_integer, 2)

    def test_str(self):
        """Method to test string param"""
        self.assertEqual(max_integer('str'), 't')

    def test_none(self):
        """Method to test None value"""
        self.assertRaises(TypeError, max_integer, None)

    def test_string_list(self):
        self.assertEqual(max_integer(['Hi', 'there']), 'there')
