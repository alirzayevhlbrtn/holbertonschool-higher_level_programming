#!/usr/bin/python3
"""
First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class of rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area calculate
        """
        return self.__width * self.__height

    def display(self):
        """
        display function
        """
        for i in range(self.__y):
            print()

        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for k in range(self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print()
        print()

    def __str__(self):
        """
        modified __str__
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        update function
        """
        if args:
            ls = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, ls[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
