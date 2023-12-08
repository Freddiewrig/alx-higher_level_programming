#!/usr/bin/python3
"""Define class"""
from models.base import Base

class Rectangle(Base):
    """Init new rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle that inherits from Base.
        
        Args:
            width(int): width of the rectangle.
            height(int): height if the rectangle.
            x(int): x cordinate
            y(int): y cordinate
            id: id
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width
    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @property
    def height(self):
        """getter for  height"""
        return self.__height
    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        
    @property
    def x(self):
        """getter for x"""
        return self.__x
    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an int")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
        
    @property
    def y(self):
        """getter for y"""
        return self.__y
    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) != int:
            raise TypeError("y must be an int")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return(self.__height * self.__width)
    
    def display(self):
        """prints the rectangle using #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))