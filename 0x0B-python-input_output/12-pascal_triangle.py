#!/usr/bin/python3
"""
This module defines function pascal_triangle
that returns a list of list of integers representing
the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n number of rows

    Args:
        n (int): The number of rows to generate

    Returns:
        list of lists: A list of lists representing Pascal's Triangle
    """
    if n <= 0:
        triangle = []
    elif n == 1:
        triangle = [[1]]
    elif n == 2:
        triangle = [[1, 1]]
    else:
        triangle = [[1], [1, 1]]
        for i in range(3, n+1):
            m_list = triangle[i - 2]
            tmp_list = [1]
            k = 0
            for j in range(1, i-1):
                tmp_list.append(m_list[k] + m_list[k+1])
                k = k + 1
            tmp_list.append(1)
            triangle.append(tmp_list)
    return triangle
