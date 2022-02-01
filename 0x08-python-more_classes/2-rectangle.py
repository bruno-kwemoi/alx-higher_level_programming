#!/usr/bin/python3
"""
module 2-rectangle
"""


class Rectangle:
    """it defines the class rectangle"""
    def __init__(self, width=0, height=0):
        """initializes class attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrives width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrives height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        return (self.__width) * 2 + (self.__height) * 2
