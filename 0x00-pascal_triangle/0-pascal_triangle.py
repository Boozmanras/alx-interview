#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    
    Args:
        n (int): The number of rows of Pascal's triangle to generate.
    
    Returns:
        list: A list of lists of integers representing Pascal's triangle.
        If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle


if __name__ == "__main__":
    print_triangle = __import__('0-main').print_triangle

    print_triangle(pascal_triangle(5))
