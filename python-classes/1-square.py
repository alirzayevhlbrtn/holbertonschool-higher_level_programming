#!/usr/bin/python3
"""
Defining a class Square with properties
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size) -> None:
        """
        __init__ method that sets the sets the size of the square

        Args:
            size (int): size of square
        """
        self.__size = size
