import unittest

class Palindrome(object):

    skipChars = [" ", ",", "!", "."]

    @staticmethod
    def is_palindrome(s):
        i = 0
        j = len(s) - 1
        while (i < len(s) and j > 0):
            if (s[i] in Palindrome.skipChars):
                i = i + 1
            elif (s[j] in Palindrome.skipChars):
                j = j - 1
            else:
                if (s[i].lower() != s[j].lower()):
                    return False
                i = i + 1
                j = j - 1
        return True

class TestPalindrome(unittest.TestCase):

    def test_a_man_no_other_chars(self):
        s = "A man a plan a canal Panama"
        self.assertTrue(Palindrome.is_palindrome(s))

    def test_amor_roma_no_other_chars(self):
        s = "Amor Roma"
        self.assertTrue(Palindrome.is_palindrome(s))

    def test_not_palindrom(self):
        s = "hello world"
        self.assertFalse(Palindrome.is_palindrome(s))
    
    def test_amor_roma(self):
        s = "Amor, Roma"
        self.assertTrue(Palindrome.is_palindrome(s))

    def test_a_man(self):
        s = "A man, a plan, a canal, Panama!"
        self.assertTrue(Palindrome.is_palindrome(s))

if __name__ == '__main__':
    unittest.main()
