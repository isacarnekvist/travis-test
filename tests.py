import unittest

from main import add


class TestCase(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(1, -2), -1)
