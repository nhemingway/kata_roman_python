#!/usr/bin/env python

import unittest

from roman import roman

class TestRoman(unittest.TestCase):
    def test_roman(self):
        with self.assertRaises(ValueError):
            roman(0)

        self.assertEqual('I', roman(1))
        self.assertEqual('II', roman(2))
        self.assertEqual('III', roman(3))
        self.assertEqual('IV', roman(4))
        self.assertEqual('V', roman(5))
        self.assertEqual('VI', roman(6))
        self.assertEqual('VII', roman(7))
        self.assertEqual('VIII', roman(8))
        self.assertEqual('IX', roman(9))
