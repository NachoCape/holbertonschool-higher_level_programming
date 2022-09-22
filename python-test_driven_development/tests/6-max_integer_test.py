#!/usr/bin/python3
"""task6 module"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([]), None)
