import logging
import os
from comm.common import str_nowTime


class Logger(object):
    def __init__(self):
        """
        指定保存的日志文件的粒径，日志级别，调用文件
        将日志存入指定的文件中
        :param logger:
        """
        # 创建一个logger(记录器)
        # 日志记录的工作主要由logger对象来完成。在调用getLogger时要提供logger名称
        # 多次使用相同名称来调用getLogger，返回的是同一对象的引用
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = str_nowTime()
        log_name = os.path.dirname(os.getcwd()) + '/report/logs/' + rq + 'logs.text'
        # 将日志写入磁盘
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.DEBUG)

        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s- %(messsage)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger






