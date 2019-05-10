import logging
from comm.common import *


class Logger:
    def __init__(self):
        rq = str_nowTime()
        path = os.path.dirname(__file__) + '/report/logs/' + rq + 'logs'
        print('logger path')
        print(path)
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.info)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # 设置CMD日志
        # sh = logging.StreamHandler()
        # sh.setFormatter(fmt)
        # sh.setLevel(clevel)
        # 设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(logging.info)
        # self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    # def war(self, message):
    #     self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


# if __name__ == '__main__':
#     logyyx = Logger('yyx.log', logging.ERROR, logging.DEBUG)
#     logyyx.debug('一个debug信息')
#     logyyx.info('一个info信息')
#     logyyx.war('一个warning信息')
#     logyyx.error('一个error信息')
#     logyyx.cri('一个致命critical信息')
