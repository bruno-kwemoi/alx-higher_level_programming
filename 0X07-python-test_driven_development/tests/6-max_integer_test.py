#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_maxinteger(self):
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_types(self):
        self.assertRaises(TypeError, max_integer, 'b')
        self.assertRaises(TypeError, max_integer, 3+5j)
