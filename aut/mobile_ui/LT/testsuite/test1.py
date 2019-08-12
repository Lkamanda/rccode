import time
from appium import webdriver
desired_caps = {}

desired_caps['resetKeyboard'] = 'True'# 手机类型
desired_caps['platformName'] = 'Android'
# 被测试手机，版本
desired_caps['platformVersion'] = '5.1.1'
# baa822b7   a82ccd1d Q8JNNNGUOF8L4PON   127.0.0.1:62001 ，
#  设备名称， adb devices
desired_caps['deviceName'] = '127.0.0.1:62001'
#\desired_caps['app'] = PATH('D:\\apk\\boobuz.apk')
# desired_caps['app'] = r'D:\apk\boobuz.apk'
desired_caps['appPackage'] = 'com.erlinyou.worldlist'
# com.erlinyou.worldlist/com.erlinyou.map.MapActivity/@0xaa1e354
desired_caps['appActivity'] = 'com.erlinyou.map.MapActivity' #/@0xda50b9
# appium 传输中使用自己的输入法，可以传输中文
desired_caps['unicodKeyboard'] = 'True'
# 程序结束时重置原来的输入法'
desired_caps['noReset'] = 'True'
desired_caps['autoGrantPermissions'] = 'True'
time.sleep(5)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)

driver.quit()