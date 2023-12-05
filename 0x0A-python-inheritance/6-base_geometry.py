#!/usr/bin/python3
"""Define base class."""


class BaseGeometry:
    """rep base geometry"""

    def area(self):
        """raise exception error"""
        raise Exception("area() is not implemented")