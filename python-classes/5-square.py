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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculates size of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints square with #
        """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
