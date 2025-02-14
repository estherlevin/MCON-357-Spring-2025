import unittest
from sys import getrecursionlimit

import exercises.calculate_factorial
from exercises.calculate_factorial import factorial_recursive
from exercises.calculate_factorial import process_input

class MyTestCase(unittest.TestCase):
    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(5), 120)  # add assertion here
    def test_process_input_negative_value(self):
        value, error_message = process_input("-2")
        self.assertIsNone(value)
        self.assertEqual(error_message,"Number must be a positive integer.")
    def test_factorial_recursive_of_zero(self):
        self.assertEqual(factorial_recursive(0), 1)
    def test_factorial_recursive_of_one(self):
        self.assertEqual(factorial_recursive(1), 1)
    def test_process_input_for_fraction(self):
        value, error_message = process_input("3.4")
        self.assertIsNone(value)
        self.assertEqual(error_message,"Number must be a positive integer.")
    def test_factorial_recursive_of_large_number(self):
        self.assertEqual(factorial_recursive(11),39916800)
    def test_factorial_recursive_before_limit(self):
        test_value = getrecursionlimit() - 20 # just below the limit
        result = factorial_recursive(test_value)
        self.assertIsInstance(result, int)  # will be equal to an int value

    def test_factorial_recursive_at_or_above_limit(self):
        test_value = getrecursionlimit() + 50  # beyond recursion limit
        #handles gracefully with the error
        with self.assertRaises(RecursionError):
            factorial_recursive(test_value)

if __name__ == '__main__':
    unittest.main()
