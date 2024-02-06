#!/usr/bin/python3
"""
Document of empty class
"""


BaseGeometry = __import__('8-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class of inherited rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
