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

        self.assertEqual('C', roman(100))
        self.assertEqual('CX', roman(110))
        self.assertEqual('CXX', roman(120))
        self.assertEqual('CXXX', roman(130))
        self.assertEqual('CXL', roman(140))
        self.assertEqual('CL', roman(150))
        self.assertEqual('CLX', roman(160))
        self.assertEqual('CLXX', roman(170))
        self.assertEqual('CLXXX', roman(180))
        self.assertEqual('CXC', roman(190))

        self.assertEqual('CC', roman(200))
        self.assertEqual('CCC', roman(300))
        self.assertEqual('CD', roman(400))
        self.assertEqual('D', roman(500))
        self.assertEqual('DC', roman(600))
        self.assertEqual('DCC', roman(700))
        self.assertEqual('DCCC', roman(800))
        self.assertEqual('CM', roman(900))

        self.assertEqual('M', roman(1000))
        self.assertEqual('MC', roman(1100))
        self.assertEqual('MCC', roman(1200))
        self.assertEqual('MCCC', roman(1300))
        self.assertEqual('MCD', roman(1400))
        self.assertEqual('MD', roman(1500))
        self.assertEqual('MDC', roman(1600))
        self.assertEqual('MDCC', roman(1700))
        self.assertEqual('MDCCC', roman(1800))
        self.assertEqual('MCM', roman(1900))

        self.assertEqual('MM', roman(2000))
        self.assertEqual('MMM', roman(3000))

        self.assertEqual('CCCXCIX', roman(399))
        self.assertEqual('MCMLXIX', roman(1969))
        self.assertEqual('MCMXCVIII', roman(1998))
        self.assertEqual('MMMCMXCIX', roman(3999))

        with self.assertRaises(ValueError):
            roman(4000)

