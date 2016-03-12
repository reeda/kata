import unittest
from prime_factors import PrimeFactors

class PrimeFactorsTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(self.prime_list(), PrimeFactors.generate(1))

    def test_two(self):
        self.assertEqual(self.prime_list(2), PrimeFactors.generate(2))

    def test_three(self):
        self.assertEquals(self.prime_list(3), PrimeFactors.generate(3))

    def test_four(self):
        self.assertEqual(self.prime_list(2,2), PrimeFactors.generate(4))

    def test_six(self):
        self.assertEqual(self.prime_list(2,3), PrimeFactors.generate(6))

    def test_eight(self):
        self.assertEqual(self.prime_list(2,2,2), PrimeFactors.generate(8))

    def test_nine(self):
        self.assertEqual(self.prime_list(3,3), PrimeFactors.generate(9))

    def prime_list(self, *args):
        listy = []
        for i in args:
            listy.append(i)
        return listy

if __name__ == '__main__':
    unittest.main()
