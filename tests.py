import unittest

from main import add, times


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(1, -2), -1)

    def test_times(self):
        self.assertEqual(times(2, 2), 4)
        self.assertEqual(times(1, -1), -1)
        self.assertEqual(times(-1, -1), 1)
