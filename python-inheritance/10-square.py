#!/usr/bin/python3
"""
Document of empty class
"""


BaseGeometry = __import__('9-rectangle').Rectangle


class Square(BaseGeometry):
    """
    Class of inherited rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
