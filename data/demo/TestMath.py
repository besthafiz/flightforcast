# create test case for TestMath.py on unittest
import unittest
from Math import Math

class TestMath(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(Math.mean([2, 4]), 3)
        self.assertEqual(Math.mean([2, 4, 6]), 4)
        self.assertEqual(Math.mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(Math.mean([1, 3, 5, 7, 9]), 5)
        self.assertEqual(Math.mean([1, 1, 2, 3, 5, 8]), 3.5)

    def test_median(self):

        self.assertEqual(Math.median([1, 10, 2, 9, 5]), 5)
        self.assertEqual(Math.median([1, 9, 2, 10]), (2 + 9) / 2)
        self.assertEqual(Math.median([7, 12, 3, 1, 6]), 6)
        self.assertEqual(Math.median([7, 3, 1, 4]), 3.5)
        self.assertEqual(Math.median([7, 3, 1, 4, 2]), 3)

#  create test case for mean for outside range values

    def test_mean_outside_range(self):

        with self.assertRaises(ValueError):
            Math.mean([])

        with self.assertRaises(ValueError):
            Math.mean([1, 2, 'a'])
            
if __name__ == '__main__':
    unittest.main()
