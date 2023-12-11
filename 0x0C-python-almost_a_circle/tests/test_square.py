from models.square import Square
import unittest

class TestSquareInstantiation(unittest.TestCase):
    """Testing square instantiation unittests"""

    def test_Square_is_Base(self):
        self.assertIsInstance(Square(5), Base)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(5, 0, 0, 1).__size)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Square(5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Square(5, 0, 0, 1).__y)

    def test_size_getter(self):
        s = Square(5, 0, 0, 1)
        self.assertEqual(5, s.size)

    def test_size_setter(self):
        s = Square(5, 0, 0, 1)
        s.size = 10
        self.assertEqual(10, s.size)

    def test_x_getter(self):
        s = Square(5, 7, 5, 1)
        self.assertEqual(7, s.x)

    def test_x_setter(self):
        s = Square(5, 1, 0, 1)
        s.x = 0
        self.assertEqual(0, s.x)

    def test_y_getter(self):
        s = Square(5, 0, 3, 1)
        self.assertEqual(3, s.y)

    def test_y_setter(self):
        s = Square(5, 0, 1, 1)
        s.y = 0
        self.assertEqual(0, s.y)

    def test_order_of_initialization(self):
        s = Square(5, 3, 4, 5)
        self.assertEqual((s.size, s.x, s.y, s.id), (5, 3, 4, 5))

    def test_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_update_args(self):
        s = Square(1)
        s.update(2, 3, 4, 5)
        self.assertEqual((s.id, s.size, s.x, s.y), (2, 3, 4, 5))

    def test_update_kwargs(self):
        s = Square(1)
        s.update(id=2, size=3, x=4, y=5)
        self.assertEqual((s.id, s.size, s.x, s.y), (2, 3, 4, 5))

    def test_to_dictionary(self):
        s = Square(2, 3, 4, 5)
        s_dict = s.to_dictionary()
        self.assertEqual(
            s_dict, {'id': 5, 'size': 2, 'x': 3, 'y': 4})


if __name__ == '__main__':
    unittest.main()