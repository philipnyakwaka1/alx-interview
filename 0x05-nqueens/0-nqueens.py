#!/usr/bin/python3
"""Module for N queens puzzle"""
import sys


def check_safe(b, row, col):
    """
    Check safety
    """
    for i in range(0, col):
        if b[i] == row or b[i] == row - col + i or b[i] == row + col - i:
            return False
    return True


def solve(board, col, solutions, size):
    """
    Solves Queen problem recursively
    """
    if col == size:
        solutions.append(list(board))
        return

    for row in range(size):
        if check_safe(board, row, col):
            board[col] = row
            solve(board, col + 1, solutions, size)


def solve_n_queens(n):
    """
    Prints solutions
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve(board, 0, solutions, n)

    for solution in solutions:
        print([[row, solution[row]] for row in range(n)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solve_n_queens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
