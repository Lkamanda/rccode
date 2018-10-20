'''
webdriver 操作phantomjs
'''
from selenium import webdriver
import time

# 通过keys模拟键盘
from selenium.webdriver.common.keys import Keys
# 操作那个浏览器对哪个浏览器创建一个实例
# 自动按照环境变量查找浏览器
driver = webdriver.PhantomJS()
driver.get("https://www.baidu.com")
# 如果浏览器没有在响应的环境变量中,需要指定浏览器位置
# 通过函数查找title标签
print("Title:{0}".format(driver.title))