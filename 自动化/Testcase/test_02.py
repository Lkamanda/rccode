import unittest
from selenium import webdriver


def add(a, b):
    return a-b


class Baidu(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
        print('1')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print('2')
    @unittest.expectedFailure
    def test01(self):
        self.assertEqual(add(2-3), 1)

    def test02(self):
        so = self.driver.find_element_by_id('kw')
        self.assertFalse(so.is_enabled())

    def test03(self):
        so = self.driver.find_element_by_id('kw')
        self.assertTrue(so.is_enabled())

    def test04(self):
        self.assertIn('百度', self.driver.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)