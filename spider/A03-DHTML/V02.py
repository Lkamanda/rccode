from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 可能需要手动添加路径
driver = webdriver.Chrome()
url = "http://www.baidu.com"
driver.get(url)
text = driver.find_element_by_id('wrapper').text
print(text)
print(driver.title)
# 截屏
driver.save_screenshot("index.png")
driver.find_element_by_id("kw").send_keys(u"大熊猫")

# id= "su"是百度收搜的按钮
driver.find_element_by_id("su").click()
time.sleep(5)
driver.save_screenshot("daxiongmao.png")

# 读取当前页面cookie

print(driver.get_cookies())
d = driver.get_cookies()
print(type(d))

#  模拟输入俩个按键 ctrl +a
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "a")
# ctrl+ x
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, "x")
# 清空输入框
driver.find_element_by_id("kw").clear()
# 退出驱动关闭窗口
driver.quit()
#关闭窗口
#driver.close()