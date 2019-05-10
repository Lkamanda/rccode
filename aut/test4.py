# import os
# # PATH = lambda p: os.path.join(os.path.split(os.path.dirname(__file__))[0], p)
# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
# print(PATH('./apps/HelloFreeMusic.apk'))
import time

from aut.log_ceshi import *

mylogger = Logger(logger='TestMyLog').getlog()


class TestMyLog(object):

    def print_log(self):

        print('123')
        mylogger.info("打开浏览器")


if __name__ == '__main__':
    testlog = TestMyLog()
    testlog.print_log()
