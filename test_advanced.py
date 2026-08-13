import math
import unittest

from advanced import power, square_root, factorial, absolute


class TestPower(unittest.TestCase):
    def test_positive_base_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)

    def test_negative_base_even_exponent(self):
        self.assertEqual(power(-2, 2), 4)
        self.assertEqual(power(-3, 4), 81)

    def test_negative_base_odd_exponent(self):
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-3, 3), -27)

    def test_zero_base_zero_exponent(self):
        self.assertEqual(power(0, 0), 1)

    def test_zero_base_positive_exponent(self):
        self.assertEqual(power(0, 5), 0)

    def test_one_base_any_exponent(self):
        self.assertEqual(power(1, 100), 1)

    def test_float_base(self):
        self.assertAlmostEqual(power(2.5, 2), 6.25)

    def test_float_exponent(self):
        self.assertAlmostEqual(power(4, 0.5), 2.0)

    def test_float_base_and_exponent(self):
        self.assertAlmostEqual(power(2.25, 0.5), 1.5)

    def test_negative_exponent(self):
        self.assertAlmostEqual(power(2, -1), 0.5)
        self.assertAlmostEqual(power(10, -2), 0.01)

    def test_negative_base_negative_exponent(self):
        self.assertAlmostEqual(power(-2, -2), 0.25)


class TestSquareRoot(unittest.TestCase):
    def test_positive_value(self):
        self.assertEqual(square_root(4), 2.0)
        self.assertEqual(square_root(9), 3.0)

    def test_zero(self):
        self.assertEqual(square_root(0), 0.0)

    def test_float_value(self):
        self.assertAlmostEqual(square_root(2.25), 1.5)
        self.assertAlmostEqual(square_root(0.25), 0.5)

    def test_one(self):
        self.assertEqual(square_root(1), 1.0)

    def test_negative_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_negative_float_raises_value_error(self):
        with self.assertRaises(ValueError):
            square_root(-2.5)

    def test_error_message(self):
        with self.assertRaisesRegex(ValueError, "negative number"):
            square_root(-4)


class TestFactorial(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_negative_float_raises_value_error(self):
        with self.assertRaises(ValueError):
            factorial(-3.5)

    def test_float_that_truncates_to_integer(self):
        self.assertEqual(factorial(5.0), 120)
        self.assertEqual(factorial(3.9), 6)

    def test_error_message(self):
        with self.assertRaisesRegex(ValueError, "negative numbers"):
            factorial(-2)


class TestAbsolute(unittest.TestCase):
    def test_positive_value(self):
        self.assertEqual(absolute(5), 5)

    def test_negative_value(self):
        self.assertEqual(absolute(-5), 5)

    def test_zero(self):
        self.assertEqual(absolute(0), 0)

    def test_float_value(self):
        self.assertEqual(absolute(2.5), 2.5)
        self.assertEqual(absolute(-2.5), 2.5)

    def test_large_value(self):
        self.assertEqual(absolute(-1000000), 1000000)


if __name__ == "__main__":
    unittest.main()
