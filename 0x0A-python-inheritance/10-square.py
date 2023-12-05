#!/usr/bin/python3
"""define class"""


Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """rep square"""
    def __init__(self, size):
        """Intialize a new square.
        
        Args:
            width: width of square
            height(int): height of square
        """
        self.integer_validator("size", size)
        self.__size = size
    def area(self):
        """return area of self"""
        return(self.__size * self.__size)