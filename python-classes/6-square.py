#!/usr/bin/python3
"""
Defining a class Square with properties
"""


class Square:
    """
    Class Square with private attribute size
    """
    def __init__(self, size=0, position=(0, 0))  -> None:
        """
        __init__ method that sets the size of the square

        Args:
            size (int): size of square
            position (int): position of square
        """
        self.size = size
        self.position = position
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value: tuple):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for l in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
