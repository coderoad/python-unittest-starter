import unittest
from .context import src

class MathTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(src.Add(1, 2), 3, "Should add two numbers together")
    def test_subtract(self):
        self.assertEqual(src.Subtract(5, 3), 2, "Should subtract the first number from the second")