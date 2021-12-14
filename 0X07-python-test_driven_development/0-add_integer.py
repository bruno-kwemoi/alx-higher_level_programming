#!/usr/bin/python3
"""
module 0-add_integer.py

functions add_integer
"""


def add_integer(a, b=98):
    """
    this function returns the sum of two integers

    if arguments are of type float it converts them to type int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
