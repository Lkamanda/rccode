"""
执行所有测试用文件
"""
import unittest
import os
import sys
import time


def allTests():
    """
    start_dir:获取本地路径   # 获取当前文件路径 os.path.dirname(__file__)
    pattern:正则表达式找到所有的执行文件
    return: 返回所有测试测试用例包
    """
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite


def run():
    fp = os.path.join(os.path.dirname(__file__), 'report', 'TestReportHtml')
    HTMLTestRunner.HTMLTestRunner(stream=open(fp, 'wb'), title='自动化测试报告', description='填写描述').run(allTests())
    # unittest.TextTestRunner(verbosity=2).run(allTests())


if __name__ == '__main__':
    run()
    # 获取当前时间戳
    # print(time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time())))