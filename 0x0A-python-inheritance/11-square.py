#!/usr/bin/python3
"""Define class"""


Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    def __init__(self, size):
        """Intialize a new square.
        
            Args:
                width: width of square
                height(int): height of square
        """
        self.integer_validator("size", size)
        self.__size = size