#!/usr/bin/python3
"""Define function"""


def pascal_triangle(n):
    """rep the rectangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        row = triangle[-1]
        tmp = [1]
        for i in range(len(row) - 1):
            tmp.append(row[i] + row[i +1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle