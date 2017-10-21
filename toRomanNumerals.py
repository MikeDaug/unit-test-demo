# -*- coding: utf-8 -*-
# learn python the hard way
# toRomanNumeral.py
# Copyright 2017 by Mike Daugherty (mikedaug@yahoo.com)
# last modified on: 2017-10-02 Mon 08:03 PM
##
##
# https://learnpythonthehardway.org/book/
# note: python good coding practice to never have a line over eighty chars long
# 345678901234567890123456789012345678901234567890123456789012345678901234567890
##
import unittest

# My program code here
#################################################

# special roman numerals
# if 1, return 'I' and subtract 1 from x
# if 5, return 'V' and subtract 5 from x
# if 10, return 'X' and subtract 10 from x
# if 50, return 'L' and subtract 50 from x
# if 100, return 'C' and subtract 100 from x
# if 1000, return 'M' and subtract 1000 from x


def convert_to_roman(x):
    roman = ''
    while x > 0:
        if x >= 50:
            roman += 'L'
            x -= 50
        elif x >= 40:
            roman += 'XL'
            x -= 40
        elif x >= 10:
            roman += 'X'
            x = x - 10
        elif x == 9:
            roman += 'IX'
            x = x - 9
        elif x >= 5:
            roman += 'V'
            x = x - 5
        elif x == 4:
            roman += 'IV'
            x = x - 4
        elif x >= 1:
            roman += 'I'
            x = x - 1
    return roman


# My unit tests here...
#################################################
class convert_to_roman_tests(unittest.TestCase):

    def testOne(self):
        self.failUnless(convert_to_roman(1) == 'I')

    def testTwo(self):
        self.failUnless(convert_to_roman(2) == 'II')

    def testThree(self):
        self.failUnless(convert_to_roman(3) == 'III')

    def testFour(self):
        self.failUnless(convert_to_roman(4) == 'IV')

    def testFive(self):
        self.failUnless(convert_to_roman(5) == 'V')

    def testSix(self):
        self.failUnless(convert_to_roman(6) == 'VI')

    def testSeven(self):
        self.failUnless(convert_to_roman(7) == 'VII')

    def testEight(self):
        self.failUnless(convert_to_roman(8) == 'VIII')

    def testNine(self):
        self.failUnless(convert_to_roman(9) == 'IX')

    def testTen(self):
        self.failUnless(convert_to_roman(10) == 'X')

    def testEleven(self):
        self.failUnless(convert_to_roman(11) == 'XI')

    def testTwentyFour(self):
        self.failUnless(convert_to_roman(24) == 'XXIV')

    def testTwentyFive(self):
        self.failUnless(convert_to_roman(25) == 'XXV')

    def testThirtySeven(self):
        self.failUnless(convert_to_roman(37) == 'XXXVII')

    def testThirtyNine(self):
        self.failUnless(convert_to_roman(39) == 'XXXIX')

    def testForty(self):
        self.failUnless(convert_to_roman(40) == 'XL')

    def testEightyThree(self):
        self.failUnless(convert_to_roman(83) == 'LXXXIII')

    def testEightyNine(self):
        self.failUnless(convert_to_roman(89) == 'LXXXIX')

def main():
    unittest.main()


if __name__ == '__main__':
    main()
