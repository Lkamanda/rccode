# from selenium import webdriver
# import time
#
#
# def get_baidu():
#     driver = webdriver.Firefox()
#     driver.get('https://www.baidu.com/')
#     # x = "kw"
#     driver.find_element_by_id('kw').send_keys('测试')
#     time.sleep(10)
#     driver.quit()
#
#
# if __name__ == '__main__':
#     get_baidu()

import unittest

#整个文件的开始和结束执行
def setUpModule():
    print("test module start >>>>>>>>>>>>>>")

def tearDownModule():
    print("test module end >>>>>>>>>>>>>>")

class Test(unittest.TestCase):

    #整个Test类的开始和结束执行
    @classmethod
    def setUpClass(cls):
        print("test class start =======>")

    @classmethod
    def tearDownClass(cls):
        print("test class end =======>")

    #每个用例的开始和结束执行
    def setUp(self):
        print("test case start -->")

    def tearDown(self):
        print("test case end -->")

    def test_case(self):
        print("test case1")

    def test_case2(self):
        print("test case2")

if __name__ == '__main__':
    unittest.main()