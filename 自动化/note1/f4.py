from init import *
import unittest


class F4(Init):

    def test_01(self):
        print('test01')

    def test_02(self):
        print('test02')

    @staticmethod
    def suite():
        suite = unittest.TestSuite(unittest.makeSuite(F4))
        return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(F4.suite())
        