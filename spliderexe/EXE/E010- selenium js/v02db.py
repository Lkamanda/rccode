'''
1.利用selenium 模拟鼠标下拉
2.每次多出先几部电影的信息

'''
from selenium import webdriver
import time
url = "https://movie.douban.com/explore#!type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start=0"
driver = webdriver.Chrome()
driver.get(url)

# 向下滚动10000像素
js = 'document.body.scrollTop=1000'
time.sleep(2)
driver.save_screenshot('douban1.png')
driver.execute_script(js)
time.sleep(3)
driver.save_screenshot('douban2.png')
driver.quit()