from selenium import webdriver
import pytesseract as pt
from PIL import Image
import requests
import time
from lxml import etree


username = "18612463553@163.com"
password = "hideandbush123"
# 得到图片
def get_image(image_url):
    rsp = requests.get(image_url)
    with open('YM_01.png', 'wb') as f:
        # 对于图片的类型的通过rsp.content方式访问响应内容,将响应内容写入YM_01png中
        f.write(rsp.content)
    global n
    n = 'YM_01.png'
    return n
def pt_image(n):
    image = Image.open(n)
    global ym
    ym = pt.image_to_string(image)
    print(ym)
def content_parse(fn):
    html = ''
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
    # 生成xml树
    global tree
    tree = etree.HTML(html)

def dl_douban(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath('//div[@class="item"]/input[@id="email"]').send_keys(username)
    driver.implicitly_wait(4)
    driver.find_element_by_xpath('//div[@class="item"]/input[@id="password"]').send_keys(password)

    #image_url = driver.find_element_by_xpath('//div/img[@id="captcha_image"]')
    fn = 'douban_reader_html'
    with open(fn, 'w', encoding="utf-8") as f:
        # 把的到页面源码写入fn
        f.write(driver.page_source)
    content_parse(fn)
    image_url = tree.xpath('//div/img[@id="captcha_image"]/@src')[0]
    print(image_url)
    time.sleep(4)
    # 的到图片
    get_image(image_url)
    # 识别图片,并返回图片内容
    time.sleep(4)
    pt_image(n)
    time.sleep(4)
    print(ym)
    driver.find_element_by_xpath('//div/input[@id="captcha_field"]').send_keys(ym)
    driver.implicitly_wait(10)
    driver.find_element_by_name("login").click()
    driver.implicitly_wait(5)
    driver.save_screenshot("db02.png")
    driver.quit()

if __name__ == '__main__':
    url ="https://www.douban.com/accounts/login?redir=https%3A//accounts.douban.com/"
    dl_douban(url)

# 由于pytesseract 提取图片失败,执行失败