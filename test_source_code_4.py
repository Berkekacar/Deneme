import unittest

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

class TestTemperatureConversion(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(0), 32, places=2)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(TemperatureConverter.fahrenheit_to_celsius(32), 0, places=2)

if __name__ == '__main__':
    unittest.main()
