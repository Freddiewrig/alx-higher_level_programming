#!/usr/bin/python3

"""define class rectangle"""


class Rectangle:
    """init self width
    height"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The size of the new rectangle.
            height (int): the height of the new rectangle.
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """Get/set the current width of the Rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the Rectangle."""
        return (self.__height)
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value