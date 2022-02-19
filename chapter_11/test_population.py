import unittest

from population import city_function

class TestCityFunction(unittest.TestCase):
    def test_returns_string(self):
        """Do places like 'La Paz, Bolivia' work?"""
        output = city_function('la paz', 'bolivia')
        self.assertEqual(output, 'La Paz, Bolivia - population unknown')
    
    def test_returns_inputted_population(self):
        """Does it recognise user input?"""
        output = city_function('santiago', 'chile', population=5_000_000)
        self.assertEqual(output, 'Santiago, Chile - population 5000000')