#!/usr/bin/python3
"""Define base geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """rep the rectangle"""
    def __init__(self, width, height):
        """Intialize a new Rectangle.
        
        Args:
            width: width of rectangle
            height(int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """Return area self"""
        return (self.__width * self.__height)
    
    def __str__(self):
        """Return rectangle description and print"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string