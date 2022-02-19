import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.worker = Employee('joe', 'bloggs', 25000)
    
    def test_give_default_raise(self):
        self.worker.give_raise()

        self.assertEqual(self.worker.salary, 30000)

    def test_give_custom_raise(self):
        self.worker.give_raise(10_000)

        self.assertEqual(self.worker.salary, 35000)
