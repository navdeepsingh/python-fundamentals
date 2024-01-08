import unittest
import my_math_functions

class TestMyMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(my_math_functions.add(1, 2), 3)
        self.assertEqual(my_math_functions.add(1, 3), 4)
        self.assertEqual(my_math_functions.add(1, 4), 5)
        self.assertEqual(my_math_functions.add(1, 5), 6)

    def test_multiply(self):
        self.assertEqual(my_math_functions.multiply(2, 3), 6)
        self.assertEqual(my_math_functions.multiply(2, 4), 8)
        self.assertEqual(my_math_functions.multiply(2, 5), 10)
        self.assertEqual(my_math_functions.multiply(2, 6), 12)