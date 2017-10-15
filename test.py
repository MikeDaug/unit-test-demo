## demo from http://www.onlamp.com/pub/a/python/2004/12/02/tdd_pyunit.html

import unittest

class FooTests(unittest.TestCase):

    def testMatches(self):
        p = DatePattern(2004, 9, 28)
        d = datetime.date(2004, 9, 28)
        self.failUnless(p.matches(d))

def main():
    unittest.main()

if __name__ == '__main__':
    main()



