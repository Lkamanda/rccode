"""
链接小米6真机
"""

import os, time, unittest
from appium import webdriver
# from LT.comm.public_element import *

# PE = Public_element()
# print(PE.get_user_avatar())


class LT(unittest.TestCase):

    # driver = None

    @classmethod
    def setUp(cls):
        # PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        # 连接手机app，初始化一些东西
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '8.0.0',
                        'deviceName': 'a82ccd1d',
                        # 'app': r'D:\apk\boobuz.apk',
                        'appPackage': 'com.erlinyou.worldlist',
                        'appActivity': 'com.erlinyou.map.Erlinyou',
                        'unicodKeyboard': 'True',
                        'resetKeyboard': 'True',
                        'noReset': 'True',
                        # 'autoGrantPermissions': 'True'
                        }
        # 手机类型
        # 被测试手机，版本
        # baa822b7   a82ccd1d Q8JNNNGUOF8L4PON   127.0.0.ce1:62001 ，
        #  设备名称， adb devices
        # \desired_caps['app'] = PATH('D:\\apk\\boobuz.apk')
        # desired_caps['appPackage'] = 'com.erlinyou.worldlist'
        # com.erlinyou.worldlist/com.erlinyou.map.MapActivity/@0xaa1e354
        # desired_caps['appActivity'] = 'com.erlinyou.map.MapActivity' #/@0xda50b9
        # appium 传输中使用自己的输入法，可以传输中文
        # 程序结束时重置原来的输入法
        # desired_caps['autoGrantPermissions'] = 'True'
        print('start')
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print('test1')
        time.sleep(10)

    @classmethod
    def tearDown(cls):
        time.sleep(2)
        cls.driver.quit()

    def test_1(self):
        print('test1')
        # self.driver.find_element_by_id().click()
        time.sleep(4)
        self.driver.find_element_by_id('user_avatar_img').click()
        time.sleep(4)
        self.driver.find_element_by_id("user_name_tv").click()
        self.driver.find_element_by_id("iv_other_login").click()
        self.driver.implicitly_wait(10)
        time.sleep(4)
        self.driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.LinearLayout[ce1]/android.widget.EditText").send_keys('1599200510')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='当前所在页面,登录微信']/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText").send_keys("5211314zxy.")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.tencent.mm:id/ch7").click()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main(verbosity=2)