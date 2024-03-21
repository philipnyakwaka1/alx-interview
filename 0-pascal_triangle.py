#!/usr/bin/python3
"""
This module defines a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n:
"""
from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """
    This function def pascal_triangle(n):
    that returns a list of lists of integers representing
    the Pascal’s triangle of n:
    """

    if n <= 0:
        return []

    triangle: List[List[int]] = [[1]]
    for i in range(1, n):
        row: List[int] = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
