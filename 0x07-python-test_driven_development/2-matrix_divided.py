#!/usr/bin/python3
"""
Defines a function to divide matrices
The matrix is a 2D array

"""


def matrix_divided(matrix, div):
    """
    Divides elements of a matrix with the div

    Args:
        matrix (list(list(int, float)):
                A 2D matrix of either integers or floats
        div (int, float): The divisor

    Raises:
        TypeError: If the elements of the matrix are
                   not a list of int or floats
                   Or the rows of the matrix have varrying size
                   Or the divisor is not an int or a float
        ZeroDivisionError: If the divisor is equal to zero.
    Return: returns a new matrix where each element of each row
            in the matrix have been divided by the divisor.

    """

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
