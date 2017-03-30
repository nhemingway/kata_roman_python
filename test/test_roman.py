#!/usr/bin/env python

import unittest

from roman import roman

class TestRoman(unittest.TestCase):
    def test_roman(self):
        with self.assertRaises(ValueError):
            roman(0)

        self.assertEqual('I', roman(1))
