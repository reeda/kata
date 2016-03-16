import unittest
from fizzbuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual("1", FizzBuzz.generate(1))

    def test_two(self):
        self.assertEqual("1\n2", FizzBuzz.generate(2))

    def test_three(self):
        self.assertEqual("1\n2\nFizz", FizzBuzz.generate(3))

    def test_five(self):
        self.assertEqual("1\n2\nFizz\n4\nBuzz", FizzBuzz.generate(5))

    def test_fifteen(self):
        self.assertEqual("1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz", FizzBuzz.generate(15))

if __name__ == '__main__':
    unittest.main()
