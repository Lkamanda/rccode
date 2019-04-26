import os, time, unittest
from appium import webdriver


# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': '127.0.0.1:62001', #Redmi Note4
#     'platformVersion': '5.1',
#     'appPackage': 'com.erlinyou.worldlist',
#     'appActivity': 'com.erlinyou.map.SplashActivity',
#
# }
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '127.0.0.1:62001' # baa822b7   a82ccd1d Q8JNNNGUOF8L4PON   127.0.0.1:62001
desired_caps['app'] = r'D:\apk\boobuz.apk'
# desired_caps['appPackage'] = 'com.miui.calculator'
# desired_caps['appActivity'] = 'com.miui.calculator.cal.CalculatorActivity' #/@0xda50b9
desired_caps['unicodKeyboard'] = 'True'
desired_caps['resetKeyboard'] ='True'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)

print('test1')
