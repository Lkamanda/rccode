import unittest

class test_baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(1)

    @classmethod
    def tearDownClass(cls):
        print(2)

    def test1(self):
        print('test1')

    def test2(self):
        print('test2')

if __name__ == '__main__':
    unittest.main(verbosity=2)

