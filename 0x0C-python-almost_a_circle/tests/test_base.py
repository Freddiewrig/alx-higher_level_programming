from models.base import Base
import unittest

class TestBaseInstantiation(unittest.TestCase):
    """Testing Base instantiation unittests"""

    def test_id_incrementation(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_manual_assignment(self):
        b1 = Base(10)
        b2 = Base(20)
        b3 = Base()
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)
        self.assertEqual(b3.id, 1)

    def test_id_negative_assignment(self):
        b1 = Base(-5)
        b2 = Base(-10)
        b3 = Base()
        self.assertEqual(b1.id, -5)
        self.assertEqual(b2.id, -10)
        self.assertEqual(b3.id, 1)

    def test_id_string_assignment(self):
        b1 = Base("abc")
        b2 = Base("xyz")
        b3 = Base()
        self.assertEqual(b1.id, "abc")
        self.assertEqual(b2.id, "xyz")
        self.assertEqual(b3.id, 1)

if __name__ == '__main__':
    unittest.main()