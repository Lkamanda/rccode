

import os, time, unittest
from appium import webdriver



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

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# self.driver.find_element_by_id().click()
time.sleep(4)
driver.find_element_by_id('user_avatar_img').click()
time.sleep(4)
driver.find_element_by_id("user_name_tv").click()
# self.driver.find_element_by_id("iv_other_login").click()
# self.driver.implicitly_wait(10)
# time.sleep(4)
# self.driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText").send_keys('1599200510')
# self.driver.implicitly_wait(10)
# self.driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='当前所在页面,登录微信']/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText").send_keys("5211314zxy.")
# self.driver.implicitly_wait(10)
# self.driver.find_element_by_id("com.tencent.mm:id/ch7").click()
# time.sleep(10)


