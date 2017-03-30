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

        self.assertEqual('X', roman(10))
        self.assertEqual('XI', roman(11))
        self.assertEqual('XII', roman(12))
        self.assertEqual('XIII', roman(13))
        self.assertEqual('XIV', roman(14))
        self.assertEqual('XV', roman(15))
        self.assertEqual('XVI', roman(16))
        self.assertEqual('XVII', roman(17))
        self.assertEqual('XVIII', roman(18))
        self.assertEqual('XIX', roman(19))

        self.assertEqual('XX', roman(20))
        self.assertEqual('XXI', roman(21))
        self.assertEqual('XXII', roman(22))
        self.assertEqual('XXIII', roman(23))
        self.assertEqual('XXIV', roman(24))
        self.assertEqual('XXV', roman(25))
        self.assertEqual('XXVI', roman(26))
        self.assertEqual('XXVII', roman(27))
        self.assertEqual('XXVIII', roman(28))
        self.assertEqual('XXIX', roman(29))

        self.assertEqual('XXX', roman(30))
        self.assertEqual('XL', roman(40))
        self.assertEqual('L', roman(50))
        self.assertEqual('LX', roman(60))
        self.assertEqual('LXX', roman(70))
        self.assertEqual('LXXX', roman(80))
        self.assertEqual('XC', roman(90))

