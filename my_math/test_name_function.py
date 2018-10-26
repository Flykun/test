import unittest
from my_math.math_function import product


class ProductTestCase(unittest.TestCase):
    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = product(x, y)
                self.assertEqual(p, x * y)

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10
                y = y / 10
                p = product(x, y)
                self.assertEqual(p, x * y)


if __name__ == '__main__':
    unittest.main()
