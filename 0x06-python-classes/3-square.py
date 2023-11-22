#!/usr/bin/python3
"""define class square"""
class Square:
    """init size"""
    def __init__(self, size=0):
        """size must be int and >=0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """returns area of self"""
        return (self.__size * self.__size)
