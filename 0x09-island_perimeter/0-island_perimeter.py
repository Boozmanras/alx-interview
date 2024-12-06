#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.

    Args:
        grid (list of list of int):
        A 2D grid representing water (0) and land (1).
        Each cell is square, side length of 1.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1

                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1

                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
