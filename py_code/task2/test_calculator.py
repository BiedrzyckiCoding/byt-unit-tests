import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        calc = Calculator(10, 5, "+")
        self.assertEqual(calc.calculate(), 15)

    def test_subtraction(self):
        calc = Calculator(10, 5, "-")
        self.assertEqual(calc.calculate(), 5)

    def test_multiplication(self):
        calc = Calculator(10, 5, "*")
        self.assertEqual(calc.calculate(), 50)

    def test_division(self):
        calc = Calculator(10, 2, "/")
        self.assertEqual(calc.calculate(), 5)

    #division by zero
    def test_division_by_zero(self):
        calc = Calculator(10, 0, "/")
        with self.assertRaises(ZeroDivisionError):
            calc.calculate()

    #wrong operator
    def test_invalid_operation(self):
        calc = Calculator(10, 5, "%")
        with self.assertRaises(ValueError):
            calc.calculate()

    #negative numbers
    def test_negative_numbers(self):
        calc = Calculator(-10, -5, "+")
        self.assertEqual(calc.calculate(), -15)

    #float inputs -> TODO: change so that this is allowed normally, floats and negative numbers should be ok
    def test_float_inputs(self):
        calc = Calculator(2.5, 0.5, "*")
        self.assertAlmostEqual(calc.calculate(), 1.25)

    #large number test
    def test_large_numbers(self):
        calc = Calculator(10**10, 10**10, "+")
        self.assertEqual(calc.calculate(), 2 * 10**10)

    #mixed types -> TODO: also should be okay
    def test_mixed_types(self):
        calc = Calculator(10, 2.5, "/")
        self.assertEqual(calc.calculate(), 4)

    #more edge cases:
    def test_zero_zero_add(self):
        calc = Calculator(0, 0, "+")
        self.assertEqual(calc.calculate(), 0)

    def test_zero_zero_multiply(self):
        calc = Calculator(0, 0, "*")
        self.assertEqual(calc.calculate(), 0)

    def test_zero_plus_positive(self):
        calc = Calculator(0, 10, "+")
        self.assertEqual(calc.calculate(), 10)

    def test_zero_minus_positive(self):
        calc = Calculator(0, 10, "-")
        self.assertEqual(calc.calculate(), -10)

    def test_positive_minus_zero(self):
        calc = Calculator(10, 0, "-")
        self.assertEqual(calc.calculate(), 10)

    def test_positive_times_zero(self):
        calc = Calculator(10, 0, "*")
        self.assertEqual(calc.calculate(), 0)

    def test_small_floats(self):
        calc = Calculator(0.0000001, 0.0000002, "+")
        self.assertAlmostEqual(calc.calculate(), 0.0000003)

    def test_large_floats(self):
        calc = Calculator(1e308, 1e308, "+")
        self.assertEqual(calc.calculate(), float("inf"))

    def test_large_multiplication_overflow(self):
        calc = Calculator(1e308, 2, "*")
        self.assertEqual(calc.calculate(), float("inf"))

    def test_negative_divided_by_positive(self):
        calc = Calculator(-10, 2, "/")
        self.assertEqual(calc.calculate(), -5)

    def test_positive_divided_by_negative(self):
        calc = Calculator(10, -2, "/")
        self.assertEqual(calc.calculate(), -5)

    def test_negative_divided_by_negative(self):
        calc = Calculator(-10, -2, "/")
        self.assertEqual(calc.calculate(), 5)

    def test_lowercase_operation(self):
        calc = Calculator(10, 5, "x")
        with self.assertRaises(ValueError):
            calc.calculate()

    def test_none_operation(self):
        calc = Calculator(10, 5, None)
        with self.assertRaises(ValueError):
            calc.calculate()

    def test_operation_wrong_type(self):
        calc = Calculator(10, 5, 1)
        with self.assertRaises(ValueError):
            calc.calculate()

    def test_operand_is_string(self):
        calc = Calculator("a", 5, "+")
        with self.assertRaises(TypeError):
            calc.calculate()

    def test_int_division_result_float(self):
        calc = Calculator(3, 2, "/")
        self.assertEqual(calc.calculate(), 1.5)

    def test_division_result_infinity(self):
        calc = Calculator(1, 1e-308, "/")
        self.assertTrue(calc.calculate() > 1e307)

    def test_nan_input(self):
        import math
        calc = Calculator(math.nan, 1, "+")
        result = calc.calculate()
        self.assertTrue(math.isnan(result))

    def test_huge_plus_small(self):
        calc = Calculator(1e308, 1e-308, "+")
        self.assertEqual(calc.calculate(), 1e308)

if __name__ == "__main__":
    unittest.main(verbosity=2)
