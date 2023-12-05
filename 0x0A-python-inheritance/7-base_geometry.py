#!/usr/bin/python3
"""Define class"""


class BaseGeometry:
    """rep class geometry"""

    def area(self):
        """raise error"""
        Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter as int.
        
        Args:
            name(str): name of the parameter.
            value(int): value of parameter.
        Raises:
            TypeError - if not int.
            ValueError - if less than 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))