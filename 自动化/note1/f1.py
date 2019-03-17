import unittest


class F1(unittest.TestCase):
    def setUp(self):
        print('开始执行')

    def tearDown(self):
        print('结束执行')

    def test_01(self):
        print('this is test01')

    def test_02(self):
        print('this is test02')

    def test_03(self):
        print('this is test03')


if __name__ == '__main__':
    unittest.main(verbosity=2)

