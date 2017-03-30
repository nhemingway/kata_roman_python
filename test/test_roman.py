#!/usr/bin/env python

import unittest

from roman import roman

class TestRoman(unittest.TestCase):
    def test_roman(self):
        self.assertEqual('I', roman(1))
