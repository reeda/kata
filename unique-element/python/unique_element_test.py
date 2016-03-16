import unittest
from unique_element import UniqueElement

class UniqueElementTest(unittest.TestCase):
    def test_112233445556(self):
        input = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
        self.assertEqual(6, UniqueElement.find(input))

    def test_12233445566(self):
        input = [1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6]
        self.assertEqual(1, UniqueElement.find(input))

if __name__ == '__main__':
    unittest.main()
