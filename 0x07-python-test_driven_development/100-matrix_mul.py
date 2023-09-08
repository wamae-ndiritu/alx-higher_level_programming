#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """
    """
    # Check if m_a or m_b is not list
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')

    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    # Check if elements of m_a or m_b not list
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    # Check if m_a or m_b is empty
    if not m_b:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")

    # Check if the list values are int or float
    for row in m_a:
        if not all(isinstance(num, (int, float))
                   for num in row):
            raise TypeError('m_a should contain only integers or floats')

    for row in m_b:
        if not all(isinstance(num, (int, float))
                   for num in row):
            raise TypeError('m_b should contain only integers or floats')

    # Check if m_a or m_b is not rectangle, each row must be same size
    num_cols_m_a = len(m_a[0])
    num_cols_m_b = len(m_b[0])

    if any(len(row) != num_cols_m_a for row in m_a):
        raise TypeError('each row of m_a must be of the same size')

    if any(len(row) != num_cols_m_b for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    # Check if m_a and m_b can't be multiplied
    if num_cols_m_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize the result matrix with zeros
    result = [[0.0 for _ in range(num_cols_m_b)] for _ in range(len(m_a))]

    # Perform matrix multiplacation
    for i in range(len(m_a)):
        for j in range(num_cols_m_b):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
