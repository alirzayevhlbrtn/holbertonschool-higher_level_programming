#!/usr/bin/python3
"""
Pascal print triangle
"""


def pascal_triangle(n):
    """
    function of pascal
    """
    pascal = []
    if n <= 0:
        return pascal
    else:
        for i in range(n):
            row = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    abv = pascal[i - 1]
                    m = abv[j - 1] + abv[j]
                    row.append(m)
            pascal.append(row)

        return pascal
