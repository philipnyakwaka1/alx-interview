#!/usr/bin/python3
"""Module for rotate_2d_matrix function
"""


def rotate_2d_matrix(matrix: list[list[int]]) -> None:
    """Rotates a 2D matrix 90 degrees, clockwise
    """
    left, right = 0, len(matrix) - 1
    while left < right:
        top, bottom = left, right
        for i in range(right):
            tmp = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = tmp
        left += 1
        right -= 1
