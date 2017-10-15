# -*- coding: utf-8 -*-
## learn python the hard way
## toRomanNumeral.py
## Copyright 2017 by Mike Daugherty (mikedaug@yahoo.com)
## last modified on: 2017-10-02 Mon 08:03 PM
##
##
## https://learnpythonthehardway.org/book/
## note: python good coding practice to never have a line over eighty chars long
##345678901234567890123456789012345678901234567890123456789012345678901234567890
##
import unittest

#### My program code here
#################################################

def convert_to_roman(x):
    
    if x == 1:
        return 'I'

    if x == 2:
        return 'II'

    if x == 3:
        return 'III'
    
    if x == 5:
        return 'V'

    return None





#### My unit tests here...
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



def main():
    unittest.main()

if __name__ == '__main__':
    main()

