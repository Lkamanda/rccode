# 类方法
from selenium import webdriver
import unittest


class F2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get('http://www.baidu.com')
        print('开始执行')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        '''百度新闻测试'''
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.back()

    '''百度首页'''
    def test_02(self):
        '''百度首页:百度地图测试'''
        self.driver.find_element_by_link_text('地图').click()
        self.driver.back()

    def test_03(self):
        '''百度首页:百度错误测试'''
        self.driver.find_element_by_link_text('视频').click()
        self.driver.back()
        

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    # 生成类实例
    suit = unittest.TestSuite()
    # 将测试用例添加到测试套件中
    # 先添加的先执行
    suit.addTest(F2('test_01'))
    suit.addTest(F2('test_02'))
    # suit.addTest(F2('test_03'))
    # 执行测试套件
    unittest.TextTestRunner(verbosity=2).run(suit)