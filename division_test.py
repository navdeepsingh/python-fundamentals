import unittest
import division

class TestDivision(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(division.is_divide_by(10, 2), True)
        self.assertEqual(division.is_divide_by(10, 3), False, 'Should return False if 10 is divisible by 3')
        
if __name__ == '__main__':
    unittest.main()