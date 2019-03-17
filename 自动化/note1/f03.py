import unittest


class F3(unittest.TestCase):
    def setUp(self):
        print('setup')
        pass

    def tearDown(self):
        print('teardown')
        pass

    def test01(self):
        print('test01')
        pass

    def test02(self):
        print('test02')
        pass


if __name__ == '__main__':
    suit = unittest.TestSuite(unittest.makeSuite(F3))
    unittest.TextTestRunner(verbosity=2).run(suit)

