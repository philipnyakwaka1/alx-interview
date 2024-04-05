#!/usr/bin/python3
"""
This module defines a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    This function def pascal_triangle(n):
    that returns a list of lists of integers representing
    the Pascal’s triangle of n:
    """

    my_list = [[1], [1, 1]]
    for i in range(2, n):
        row = []
        for j in range(len(my_list[i - 1]) - 1):
            num = my_list[i - 1][j] + my_list[i - 1][j + 1]
            row.append(num)
        row.append(1)
        row.insert(0, 1)
        my_list.append(row)
    return [[1]] if n == 1 else [] if n <= 0 else my_list
