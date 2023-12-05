#!/usr/bin/python3
"""import base geometry"""
BaseGeometry = __import__('7-base_geomety').BaseGeometry

class Rectangle(BaseGeometry):
    """rep a rectangle"""
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