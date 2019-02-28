from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions  as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from bs4 import BeautifulSoup

browser = webdriver.Chrome()

url = 'https://music.163.com/#/playlist?id=2521554648'

browser.get(url=url)
sleep(10)
source = browser.page_source
browser.find_element_by_xpath('//span[@class="txt"/a]').get_attribute('href')


# soup = BeautifulSoup(source)
# items = soup.find_all('span', {'class': 'txt'})
# print(items)
# for item in items:
#     href = item.find_all('a')[0].get('href')
#     print(href)
#

