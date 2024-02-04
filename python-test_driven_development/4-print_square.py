#!/usr/bin/python3
"""
Square printer
"""


def print_square(size):
    """
    function of printer
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
