#!/usr/bin/python3
"""Module for makeChange"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make the total amount.

    Args:
        coins (List[int]): List of coin denominations available.
        total (int): Total amount to make change for.

    Returns:
        int: The minimum number of coins needed to make the total amount.
        Returns -1 if change cannot be made.
    """

    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
