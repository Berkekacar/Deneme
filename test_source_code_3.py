import unittest

class StringManipulator:

    def reverse(self, text):
        return text[::-1]

    def capitalize(self, text):
        return text.capitalize()

class TestStringManipulation(unittest.TestCase):

    def setUp(self):
        self.manipulator = StringManipulator()

    def test_reverse(self):
        self.assertEqual(self.manipulator.reverse("hello"), "olleh")

    def test_capitalize(self):
        self.assertEqual(self.manipulator.capitalize("world"), "World")

if __name__ == '__main__':
    unittest.main()
