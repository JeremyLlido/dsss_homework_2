import unittest
from math_quiz import generation_random_integer, random_operator_selection, elementary_operation_calculations

class TestMathGame(unittest.TestCase):

    def test_generation_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generation_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator_selection(self):
        # Test if the function returns a valid operator (+, -, *)
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = random_operator_selection()
            self.assertIn(operator, valid_operators)

    def test_elementary_operation_calculations(self):
        # Test different cases for elementary_operation_calculations
        test_cases = [
            (5, 2, '+', '5 + 2', 7), # expected result is 7
            (7, 3, '-', '7 - 3', 4),
            (4, 6, '*', '4 * 6', 24)
        ]

        for num1, num2, operator, expected_calculation, expected_result in test_cases:
            
            # Generation of a calculation and the associated result
            calculation, result = elementary_operation_calculations(num1, num2, operator)
            self.assertEqual(calculation, expected_calculation)  # Check the calculation string
            self.assertEqual(result, expected_result)  # Check the calculated result

if __name__ == "__main__":
    unittest.main()
