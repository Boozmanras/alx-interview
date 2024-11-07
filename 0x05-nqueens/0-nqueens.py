#!/usr/bin/python3
import sys


def print_solution(board):
    """Print a solution in the required format"""
    solution = []
    for row in range(len(board)):
        solution.append([row, board[row]])
    print(solution)


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N):
    """Use backtracking to find all solutions"""
    if row == N:
        print_solution(board)
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, N)


def main():
    """Main function to handle input validation and call the solver"""
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

    board = [-1] * N
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    main()
