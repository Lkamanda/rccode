import os, time, unittest
from selenium import webdriver

class LT(unittest.TestCase):
    @classmethod
    def setUp(self):
        # PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Q8JNNNGUOF8L4PON', #Redmi Note4
            'platformVersion': '6.0',
            'appPackage': 'com.erlinyou.worldlist',
            'appActivity': 'com.erlinyou.map.MapActivity',
        }
        time.sleep(10)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)


    def test1(self):
        print('test1')

    @classmethod
    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()