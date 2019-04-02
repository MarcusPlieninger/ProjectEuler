import unittest
from problem001_multiplesof3and5 import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solution(10), 23)

    def test_example2(self):
        self.assertEqual(solution(1000), 233168)

if __name__ == '__main__':
    unittest.main()