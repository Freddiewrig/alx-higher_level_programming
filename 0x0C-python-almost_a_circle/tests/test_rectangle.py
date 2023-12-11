#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
Unittest classes:
    TestRectangle_instantiation
    TestRectangle_width
    TestRectangle_height
    TestRectangle_x
    TestRectangle_y
    TestRectangle_order_of_initialization
    TestRectangle_area
    TestRectangle_update_args
    TestRectangle_update_kwargs
    TestRectangle_to_dictionary
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """testing rectangle istantiation unnitest"""
    def test_Rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 5), Base)

        """test private attr"""
    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 0, 0, 1).__y)

            """test the getters"""
    def test_width_getter(self):
        r = Rectangle(5, 5, 0, 0, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 5, 0, 0, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(10, 5, 0, 0, 1)
        self.assertEqual(5, r.height)

    def test_height_setter(self):
        r = Rectangle(10, 10, 0, 0, 1)
        r.height = 5
        self.assertEqual(5, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 5, 1, 0, 1)
        r.x = 0
        self.assertEqual(0, r.x)

    def test_y_getter(self):
        r = Rectangle(10, 5, 0, 0, 1)
        self.assertEqual(0, r.y)

    def test_y_setter(self):
        r = Rectangle(10, 5, 0, 1, 1)
        r.y = 0
        self.assertEqual(0, r.y)
    
    def test_order_of_initialization(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), (1, 2, 3, 4, 5))

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_update_args(self):
        r = Rectangle(1, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (2, 3, 4, 5, 6))

    def test_update_kwargs(self):
        r = Rectangle(1, 1)
        r.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (2, 3, 4, 5, 6))

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        self.assertEqual(
            r_dict, {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})


if __name__ == '__main__':
    unittest.main()