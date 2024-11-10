#!/usr/bin/python3
"""
N Queens puzzle solution using backtracking
The program solves the N Queens problem of placing N non-attacking
queens on an N×N chessboard
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    Args:
        board: The current board state
        row: Current row to check
        col: Current column to check
        n: Size of the board
    Returns:
        Boolean indicating if the position is safe
    """

    for j in range(col):
        if board[row][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):

    """
    Solve the N Queens puzzle and print all solutions
    Args:
        n: Size of the board and number of queens
    """

    board = [[0 for x in range(n)] for y in range(n)]
    solutions = []
    solve_util(board, 0, n, solutions)

    for sol in solutions:
        output = []
        for i in range(n):
            for j in range(n):
                if sol[i][j] == 1:
                    output.append([i, j])
        print(output)


def solve_util(board, col, n, solutions):
    """
    Utility function to solve N Queens problem using backtracking
    Args:
        board: Current board state
        col: Current column being processed
        n: Size of the board
        solutions: List to store all valid solutions
    Returns:
        Boolean indicating if a solution is possible
    """

    if col >= n:
        temp = [row[:] for row in board]
        solutions.append(temp)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):

            board[i][col] = 1

            res = solve_util(board, col + 1, n, solutions) or res

            board[i][col] = 0

    return res


def main():
    """Main function to handle program execution and validation"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
