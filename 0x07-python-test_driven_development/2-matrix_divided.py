#!/usr/bin/python3


def matrix_divided(matrix, div):
    # Check if the matrix is a list of lists, integers or floats
    if not all(isinstance(row, list) and
               all(isinstance(num, (int, float))
               for num in row) for row in matrix):
        raise TypeError(
               "matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    row_len = set(len(row) for row in matrix)
    if len(row_len) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is an int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 dp
    result_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return result_matrix
