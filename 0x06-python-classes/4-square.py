#!/usr/bin/python3
"""define class square"""
class Square:
    """init size"""
    def __init__(self, size=0):
        """instantiate the square"""
        self.size = size
        """set the properties of the square"""
    @property
    def size(self):
        return (self.__size)
    @size.setter
    def size(self, value):
        """instantiate the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        return (self.__size * self.__size)
