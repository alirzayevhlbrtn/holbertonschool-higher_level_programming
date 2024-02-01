#!/usr/bin/python3
"""
Defining a class Square with properties
"""


class Square:
    """
    Class Square with private attribute size
    """
    def __init__(self, size=0) -> None:
        """
        __init__ method that sets the size of the square

        Args:
            size (int): size of square
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        calculates size of square
        """
        return self.__size ** 2
