#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Prime Game function
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_num + 1, i):
                primes[j] = False

    num_of_primes = sum(1 for prime in primes if prime)

    if num_of_primes <= 2:
        return "Ben"

    return "Maria" if x % 2 == 0 else "Ben"
