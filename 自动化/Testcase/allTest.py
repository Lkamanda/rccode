"""
执行所有测试用文件
"""
import unittest
import os


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
    unittest.TextTestRunner(verbosity=2).run(allTests())


if __name__ == '__main__':
    run()