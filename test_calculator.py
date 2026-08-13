import unittest

from calculator import add, subtract, multiply, modulo


class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-2, 3), 1)

    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)


class TestSubtract(unittest.TestCase):
    def test_subtract_positive(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-2, -3), 1)
        self.assertEqual(subtract(2, -3), 5)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(5.5, 2.1), 3.4)

    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)


class TestMultiply(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)


class TestModulo(unittest.TestCase):
    def test_modulo_positive(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_modulo_negative(self):
        self.assertEqual(modulo(-10, 3), 2)
        self.assertEqual(modulo(10, -3), -2)

    def test_modulo_floats(self):
        self.assertAlmostEqual(modulo(5.5, 2), 1.5)

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modulo(5, 0)

    def test_modulo_zero_dividend(self):
        self.assertEqual(modulo(0, 5), 0)


if __name__ == "__main__":
    unittest.main()
