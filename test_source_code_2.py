import unittest

def is_even(number):
    return number % 2 == 0

class TestEvenNumber(unittest.TestCase):

    def test_positive_even(self):
        self.assertTrue(is_even(4))

    def test_positive_odd(self):
        self.assertFalse(is_even(7))

    def test_negative_even(self):
        self.assertTrue(is_even(-2))

if __name__ == '__main__':
    unittest.main()
