#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import rectangle

class Square(rectangle):
    """Init the new square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        new square
        Args:
            size(int): size of the square
            x(int): the x coordinates
            y(int): the y coordinate.
            id(int): the id of the square.
        """
        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        """get/ set size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square object.

        Args:
            *args: No-keyword arguments.
            **kwargs: Keyword arguments.
        """
        if args:
            # Update attributes based on positional arguments
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                else:
                    break
        else:
            # Update attributes based on keyword arguments
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """returns the atrr of the square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
