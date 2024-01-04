#!/usr/bin/python3
"""The N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
For Ex.:
    $$ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
"""

import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    for row in board:
        print(" ".join('.' if i != row else 'Q' for i in range(len(board))))
    print()

def solve_nqueens_util(board, row, n):
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens_util(board, row + 1, n)

def solve_nqueens(n):
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens_util(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
