#!/usr/bin/python3
"""
Code of square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class of Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size,
        )

    def update(self, *args, **kwargs):
        """
        Update suqare
        """
        if args:
            ls = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, ls[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
