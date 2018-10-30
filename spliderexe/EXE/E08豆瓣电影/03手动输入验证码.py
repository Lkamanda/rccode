from selenium import webdriver
import time

username = "18612463553@163.com"
password = "hideandbush123"

def dl(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(4)
    #生成快照用来检验验证码
    driver.save_screenshot('db_dl.png')
    captcha = input("plz your yzm:")
    driver.find_element_by_xpath('//div[@class="item"]/input[@id="email"]').send_keys(username)
    driver.implicitly_wait(4)
    driver.find_element_by_xpath('//div[@class="item"]/input[@id="password"]').send_keys(password)
    driver.implicitly_wait(4)
    driver.find_element_by_xpath('//div/input[@id="captcha_field"]').send_keys(captcha)
    driver.implicitly_wait(10)
    driver.find_element_by_name("login").click()
    driver.implicitly_wait(5)
    driver.save_screenshot("db02.png")
    with open("db_dl.html", 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    driver.quit()

if __name__ == '__main__':
    url = "https://www.douban.com/accounts/login?redir=https%3A//accounts.douban.com/"
    dl(url)