#!/usr/bin/python3
import sys


def print_solution(solution):
    """Prints a single solution in the required format."""
    print(solution)


def is_safe(board, row, col):
    """Check if placing a queen at board[row][col] is safe."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row=0, board=[]):
    """Recursively solves the N-queens problem using backtracking."""
    if row == N:
        print_solution([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if is_safe(board, row, col):
            solve_nqueens(N, row + 1, board + [col])


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
