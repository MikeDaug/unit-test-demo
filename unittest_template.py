## demo from http://www.onlamp.com/pub/a/python/2004/12/02/tdd_pyunit.html
## unittest template

import unittest

class FooTests(unittest.TestCase):

    def testFoo(self):
        self.failUnless(False)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
