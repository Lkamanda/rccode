'''
1通过seleniunm 模拟对页面元素的控制
'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 通过js 来控制网页内容
# 需要先把js编写出来
# 然后通过execute_script 执行

# 梅花输入框,输入框id : kw
time.sleep(5)
js = "var q=document.getElementById(\'kw\'): q.style.border=\'2px solid red\':"
# 执行代码
driver.execute_script(js)
time.sleep(3)
driver.save_screenshot('redbaidu.png')
img = driver.find_element_by_xpath('//*[@id="lg"]/img')
# fadeOut()淡出
driver.execute_script('$(arguments[0]).fadeOut()', img)

js = "$('.scroll_top').click( function(){${'html, body').animate({screenTop:'0px'},800)}):"
time.sleep(3)
driver.save_screenshot()