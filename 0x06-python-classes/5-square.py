#!/usr/bin/python3
"""
Module 5-square.py
class Square
"""


class Square:
    """
    defines a square

    args self, size
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print('')
        i = 0
        while i < self.__size:
            print("#" * self.__size)
            i += 1
