#!/usr/bin/python3
"""
module 6-square
"""
class Square:
    """
    defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position (self, value):
        if isinstance(value, tuple) is not True and len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return self._size**2

    def my_print(self):
        if self._size == 0:
            print('')
        i = 0;
        while i < self._size:
            print('{}{}'.format(' '*self._position[0], '#'*self.size))
            i += 1
