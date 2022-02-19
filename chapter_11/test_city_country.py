import unittest

from city_functions import city_function

class TestCityFunction(unittest.TestCase):
    def test_returns_string(self):
        """Do places like 'La Paz, Bolivia' work?"""
        output = city_function('la paz', 'bolivia')
        self.assertEqual(output, 'La Paz, Bolivia')