#!/usr/bin/python3
"""
module 2-matrix_divided.py

functions matrix_divided
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    a = len(matrix[0])
    for i in matrix:
        if len(i) != a:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
    new = []
    for rows in matrix:
        new.append(list(map(lambda x: round(x/div, 2), rows)))
    return(new)
