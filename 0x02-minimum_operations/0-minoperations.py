#!/usr/bin/python3

"""
This module defines a method that calculates the fewest
number of operations needed to result in
exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    This function calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    num: int = 0
    m: int = 2
    while n > 1:
        while n % m == 0:
            num = num + m
            n = n // m
        m += 1
    return num
